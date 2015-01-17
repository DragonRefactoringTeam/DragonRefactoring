#! /usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name = 'Bodies',
    version='1.1.0',
    description='Bodies written by Python and PyOpenGL',
    url = 'http://www.cse.kyoto-su.ac.jp/~drt',
    author = 'Ishihara, Isobe, Ueda, Yoshio',
    author_email = 'g1244163@cse.kyoto-su.ac.jp',
    license = 'The GNU General Public License.',
    long_description = 'ドラゴン・スズメバチ・うさぎ・ペンギン・鬼・赤ちゃんを3次元描画する。',
    platforms = 'OS X (10.10.1)',
    packages=['jp',
              'jp.ac',
              'jp.ac.kyoto_su',
              'jp.ac.kyoto_su.cse',
              'jp.ac.kyoto_su.cse.drt',
              'jp.ac.kyoto_su.cse.drt.Bodies',
              'jp.ac.kyoto_su.cse.drt.MVC',
              'jp.ac.kyoto_su.cse.drt.Parts'],
    )
