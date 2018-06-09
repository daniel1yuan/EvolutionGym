# Holds structure for gym environment
# @author: Daniel Yuan
# @file: sim.py

# Imports
from Terrain import Terrain

# Constants
DEFAULT_HEIGHT = 50
DEFAULT_WIDTH = 50
DEFAULT_SEED = 0

class BaseSimulation(object):
    '''
    Class definition for Simulation, which holds training parameters

    Attributes:
    @agents ([Agent]): Agents that are part of simulation
    @biomes ([Biome]): Biomes used in this simulation
    @seed (int): Seed used to seed Perlin noise for terrain generation
    @tick (int): Current game tick
    @visualizer (PyQt Application): Visualizer application for GUI
    '''

    def __init__(self, agents, width = DEFAULT_WIDTH, height = DEFAULT_HEIGHT, biomes = None, seed = DEFAULT_SEED):
        self.tick = 0
        self.seed = seed
        self.width = width
        self.height = height
        self.agents = agents
        if biomes:
            self.biomes = biomes
        else:
            self.biomes = self._generate_biomes()

        self.terrain = Terrain(self.biomes, width, height, seed)
        self.visualizer = self._generate_gui()

    def __str__(self):
        return ""

    def run(self):
        pass

    def set_gui_update_signal(self, signal):
        self.gui_update_signal = signal

    def _reset(self):
        print ("test")

    def _generate_biomes(self):
        print ("test")

    def _generate_gui(self):
        print ("test")
