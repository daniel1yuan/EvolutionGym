# Holds Class structure for the Evolution simulation that contains environment
# and simulation logic
# @author: Daniel Yuan
# @file: Terrain.py

# Imports
import random
import warnings
import math
import numpy as np
from PIL import Image
from opensimplex import OpenSimplex

from Tile import *

# Constants
DEFAULT_HEIGHT = 50
DEFAULT_WIDTH = 50
DEFAULT_SEED = 0
MIN_SEED_LENGTH = 3
NOISE_STEP_SIZE = 0.1

# Class definition for the simulation gym
class Terrain (object):
  '''
  Class definition for the Terrain

  @biomes: Array of biomes that will be used for this terrain generation
  @seed: Seed used to seed Perlin noise for terrain generation
  @height: Height of terrain
  @width: Width of terrain
  '''

  def __init__(self, biomes, seed = DEFAULT_SEED, height = DEFAULT_HEIGHT, width = DEFAULT_WIDTH):
    self.seed = seed
    self.height = height
    self.width = width
    self.biomes = biomes

    # Generate terrain from seed
    self.terrain = self.generate_terrain()
    self.generate_biome_map()
    self.generate_energy_map()

  # Generates Terrain using seeded Simplex noise to select biomes based on height map
  def generate_terrain(self):
    simplex_noise = OpenSimplex(self.seed)
    terrain = np.ndarray(shape = (self.width, self.height), dtype=Tile)
    for i in range(self.width):
      for j in range(self.height):
        current_tile_noise = (simplex_noise.noise2d(i * NOISE_STEP_SIZE, j * NOISE_STEP_SIZE) + 1)/2
        biome = self.biomes[int(current_tile_noise * len(self.biomes))]
        terrain[i,j] = Tile(biome)

    return terrain

  # Generates color map for terrain biomes
  def generate_biome_map(self):
    color = np.zeros((self.width, self.height, 3), 'uint8')
    for i in range(self.width):
      for j in range(self.height):
        color[i,j,0] = self.terrain[i,j].biome.r
        color[i,j,1] = self.terrain[i,j].biome.g
        color[i,j,2] = self.terrain[i,j].biome.b

    img = Image.fromarray(color)
    img.show()
    return color

  # Generates energy map for terrain tiles
  def generate_energy_map(self):
    energy = np.zeros((self.width, self.height))
    max_energy = 0
    for i in range(self.width):
      for j in range(self.height):
        energy[i,j] = self.terrain[i,j].energy
        if energy[i,j] > max_energy:
          max_energy = energy[i,j]

    img = Image.fromarray(energy/max_energy*255)
    img.show()
    return energy
