from PyQt4 import QtGui
from PyQt4 import QtCore


class Node(QtGui.QGraphicsItem):
    def __init__(self, source):
        super().__init__()
        self.setFlag(self.ItemIsMovable, True)
        self.setFlag(self.ItemIsSelectable, True)
        self.pixmap = source.icon().pixmap(32, 32)
        self.source = source
        self.setToolTip(source.path + "." + source.name)

    def paint(self, painter, option, widget):
        if option.state & QtGui.QStyle.State_Selected:
            pen = painter.pen()
            pen.setStyle(QtCore.Qt.DotLine)
            painter.setPen(pen)
            painter.drawRect(self.boundingRect())
        pen = QtGui.QPen(QtGui.QColor(0, 192, 0))
        painter.setPen(pen)
        w = self.pixmap.width()
        h = self.pixmap.height()
        x0 = (48 - w) / 2
        y0 = (48 - h) / 2
        rect = QtCore.QRectF(x0, y0, w, h)
        pixmap_rect = QtCore.QRectF(0, 0, w, h)
        painter.drawRoundRect(rect, 4, 4)
        painter.drawPixmap(rect, self.pixmap, pixmap_rect)
        painter.setBrush(QtGui.QBrush(QtGui.QColor(0, 192, 0)))
        path = QtGui.QPainterPath(QtCore.QPointF(24 - x0/2, 0))
        path.lineTo(24, y0)
        path.lineTo(24 + x0 / 2, 0)
        path.lineTo(24 - x0/2, 0)
        painter.drawPath(path)
        painter.drawEllipse(24 - x0/2, 48 - y0, x0, y0)

    def boundingRect(self):
        return QtCore.QRectF(0, 0, 48, 48)