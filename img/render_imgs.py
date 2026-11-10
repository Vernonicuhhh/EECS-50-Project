from PIL import Image
import numpy as np

size = 1024
y, x = np.mgrid[0:size, 0:size] - size / 2

r_squared = y**2 + x**2

# Repeated circle
# k = circle width amplitude
# 0.5 on before + increments the pixel brightness since cos(x) = -1<n<1
# I = 1/2 + 0.5cos(kr^2)
k = np.pi / size
image_circle = 0.5 + 0.5 * np.cos(k * r_squared)


# striped
D = 4  # your downsampling factor
period = 1.8 * D  # just under 2·D pixels
stripes = 0.5 + 0.5 * np.cos(2 * np.pi * x / period)


# slanted edge
angle = np.deg2rad(5)
edge = (x * np.cos(angle) + y * np.sin(angle) > 0).astype(float)

# star
theta = np.arctan2(y, x)
star = (np.sin(36 * theta) > 0).astype(float)

# white square
square = np.zeros((size, size))
square[256:768, 256:768] = 1.0


Image.fromarray((image_circle * 255).round().astype(np.uint8)).save("zone_plate.png")
Image.fromarray((stripes * 255).round().astype(np.uint8)).save("stripes.png")
Image.fromarray((edge * 255).round().astype(np.uint8)).save("slanted_edge.png")
Image.fromarray((star * 255).round().astype(np.uint8)).save("siemmens_star.png")
Image.fromarray((square * 255).round().astype(np.uint8)).save("square.png")
