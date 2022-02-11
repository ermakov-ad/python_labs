import gmsh
import sys
import math
import os

gmsh.initialize()

path = os.path.dirname(os.path.abspath(__file__))
gmsh.merge(os.path.join(path, 'tor.STL'))

angle = 20

# For complex geometries, patches can be too complex, too elongated or too large
# to be parametrized; setting the following option will force the creation of
# patches that are amenable to reparametrization:
forceParametrizablePatches = True

# For open surfaces include the boundary edges in the classification process:
includeBoundary = False

# Force curves to be split on given angle:
curveAngle = 180

gmsh.model.mesh.classifySurfaces(angle * math.pi / 180., includeBoundary,
                                 forceParametrizablePatches,
                                 curveAngle * math.pi / 180.)

# Create a geometry for all the discrete curves and surfaces in the mesh, by
# computing a parametrization for each one
gmsh.model.mesh.createGeometry()

# Create a volume from all the surfaces
s = gmsh.model.getEntities(2)
l = gmsh.model.geo.addSurfaceLoop([s[i][1] for i in range(len(s))])
gmsh.model.geo.addVolume([l])

gmsh.model.geo.synchronize()

# We specify element sizes imposed by a size field
funny = False
f = gmsh.model.mesh.field.add("MathEval")
if funny:
    gmsh.model.mesh.field.setString(f, "F", "1")
else:
    gmsh.model.mesh.field.setString(f, "F", "0.3")
gmsh.model.mesh.field.setAsBackgroundMesh(f)

gmsh.model.mesh.generate(3)
gmsh.write('tor_1.msh')

if '-nopopup' not in sys.argv:
    gmsh.fltk.run()

gmsh.finalize()