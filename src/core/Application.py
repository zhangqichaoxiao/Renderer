# -*- coding:utf-8 -*-
import math
import sys
import time

from PySide2 import QtWidgets, QtGui
from PySide2.QtCore import Qt, QTimer, QDateTime, QObject

from src.Vector import vector
from src.common.Singleton import Singleton
from src.core.Graphics import Graphics

app = QtWidgets.QApplication(sys.argv)


class AppWindow(QtWidgets.QMainWindow):
    def __init__(self, app):
        self.app = app
        super(AppWindow, self).__init__()

    def closeEvent(self, event):
        super(AppWindow, self).closeEvent(event)
        self.app.on_close(event)


class Application(Singleton):
    def __init__(self, size):
        super(Application, self).__init__()

    def _initialize(self, size):
        self.window = AppWindow(self)
        self.size = size
        self.window.setFixedSize(*size)

        self._label = QtWidgets.QLabel()
        self.canvas = QtGui.QPixmap(*size)
        self._label.setPixmap(self.canvas)
        self.window.setCentralWidget(self._label)
        self.painter = QtGui.QPainter(self._label.pixmap())
        self.graphics = Graphics(self.painter, self.canvas)
        self.graphics.clear(Qt.black)

        self.lb_fps = QtWidgets.QLabel(self.window)
        self.lb_fps.setStyleSheet("QLabel { color : white; }")


        # 初始化帧率
        self.fps = 60
        self.fps_interval = 1000.0 / self.fps
        self.start_time = self.cur_time()
        self.last = self.start_time
        self.tick_timer = QTimer(self.window)
        self.tick_timer.timeout.connect(self.update)
        self.tick_timer.setTimerType(Qt.PreciseTimer)
        self.tick_timer.start(0)


        # 初始化成员数据
        self.angle = 0

    def update(self):
        now = self.cur_time()
        elapsed = now - self.last
        if elapsed < self.fps_interval:
            return
        self.last = now - elapsed % self.fps_interval
        self.lb_fps.setText("FPS: %d" % (1000 / elapsed))
        self.render(elapsed / 1000.0)
        self._label.update()

    def render(self, dt):
        g = self.graphics
        g.clear(Qt.black)
        pa = vector(self.size[0] * 0.5, self.size[1] * 0.5)
        radius = 200

        self.angle += dt * 20
        angle = self.angle / 180 * math.pi

        # print(angle)
        s, c = math.sin(angle), math.cos(angle)
        pb = pa + vector(c, s) * radius

        # bresenham算法
        self.painter.setPen(Qt.white)
        g.dda_line(vector(100, 100), vector(300, 300), Qt.yellow)
        g.dda_line(pa, pb, Qt.white)

    def run(self):
        self.window.show()
        sys.exit(app.exec_())

    def on_close(self, event):
        app.exit(0)

    def cur_time(self):
        return round(time.time() * 1000)