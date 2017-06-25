import inspect
import logging
from PyQt4 import QtGui
from PyQt4 import QtCore


class Operator(QtGui.QPushButton):
    def __init__(self, source, path="", parent=None):
        self.name = source.__name__
        super(Operator, self).__init__(self.name, parent)
        self.setFlat(True)
        self.setMaximumHeight(20)
        self.source = source
        self.path = path
        self.docstring = inspect.getdoc(source)
        self.setToolTip(self.docstring)
        sig = inspect.signature(source)
        self.inputs = sig.parameters
        self.setIcon(QtGui.QIcon(":/Canvas/Icons/operator.svg") if len(self.inputs) > 0
                     else QtGui.QIcon(":/Canvas/Icons/dataset.svg"))
        # For the scikit-image we can rely on docstring to get the outputs
        self.outputs = None

    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            data = QtCore.QByteArray()
            mime_data = QtCore.QMimeData()
            mime_data.setData("application/x-operator", data)
            mime_data.setText(self.name)
            drag = QtGui.QDrag(self)
            drag.setMimeData(mime_data)
            drag.setHotSpot(self.rect().topLeft())
            drag.setPixmap(self.icon().pixmap(24, 24))
            drop_action = drag.start(QtCore.Qt.MoveAction)


def populate_layout(layout, path, members):
    for m in members:
        sig = inspect.signature(m[1])
        # For the scikit-image we can rely on docstring to get the outputs
        # For the cv2 try to get from code (not obvious as cv2 is a wrapper of c++ opencv)
        layout.addWidget(Operator(m[1], path))


def fill_skimage(toolbox):
    """Given the particular structure of scikit-image this must be done 'submodule' by 'submodule'"""
    import skimage
    from skimage import color
    f = QtGui.QFrame()
    l = QtGui.QVBoxLayout()
    members = inspect.getmembers(color, predicate=inspect.isfunction)
    populate_layout(l, "skimage.color", members)
    f.setLayout(l)
    toolbox.insertItem(0, f, "color")
    toolbox.setCurrentIndex(0)
    from skimage import data
    f = QtGui.QFrame()
    l = QtGui.QVBoxLayout()
    members = inspect.getmembers(data, predicate=inspect.isfunction)
    populate_layout(l, "skimage.data", members)
    f.setLayout(l)
    toolbox.insertItem(0, f, "data")
    w = toolbox.widget(2)
    toolbox.removeItem(2)
    w.setParent(None)
    logging.info("sckit-image sub-modules loaded")
    return True


def fill_opencv(toolbox):
    try:
        import cv2
    except ImportError:
        return False
    pass