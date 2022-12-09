# import os,sys
# sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# from OpenGL.GL import *  # pylint: disable=W0614

from utils.meshViewer import MeshViewWindow

from utils.meshFromObj import meshFromObj
from utils.basicShading import basicShading

if __name__ == "__main__":
    win = MeshViewWindow().init_default()    
    win.add_mesh(meshFromObj(meshName="resources/tu04/suzanne.obj",textureName="resources/tu04/uvmap.DDS",location=[0.0,3.0,0.0]))    
    win.add_mesh(basicShading(meshName="resources/tu04/suzanne.obj",textureName="resources/tu04/uvmap.DDS"))
    win.run()
