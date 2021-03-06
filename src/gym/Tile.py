# Holds Class structure for basic definition of a Tile
# @author: Daniel Yuan
# @file: Tile.py

#imports
from random import Random
import warnings
import math

class Biome(object):
  '''
  Class definition for a Biome in a terrain tile, which describes the attributes of the tile

  Attributes:
    @biome_name (str): The name of this type of biome
    @initial_energy (int): The starting energy of the biome when the terrain is generated
    @energy_generation (int): The amount of energy added into the tile per game tick
    @cost (int): The amount of energy needed to enter the tile
    @r (int [0,255]): Red channel color for biome
    @g (int [0,255]): Green channel color for biome
    @b (int [0,255]): Blue channel color for biome
  '''
  def __init__(self, biome_name, initial_energy, energy_generation, cost):
    self.biome_name = biome_name
    self.initial_energy = initial_energy
    self.energy_generation = energy_generation
    self.cost = cost

    # Generate random color for biome seeded by biome name
    color_rng = Random()
    color_rng.seed(biome_name)
    self.r = int(color_rng.random()*255)
    self.g = int(color_rng.random()*255)
    self.b = int(color_rng.random()*255)

  def set_color(self, r, g, b):
    self.r = r
    self.g = g
    self.b = b


class Tile(object):
  '''
  Class definition for a Tile in terrain

  Attributes:
    @biome (Biome): The biome that this tile hosts
    @energy (int): Amount of energy that this tile currently has
  '''
  def __init__(self, biome):
    self.biome = biome
    self.energy = biome.initial_energy

  # Harvest energy from this tile
  # @energy_consumed: Amount of energy that an entity is trying to consume
  # @return: Amount of energy harvested from tile
  def harvest(self, energy_consumed):
    energy_harvested = 0
    if energy_consumed > self.energy:
      energy_harvested = self.energy
    else:
      energy_harvested = energy_consumed

    self.energy -= energy_harvested

    return energy_harvested

  # Updates the energy in a tile in game tick
  def update(self):
    self.energy += self.biome.energy_generation

  def __str__(self):
    return self.biome.biome_name
