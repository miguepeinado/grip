from PyQt4 import QtGui
from diagram.node import Node


class Canvas(QtGui.QGraphicsView):
    def __init__(self, parent=None):
        super(Canvas, self).__init__(parent)
        self.scene = QtGui.QGraphicsScene(0, 0, 1000, 1000, self)
        self.setScene(self.scene)
        self.setDragMode(QtGui.QGraphicsView.RubberBandDrag)
        self.setRenderHints(QtGui.QPainter.Antialiasing | QtGui.QPainter.TextAntialiasing)
        self.scene.selectionChanged.connect(self.update_toolbar)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        event.accept()

    def dragMoveEvent(self, event):
        event.accept()

    def dropEvent(self, event):
        if event.mimeData().hasFormat("application/x-operator"):
            node = Node(event.source())
            pos = self.mapToScene(event.pos())
            node.setPos(pos)
            self.scene.addItem(node)
            node.setSelected(True)

    def update_toolbar(self):
        pass