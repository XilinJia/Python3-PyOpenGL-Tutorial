# import os,sys
# sys.path.append(os.path.abspath(os.path.dirname(__file__)))


from OpenGL.GL import *  # pylint: disable=W0614

from utils.meshViewer import MeshViewWindow, meshWithRender
from utils.shaderLoader import Shader

import glm

class meshFromArray(meshWithRender):

    def __init__(self, vertex_array, color_array):
        self.vertex_data = vertex_array
        self.color_data = color_array

    def loadShader(self):
        self.shader = Shader()
        self.shader.initShaderFromGLSL(
            ["glsl/tu01/vertex.glsl"], ["glsl/tu01/fragment.glsl"])
        self.MVP_ID = glGetUniformLocation(self.shader.program, "MVP")

    def loadObject(self):
        self.vertexbuffer = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.vertexbuffer)
        glBufferData(GL_ARRAY_BUFFER, len(self.vertex_data)*4, 
            (GLfloat * len(self.vertex_data))(*self.vertex_data), GL_STATIC_DRAW)

        self.vertexLen = len(self.vertex_data)

        self.colorbuffer = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.colorbuffer)
        glBufferData(GL_ARRAY_BUFFER, len(self.color_data)*4, (GLfloat *
                                                               len(self.color_data))(*self.color_data), GL_STATIC_DRAW)
    def loadTexture(self):
        self.texture = None

    def rendering(self, MVP,View,Projection):

        self.shader.begin()
        glUniformMatrix4fv(self.MVP_ID, 1, GL_FALSE,  glm.value_ptr(MVP)  )

        glEnableVertexAttribArray(0)
        glBindBuffer(GL_ARRAY_BUFFER, self.vertexbuffer)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)

        glEnableVertexAttribArray(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.colorbuffer)
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 0, None)
        
        glDrawArrays(GL_TRIANGLES, 0, self.vertexLen)

        glDisableVertexAttribArray(0)
        glDisableVertexAttribArray(1)
        self.shader.end()

from utils.meshFromObj import meshFromObj
from tu_01_color_cube import g_vertex_buffer_data, g_color_buffer_data
if __name__ == "__main__":

    win = MeshViewWindow().init_default()
    win.add_mesh(meshFromObj(meshName="resources/tu04/suzanne.obj",textureName="resources/tu04/uvmap.DDS",location=[0.0,2.0,0.0]))
    win.add_mesh(meshFromArray(g_vertex_buffer_data, g_color_buffer_data))
    win.run()
