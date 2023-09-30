# Task-1: 
# Neural Network for Handwritten Digits Recognition
This code is designed to build and train a neural network for recognizing handwritten digits from the MNIST dataset. The network architecture includes convolutional layers, max pooling, dropout for regularization, and dense layers. It utilizes the Keras library with a TensorFlow backend.

## Installation and Usage
### Dependencies
- Python 3
- Libraries: `numpy`, `pandas`, `seaborn`, `tensorflow`, `keras`, `matplotlib`

### Installation
1. Ensure you have Python 3 installed on your system.
2. Install the required libraries using the following command:
   ```
   pip install numpy pandas seaborn tensorflow keras matplotlib
   ```
### Usage
1. Open a Python environment (Jupyter Notebook, IDE, or command line).
2. Copy and paste the provided code into your environment.
3. Execute the code.

The code performs the following steps:
1. Imports necessary libraries.
2. Loads and preprocesses the MNIST dataset.
3. Normalizes the data.
4. Displays 10 random images from the training set.
5. Flattens the images and categorizes the labels.
6. Reshapes the data to include a grayscale channel.
7. Builds the neural network with convolutional, max pooling, dropout, and dense layers.
8. Compiles the model and fits it to the dataset for training.
9. Plots graphs showing training vs. validation loss and accuracy over epochs.
10. Evaluates the model on the test dataset and displays the loss and accuracy.
11. Creates predictions on the test dataset.
12. Generates a confusion matrix to evaluate the performance.

## Code Organization
The code is organized as follows:
- Importing libraries: Necessary libraries are imported, including `numpy`, `pandas`, `seaborn`, `tensorflow`, `keras`, and `matplotlib`.
- Data loading and preprocessing: The MNIST dataset is loaded and preprocessed, including normalization, reshaping, and categorization of labels.
- Model building: A neural network architecture is defined using Keras with TensorFlow backend, including convolutional, max pooling, dropout, and dense layers.
- Model training and evaluation: The model is compiled, trained on the training set, and evaluated on the test set. Loss, accuracy, and confusion matrix are displayed.

## Conclusion
This code demonstrates an efficient approach to building and training a neural network for recognizing handwritten digits. It uses convolutional layers for feature extraction, max pooling for down-sampling, and dropout for regularization. The model achieves high accuracy on the MNIST dataset. The code is well-structured, making it easy to understand and modify for similar tasks.
