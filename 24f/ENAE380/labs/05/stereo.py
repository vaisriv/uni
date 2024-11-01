# Vai Srivastava - 0106

import numpy as np
import matplotlib.pyplot as plt
import skimage
import skimage.io


def display(img, colorbar=False):
    "Displays an image."
    plt.figure(figsize=(10, 10))
    if len(img.shape) == 2:
        i = skimage.io.imshow(img, cmap="gray")
    else:
        i = skimage.io.imshow(img)
    if colorbar:
        plt.colorbar(i, shrink=0.5, label="depth")
    plt.tight_layout()
    plt.show()


def make_pattern(shape=(16, 16), levels=64):
    "Creates a pattern from gray values."
    return np.random.randint(0, levels - 1, shape) / levels


def make_rgb_pattern(shape=(16, 16), levels=64):
    "Creates a colored pattern from RGB values."
    # generate random values for each RGB channel, normalize them
    return np.random.randint(0, levels, (*shape, 3)) / (levels - 1)


def create_circular_depthmap(shape=(600, 800), center=None, radius=100):
    "Creates a circular depthmap, centered on the image."
    depthmap = np.zeros(shape, dtype=float)
    r = np.arange(depthmap.shape[0])
    c = np.arange(depthmap.shape[1])
    R, C = np.meshgrid(r, c, indexing="ij")
    if center is None:
        center = np.array([r.max() / 2, c.max() / 2])
    d = np.sqrt((R - center[0]) ** 2 + (C - center[1]) ** 2)
    depthmap += d < radius
    return depthmap


def create_square_depthmap(shape=(600, 800), center=None, side_length=100):
    "Creates a square depthmap, centered on the image."
    depthmap = np.zeros(shape, dtype=float)  # initialize blank depthmap
    x = np.arange(depthmap.shape[0])  # row indices
    y = np.arange(depthmap.shape[1])  # column indices
    X, Y = np.meshgrid(x, y, indexing="ij")  # create grid for mask
    if center is None:
        center = np.array([x.max() / 2, y.max() / 2])  # set default center
    half_side = side_length / 2.0  # calculate half of side length
    mask = (np.abs(X - center[0]) <= half_side) & (np.abs(Y - center[1]) <= half_side)  # create square mask
    depthmap[mask] = 1.0  # apply mask to depthmap
    return depthmap


def normalize(depthmap):
    "Normalizes values of depthmap to [0, 1] range."
    if depthmap.max() > depthmap.min():
        return (depthmap - depthmap.min()) / (depthmap.max() - depthmap.min())
    else:
        return depthmap


def make_autostereogram(depthmap, pattern, shift_amplitude=0.1, invert=False):
    "Creates an autostereogram from depthmap and pattern (grayscale or color)."
    depthmap = normalize(depthmap)  # normalize depthmap
    if invert:
        depthmap = 1 - depthmap  # invert depthmap if specified

    # check if pattern is grayscale or color
    if pattern.ndim == 2:
        num_channels = 1  # grayscale pattern
        pattern_height, pattern_width = pattern.shape
    else:
        pattern_height, pattern_width, num_channels = pattern.shape  # color pattern

    # initialize autostereogram with correct shape
    autostereogram_shape = depthmap.shape + (
        (num_channels,) if num_channels > 1 else ()
    )
    autostereogram = np.zeros(autostereogram_shape, dtype=pattern.dtype)  # create blank autostereogram

    # iterate over each pixel in autostereogram
    for r in range(autostereogram.shape[0]):
        for c in range(autostereogram.shape[1]):
            if c < pattern_width:
                # copy pattern directly for first pattern_width columns
                if num_channels == 1:
                    autostereogram[r, c] = pattern[r % pattern_height, c]
                else:
                    autostereogram[r, c, :] = pattern[r % pattern_height, c, :]
            else:
                # calculate horizontal shift based on depth
                shift = int(depthmap[r, c] * shift_amplitude * pattern_width)
                src_c = c - pattern_width + shift  # source column after shift
                if num_channels == 1:
                    autostereogram[r, c] = autostereogram[r, src_c]
                else:
                    autostereogram[r, c, :] = autostereogram[r, src_c, :]  # copy shifted pixel
    return autostereogram


# create and display a sample pattern
pattern = make_rgb_pattern(shape=(128, 64))
display(pattern)

# create and display a square depthmap with a colorbar
depthmap = create_square_depthmap(side_length=150)
display(depthmap, colorbar=True)

# create and display autostereogram based on depthmap and pattern
autostereogram = make_autostereogram(depthmap, pattern, invert=True)
display(autostereogram)

# create a composite depthmap with multiple squares
depthmap = (
    create_square_depthmap(center=(200, 300), side_length=100)
    + create_square_depthmap(center=(450, 500), side_length=100)
    + create_square_depthmap(center=(200, 550), side_length=150)
)
depthmap = normalize(depthmap)  # normalize combined depthmap
display(depthmap, colorbar=True)  # display composite depthmap with colorbar

# generate and display autostereogram based on composite depthmap
autostereogram = make_autostereogram(depthmap, pattern)
display(autostereogram)
