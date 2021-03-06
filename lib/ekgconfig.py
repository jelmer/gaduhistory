#-*- coding: utf-8 -*-
#
#copyright 2010 Dominik "Socek" Długajczyk
#
#This file is part of Gadu History.
#
#Gadu History is free software; you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation; either version 2 of the License, or
#(at your option) any later version.
#
#Gadu History is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with Gadu History; if not, write to the Free Software
#Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
#
import os

class EkgConfig(object):
    def __init__(self):
        self._vars = None
    
    def read(self, path='~/.gg/config'):
        self._vars = {}
        lines = open(os.path.expanduser(path), 'r').readlines()
        for line in lines:
            tab = line.split(' ', 1)
            self._vars[tab[0]] = tab[1]
    
    def get(self, name):
        if self._vars.has_key(name):
            return self._vars[name]
    
EKG_CONFIG = EkgConfig()
