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
NUM_MAXPOOL_LAYERS = 2
MAXPOOL_KERNEL_SIZE = 2
CONV_KERNEL_SIZE = 5

# Layer sizes
CONV1_DEPTH = 16
CONV2_DEPTH = 32
CONV3_DEPTH = 48
CONV4_DEPTH = 64
CONV5_DEPTH = 64
CONV6_DEPTH = 192
CONV7_DEPTH = 192
CONV8_DEPTH = 192
FC_LENGTH = 2048

# Layer shapes
CONV1_SHAPE = [CONV_KERNEL_SIZE, CONV_KERNEL_SIZE, IMAGE_COLOR_CHANNELS, CONV1_DEPTH]
CONV2_SHAPE = [CONV_KERNEL_SIZE, CONV_KERNEL_SIZE, CONV1_DEPTH, CONV2_DEPTH]
CONV3_SHAPE = [CONV_KERNEL_SIZE, CONV_KERNEL_SIZE, CONV2_DEPTH, CONV3_DEPTH]
CONV4_SHAPE = [CONV_KERNEL_SIZE, CONV_KERNEL_SIZE, CONV3_DEPTH, CONV4_DEPTH]
CONV5_SHAPE = [CONV_KERNEL_SIZE, CONV_KERNEL_SIZE, CONV4_DEPTH, CONV5_DEPTH]
CONV6_SHAPE = [CONV_KERNEL_SIZE, CONV_KERNEL_SIZE, CONV5_DEPTH, CONV6_DEPTH]
CONV7_SHAPE = [CONV_KERNEL_SIZE, CONV_KERNEL_SIZE, CONV6_DEPTH, CONV7_DEPTH]
CONV8_SHAPE = [CONV_KERNEL_SIZE, CONV_KERNEL_SIZE, CONV7_DEPTH, CONV8_DEPTH]
FEATURE_VECTOR_LENGTH = CONV3_DEPTH * (IMAGE_SIZE / MAXPOOL_KERNEL_SIZE**NUM_MAXPOOL_LAYERS)**2
FC_SHAPE = [FEATURE_VECTOR_LENGTH, FC_LENGTH]
