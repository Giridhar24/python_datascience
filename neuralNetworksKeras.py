# Topic of the Day: Neural Networks (Keras)
#
# Explanation: We learned the "Neuron" yesterday. Now let's connect them. Keras (running on TensorFlow) makes building Neural Networks easy.
#
# Sequential: A linear stack of layers.
#
# Dense: A layer where every neuron is connected to every neuron in the next layer.

# pip install tensorflow
import tensorflow as tf
from tensorflow import keras

# 1. Define the Model
model = keras.Sequential([
    # Input Layer: 2 features (e.g., Height, Weight)
    # Hidden Layer: 4 neurons, Activation='relu' (Standard filter)
    keras.layers.Dense(4, input_shape=(2,), activation='relu'),

    # Output Layer: 1 neuron (0 or 1 classification), Activation='sigmoid'
    keras.layers.Dense(1, activation='sigmoid')
])

# 2. Compile (Tell it how to learn)
# Optimizer='adam' (The standard algorithm to adjust weights)
# Loss='binary_crossentropy' (Standard error function for Yes/No questions)
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

print(model.summary())