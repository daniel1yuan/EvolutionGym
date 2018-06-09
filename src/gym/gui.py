# Holds structure for gym GUI
# @author: Daniel Yuan
# @file: gui.py

import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QThread, QObject, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QPainter, QBrush, QColor

class SimulationThread(QThread):
    def __init__(self, sim, signal):
        super(SimulationThread, self).__init__()
        self.simulation = sim
        self.gui_update_signal = signal
        self.simulation.set_gui_update_signal(self.gui_update_signal)

    def __del__(self):
        self.wait()

    def run(self):
        self.simulation.run()

    def get_gui_update_signal(self):
        return self.gui_update_signal

class GUI(object):
    def __init__(self, sim):
        # Initialize Application
        self.app = QtWidgets.QApplication(sys.argv)

        # Launch Simulation Thread:
        self.signal = GUIUpdateSignal()
        self.simulation_thread = SimulationThread(sim, self.signal)
        self.simulation_window = SimulationWindow(sim)
        self.simulation_window.connect_gui_update_signal(self.signal)
        self.simulation_thread.start()

        # Initialize Window and run app
        self.simulation_window.show()
        sys.exit(self.app.exec_())

class GUIUpdateSignal(QObject):
    signal = pyqtSignal(tuple)

    def __init__(self):
        super(GUIUpdateSignal, self).__init__()

    def emit(self, data):
        self.signal.emit(data)

class SimulationWindow(QtWidgets.QMainWindow):
    def __init__(self, sim):
        super(SimulationWindow, self).__init__()
        self.simulation = sim
        self._initializeGUI()

        self.environment_display = None
        self.status_display = None

    def connect_gui_update_signal(self, signal):
        self.signal = signal
        signal.signal.connect(self._updateGUI)

    def _updateGUI(self, sim_state):
        pass

    def _initializeGUI(self):
        self._initializeMenu()
        self.setWindowTitle(str(self.simulation))
        layout = QtWidgets.QHBoxLayout()

    def _initializeMenu(self):
        self.main_menu = self.menuBar()
        file_menu = self.main_menu.addMenu('File')
        edit_menu = self.main_menu.addMenu('Edit')
        help_menu = self.main_menu.addMenu('Help')
