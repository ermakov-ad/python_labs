import numpy as np
import gmsh
import vtk
import math
import os

# Класс расчётной сетки
class CalcMesh:

    # Конструктор сетки size1 x size2 точек с шагом step по пространству
    def __init__(self, size_x, size_y, step):
        # 2D-сетка из расчётных точек, у каждой из которых, тем не менее, 3 координаты
        self.nodes = np.mgrid[0:(size_x-1):np.complex128(size_x), -((size_y-1)/2):((size_y-1)/2):np.complex128(size_y)]
        self.nodes *= step
        self.nodes = np.append(self.nodes, [np.zeros(shape=(size_x, size_y), dtype=np.double)], 0)

        # Модельная скалярная величина распределена как-то вот так
        self.smth = np.power(self.nodes[0], 2) + np.power(self.nodes[1], 2)
        self.velocity = np.zeros(shape=(3, size_x, size_y), dtype=np.double)

    # метод пересчёта скорости
    def vel(self, t, l):
        self.velocity[1] = -omega(t) * self.nodes[2] * self.nodes[0]/l
        self.velocity[2] = omega(t) * self.nodes[1] * self.nodes[0]/l

    # Метод отвечает за выполнение для всей сетки шага по времени величиной tau
    def move(self, tau, t, l):
        # пересчитываем скорости
        self.vel(t, l)
        r0 = np.multiply(self.nodes[1], self.nodes[1]) + np.multiply(self.nodes[2], self.nodes[2])
        self.nodes += self.velocity * tau
        r = np.multiply(self.nodes[1], self.nodes[1]) + np.multiply(self.nodes[2], self.nodes[2])
        self.nodes[1] = np.multiply(np.sqrt(np.multiply(r0, 1/r)), self.nodes[1])
        self.nodes[2] = np.multiply(np.sqrt(np.multiply(r0, 1/r)), self.nodes[2])

    # Метод отвечает за запись текущего состояния сетки в снапшот в формате VTK
    def snapshot(self, snap_number):
        # Сетка в терминах VTK
        structuredGrid = vtk.vtkStructuredGrid()
        # Точки сетки в терминах VTK
        points = vtk.vtkPoints()

        # Скалярное поле на точках сетки
        smth = vtk.vtkDoubleArray()
        smth.SetName("smth")

        # Векторное поле на точках сетки
        vel = vtk.vtkDoubleArray()
        vel.SetNumberOfComponents(3)
        vel.SetName("vel")

        # Обходим все точки нашей расчётной сетки
        # Делаем это максимально неэффективным, зато наглядным образом
        lengh1 = len(self.nodes[0])
        lengh2 = len(self.nodes[0][0])
        for i in range(0, lengh1):
            for j in range(0, lengh2):
                # Вставляем новую точку в сетку VTK-снапшота
                points.InsertNextPoint(self.nodes[0][i,j], self.nodes[1][i,j], self.nodes[2][i,j])
                # Добавляем значение скалярного поля в этой точке
                smth.InsertNextValue(self.smth[i,j])
                # Добавляем значение векторного поля в этой точке
                vel.InsertNextTuple((self.velocity[0][i,j], self.velocity[1][i,j], self.velocity[2][i,j]))

        # Задаём размеры VTK-сетки (в точках, по трём осям)
        structuredGrid.SetDimensions(lengh1, lengh2, 1)
        # Грузим точки в сетку
        structuredGrid.SetPoints(points)

        # Присоединяем векторное и скалярное поля к точкам
        structuredGrid.GetPointData().AddArray(smth)
        structuredGrid.GetPointData().AddArray(vel)

        # Создаём снапшот в файле с заданным именем
        writer = vtk.vtkXMLStructuredGridWriter()
        writer.SetInputDataObject(structuredGrid)
        writer.SetFileName("spiral-" + str(snap_number) + ".vts")
        writer.Write()

# Размер расчётной сетки, точек на сторону
size1 = 40
size2 = 20
# Шаг точек по пространству
h = 0.1
# Шаг по времени
tau = 0.01

# Создаём сетку заданного размера
m = CalcMesh(size1, size2, h)
# Пишем её начальное состояние в VTK
m.snapshot(0)
n = 201 # количество шагов

A = 10.2
T = 2
# угловая скорость
def omega(t):
    return A*math.cos(2*math.pi*t/T)
# Делаем шаги по времени,
# на каждом шаге считаем новое состояние и пишем его в VTK
for i in range(1, n):
    m.move(tau, i*tau, h*size1)
    m.snapshot(i)
    if i % int(n/10) == 0:
        print(str(int(i/int(n/100))) + "% of gif was saved")
