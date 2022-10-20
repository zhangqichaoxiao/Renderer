# -*- coding:utf-8 -*-
from PySide2.QtGui import QPainter
from PySide2.QtWidgets import QMainWindow

from src.Vector import vector


class Renderer(object):
    def __init__(self, painter: QPainter, context: QMainWindow):
        self.context = context
        self.painter = painter

    def update(self):
        self.context.update()

    def draw_line(self, start: vector, end: vector):
        pass