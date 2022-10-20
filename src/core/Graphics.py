# -*- coding:utf-8 -*-
import math

from src.common.Singleton import Singleton


class Graphics(Singleton):
    def _initialize(self, context, canvas):
        self.context = context
        self.canvas = canvas

    def set_pixel(self, x, y, color):
        self.context.save()
        self.context.setPen(color)
        self.context.drawPoint(int(x), int(y))
        self.context.restore()

    def dda_line(self, a, b, color):
        ax = a.x; ay = a.y; bx = b.x; by = b.y
        dx = b.x - a.x
        dy = b.y - a.y

        k = dy / dx
        if abs(k) < 1:
            y = a.y
            if a.x > b.x:
                ax = b.x; bx = a.x; y = b.y
            for x in range(int(ax), int(bx + 1), 1):
                self.set_pixel(x, math.trunc(y + 0.5), color)
                y += k
        else:
            x = a.x
            if a.y > b.y:
                ay = b.y; by = a.y; x = b.x
            k2 = 1.0 / k
            for y in range(int(ay), int(by + 1), 1):
                self.set_pixel(math.trunc(x + 0.5), y, color)
                x += k2

    def clear(self, color):
        self.context.fillRect(0, 0, self.canvas.width(), self.canvas.height(), color)
