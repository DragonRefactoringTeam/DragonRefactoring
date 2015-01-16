'''OpenGL extension AMD.vertex_shader_viewport_index

This module customises the behaviour of the 
OpenGL.raw.GL.AMD.vertex_shader_viewport_index to provide a more 
Python-friendly API

Overview (from the spec)
	
	The gl_ViewportIndex built-in variable was introduced by the
	ARB_viewport_array extension and OpenGL 4.1. This variable is available
	in un-extended OpenGL only to the geometry shader. When written in the
	geometry shader, it causes geometry to be directed to one of an array
	of several independent viewport rectangles.
	
	In order to use any viewport other than zero, a geometry shader must be
	present. Geometry shaders introduce processing overhead and potential
	performance issues. This extension exposes the gl_ViewportIndex built-in
	variable to the vertex shader, allowing the functionality introduced by
	ARB_viewport_array to be accessed without requiring a geometry shader to
	be present.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/AMD/vertex_shader_viewport_index.txt
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.AMD.vertex_shader_viewport_index import *
### END AUTOGENERATED SECTION