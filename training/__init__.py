"""
Module that contains all the tools needed to load training data and train the conv net.
"""

__author__ = "Matthew Peyrard"
__version__ = 0.1

MATFILE = "digitStruct.mat"
CSVFILE = "digitStruct.csv"

TRAINING_RATIO = 0.9

# TODO: Move into a model module.
IMAGE_SIZE = 32
NUM_LENGTH_CLASSES = 7