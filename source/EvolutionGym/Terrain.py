# Holds Class structure for the Evolution simulation that contains environment
# and simulation logic
# @author: Daniel Yuan
# @file: Terrain.py

# Imports
import random
import warnings
import math

# Constants
DEFAULT_HEIGHT = 200
DEFAULT_WIDTH = 200
DEFAULT_SEED = None
MIN_SEED_LENGTH = 3

TERRAIN_SEED_SUFFIX = "Terrain"
TILE_SEED_SUFFIX = "Tile"


# Class definition for the simulation gym
class Terrain (object):
  # Initializes an Evolution Gym given a seed
  # @param: seed - seed for generating terrain
  def __init__(self, seed = DEFAULT_SEED, height = DEFAULT_HEIGHT, width = DEFAULT_WIDTH):
    self.seed = seed
    self.terrainRNG = random.Random()
    self.tileRNG = random.Random()

    # Apply seed to pseudo random generator
    self.parseSeed(seed)

  # Apply seed to pseudo RNGs for terrain generation
  def parseSeed(self, seed):
    if (seed):
      # Terrain seed: 1st half of seed value
      # tile seed: 2nd half of seed value
      terrainSeed = seed + TERRAIN_SEED_SUFFIX
      tileSeed = seed + TILE_SEED_SUFFIX
      self.terrainRNG.seed(terrainSeed)
      self.tileRNG.seed(tileSeed)
    else:
      # If no seed is specified, throw a warning, but still contiue with terrain generation
      warnings.warn("Unusable Seed. Generating completely random terrain")

  # Generates terrain based on the pseudo RNG specified by seed
  def generateTerrain():
    print ("test")
