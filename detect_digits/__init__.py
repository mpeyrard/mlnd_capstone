"""

"""

__author__ = 'Matthew Peyrard'
__version__ = 0.1

# Images are normalized to 32x32x3
IMAGE_SIZE = 32
IMAGE_COLOR_CHANNELS = 3

MAX_DIGITS = 5
# The digit may be of discrete length 0-5, and we also add another class for 6+.
NUM_LENGTH_CLASSES = 7
# Each digit may be 0-9, and we also add another class to represent 'not present'.
NUM_DIGIT_CLASSES = 11
EMPTY_DIGIT_LABEL = NUM_DIGIT_CLASSES-1

# Convolutional layers hyper-parameters
MAXPOOL_KERNEL_SIZE = 2
CONV_KERNEL_SIZE = 5

# Layer sizes
CONV1_DEPTH = 48
CONV2_DEPTH = 64
CONV3_DEPTH = 128
CONV4_DEPTH = 160
CONV5_DEPTH = 192
CONV6_DEPTH = 192
CONV7_DEPTH = 192
CONV8_DEPTH = 192
FC1_LENGTH = 4096
FC2_LENGTH = 4096

# Layer shapes
# CONV1_SHAPE = [CONV_KERNEL_SIZE, CONV_KERNEL_SIZE, IMAGE_COLOR_CHANNELS, CONV1_DEPTH]
# CONV2_SHAPE = [CONV_KERNEL_SIZE, CONV_KERNEL_SIZE, CONV1_DEPTH, CONV2_DEPTH]
# CONV3_SHAPE = [CONV_KERNEL_SIZE, CONV_KERNEL_SIZE, CONV2_DEPTH, CONV3_DEPTH]
# FLATTENED_CONV_LAYER_LENGTH = CONV3_DEPTH * (IMAGE_SIZE / MAXPOOL_KERNEL_SIZE ** NUM_MAXPOOL_LAYERS) ** 2
# FC1_SHAPE = [FLATTENED_CONV_LAYER_LENGTH, FC1_LENGTH]
# FC2_SHAPE = [FC1_LENGTH, FC2_LENGTH]
#
# DIGIT_OUTPUT_LENGTH = NUM_DIGIT_CLASSES
# DIGIT_OUTPUT_SHAPE = [FC2_LENGTH, DIGIT_OUTPUT_LENGTH]
