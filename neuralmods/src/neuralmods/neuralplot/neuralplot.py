MODULE = 'neuralsetup'
# This module lists physical GPU devices and sets their memory growth to
# true. Enabling memory growth fully allocated a GPU's memory to the
# program's process(es). 

# Copyright (C) Anthony Demong 2021

# >>> Import Libraries <<<

# System:
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'
# TF_CPP_MIN_LOG_LEVEL Options:
#     0: INFO/WARNING/ERROR
#     1: WARNING/ERROR
#     2: ERROR
#     3: NONE
# TensorFlow:
import tensorflow as tf 

# >>> Global Variables <<<
GPU_LIST = 0  # Number of GPUs available for memory growth (default: 0)

# >>> Classes <<<

# >>> Functions <<<

# >>> Module <<<

# List all available GPUs and 
def list_gpu():
    GPU_LIST = tf.config.experimental.list_physical_devices('GPU')
    print(f'TensorFlow GPUs available: {len(GPU_LIST)}')


if __name__ == "__main__":
    list_gpu()  # Lists available GPUs, allocates GPU memory for process
    