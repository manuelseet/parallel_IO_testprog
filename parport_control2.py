import sys
import time
from psychopy import parallel
try:
    from PySide import QtGui
except ImportError:
    from PyQt4 import QtGui

# Was at 0x0378 on the old PC
PARALLEL_PORT_ADDRESS = 0xd050

class PortController(QtGui.QDialog):


    def __init__(self, parent=None):
        super(PortController, self).__init__(parent)

        self.port = parallel.ParallelPort(PARALLEL_PORT_ADDRESS)
        self.port.setData(0)

        self._setup_button()

        self.setWindowTitle('Click to fire.')
        self.resize(250, 200)
        self.show()

    def _setup_button(self):
        self.fire_button = QtGui.QPushButton('Fire', self)
        self.fire_button.clicked.connect(self.fire)

        button_layout = QtGui.QGridLayout()
        button_layout.addWidget(self.fire_button, 0, 0)

        self.setLayout(button_layout)


    def fire(self):
        time.sleep(0.01)
        self.port.setData(5)
        time.sleep(0.01)
        self.port.setData(0)

        self.fire_button.setEnabled(False)
        self.fire_button.setText('...')
        self.repaint()
        app.processEvents()

        time.sleep(2)

        self.fire_button.setEnabled(True)
        self.fire_button.setText('Fire')
        self.fire_button.setFocus()
        self.repaint()
        app.processEvents()



if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    controller = PortController()
    controller.exec_()
    app.exit()