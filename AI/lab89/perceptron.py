import numpy as np

def heaviside_step(z):
    """Heaviside step function as hard limiter"""
    return 1 if z > 0 else 0

def perceptron_output(inputs, weights, bias):
    """
    Computes the output of a perceptron
    
    Parameters:
    inputs : list or np.array of inputs [x1, x2, ..., xm]
    weights : list or np.array of weights [w1, w2, ..., wm]
    bias : float, external bias b

    Returns:
    int : 0 or 1 depending on step activation
    """
    # Linear combiner: weighted sum + bias
    z = np.dot(weights, inputs) + bias
    
    # Apply hard limiter
    return heaviside_step(z)
