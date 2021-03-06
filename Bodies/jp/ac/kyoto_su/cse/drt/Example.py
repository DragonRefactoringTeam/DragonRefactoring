#! /usr/bin/env python
# -*- coding: utf-8 -*-

from jp.ac.kyoto_su.cse.drt.Bodies.Dragon import DragonModel
from jp.ac.kyoto_su.cse.drt.Bodies.Wasp import WaspModel
from jp.ac.kyoto_su.cse.drt.Bodies.Bunny import BunnyModel
from jp.ac.kyoto_su.cse.drt.Bodies.Penguin import PenguinModel
from jp.ac.kyoto_su.cse.drt.Bodies.Oni import OniModel
from jp.ac.kyoto_su.cse.drt.Bodies.Baby import BabyModel

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class Example(object):
    def main(self):
        """ドラゴンを実行するメインプログラム。"""
        a_model = DragonModel()
        a_model.open()
    
        a_model = WaspModel()
        a_model.open()
    
        a_model = BunnyModel()
        a_model.open()
    
        a_model = PenguinModel()
        a_model.open()
    
        a_model = OniModel()
        a_model.open()
    
        a_model = BabyModel()
        a_model.open()
    
        glutMainLoop()
        return 0
