# Main File for Launching Evolution Gym
# @author: Daniel Yuan
# @file: main.py

from Tile import Biome
from sim import BaseSimulation
from gui import GUI

def main():
    biomes = []
    biomes.append(Biome("test", 1, 4, 5))
    biomes.append(Biome("test1", 2, 4, 5))
    biomes.append(Biome("test2", 3, 4, 5))
    biomes.append(Biome("test3", 4, 4, 5))
    biomes.append(Biome("test4", 5, 4, 5))
    biomes.append(Biome("test5", 6, 4, 5))
    biomes.append(Biome("test6", 7, 4, 5))
    sim = BaseSimulation([], biomes=biomes)
    gui = GUI(sim)

    # terrain = Terrain(biomes, 10, 200, 200)

if __name__ == '__main__':
    main()
