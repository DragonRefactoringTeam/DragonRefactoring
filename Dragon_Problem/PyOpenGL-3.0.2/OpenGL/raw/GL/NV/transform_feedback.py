'''Autogenerated by get_gl_extensions script, do not edit!'''
from OpenGL import platform as _p, constants as _cs, arrays
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_NV_transform_feedback'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_NV_transform_feedback',False)
_p.unpack_constants( """GL_BACK_PRIMARY_COLOR_NV 0x8C77
GL_BACK_SECONDARY_COLOR_NV 0x8C78
GL_TEXTURE_COORD_NV 0x8C79
GL_CLIP_DISTANCE_NV 0x8C7A
GL_VERTEX_ID_NV 0x8C7B
GL_PRIMITIVE_ID_NV 0x8C7C
GL_GENERIC_ATTRIB_NV 0x8C7D
GL_TRANSFORM_FEEDBACK_ATTRIBS_NV 0x8C7E
GL_TRANSFORM_FEEDBACK_BUFFER_MODE_NV 0x8C7F
GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_COMPONENTS_NV 0x8C80
GL_ACTIVE_VARYINGS_NV 0x8C81
GL_ACTIVE_VARYING_MAX_LENGTH_NV 0x8C82
GL_TRANSFORM_FEEDBACK_VARYINGS_NV 0x8C83
GL_TRANSFORM_FEEDBACK_BUFFER_START_NV 0x8C84
GL_TRANSFORM_FEEDBACK_BUFFER_SIZE_NV 0x8C85
GL_TRANSFORM_FEEDBACK_RECORD_NV 0x8C86
GL_PRIMITIVES_GENERATED_NV 0x8C87
GL_TRANSFORM_FEEDBACK_PRIMITIVES_WRITTEN_NV 0x8C88
GL_RASTERIZER_DISCARD_NV 0x8C89
GL_MAX_TRANSFORM_FEEDBACK_INTERLEAVED_COMPONENTS_NV 0x8C8A
GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_ATTRIBS_NV 0x8C8B
GL_INTERLEAVED_ATTRIBS_NV 0x8C8C
GL_SEPARATE_ATTRIBS_NV 0x8C8D
GL_TRANSFORM_FEEDBACK_BUFFER_NV 0x8C8E
GL_TRANSFORM_FEEDBACK_BUFFER_BINDING_NV 0x8C8F
GL_LAYER_NV 0x8DAA""", globals())
glget.addGLGetConstant( GL_TRANSFORM_FEEDBACK_BUFFER_MODE_NV, (1,) )
@_f
@_p.types(None,_cs.GLenum)
def glBeginTransformFeedbackNV( primitiveMode ):pass
@_f
@_p.types(None,)
def glEndTransformFeedbackNV(  ):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLintArray,_cs.GLenum)
def glTransformFeedbackAttribsNV( count,attribs,bufferMode ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,_cs.GLuint,_cs.GLintptr,_cs.GLsizeiptr)
def glBindBufferRangeNV( target,index,buffer,offset,size ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,_cs.GLuint,_cs.GLintptr)
def glBindBufferOffsetNV( target,index,buffer,offset ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,_cs.GLuint)
def glBindBufferBaseNV( target,index,buffer ):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLsizei,arrays.GLintArray,_cs.GLenum)
def glTransformFeedbackVaryingsNV( program,count,locations,bufferMode ):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLcharArray)
def glActiveVaryingNV( program,name ):pass
@_f
@_p.types(_cs.GLint,_cs.GLuint,arrays.GLcharArray)
def glGetVaryingLocationNV( program,name ):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,_cs.GLsizei,arrays.GLsizeiArray,arrays.GLsizeiArray,arrays.GLuintArray,arrays.GLcharArray)
def glGetActiveVaryingNV( program,index,bufSize,length,size,type,name ):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,arrays.GLintArray)
def glGetTransformFeedbackVaryingNV( program,index,location ):pass
@_f
@_p.types(None,_cs.GLsizei,arrays.GLintArray,_cs.GLsizei,arrays.GLintArray,_cs.GLenum)
def glTransformFeedbackStreamAttribsNV( count,attribs,nbuffers,bufstreams,bufferMode ):pass


def glInitTransformFeedbackNV():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )
