# Holds Class structure for basic definition of a biome
# @author: Daniel Yuan
# @file: Biome.py

#imports
import random
import warnings
import math

# Constants
DEFAULT_BIOME = {
  name: 'default',
  initial_energy: {low: 100, high: 200},
  cost_to_occupy: {low: 0, high: 10},
  energy_production: {low: 0, high: 2}
}
DEFAULT_SEED = None

INITIAL_ENERGY_SUFFIX = "Initial_Energy"
COST_TO_OCCUPY_SUFFIX = "Cost_To_Occupy"
ENERGY_PRODUCTION_SUFFIX = "Energy_Production"

# Class definition ofr a biome
class Biome (object):
  def __init__(self, biomeType = DEFAULT_BIOME, seed = DEFAULT_SEED):
    self.name = biomeType.name

  def generateValues(seed, biomeType):
    biomeRNG = random.Random()
    biomeRNG.seed(seed)
    initialEnergyRange = biomeType.inital_energy
    costToOccupyRange = biomeType.cost_to_occupy
    energyProduction
    self.initialEnergy = biomeRNG.randint(biomeType.initial_energy.low, biometype.initialEnergy.high)
    self.initialEnergy = biomeRNG.randint(biomeType.initial_energy.low, biometype.initialEnergy.high)
    self.initialEnergy = biomeRNG.randint(biomeType.initial_energy.low, biometype.initialEnergy.high)
    self.initialEnergy = biomeRNG.randint(biomeType.initial_energy.low, biometype.initialEnergy.high)
