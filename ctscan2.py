from skimage.transform import radon, iradon
import numpy as np
import matplotlib.pyplot as plt

def create_simple_object(image_size=(100, 100), shape='circle'):
    """
    Create a simple 2D object (circle or square).
    :param image_size: Size of the image (width, height).
    :param shape: Shape of the object ('circle' or 'square').
    :return: Numpy array representing the image.
    """
    image = np.zeros(image_size)
    center = (image_size[0] // 2, image_size[1] // 2)
    radius = min(image_size) // 4

    for y in range(image_size[1]):
        for x in range(image_size[0]):
            if shape == 'circle':
                if (center[0] - x) ** 2 + (center[1] - y) ** 2 <= radius ** 2:
                    image[y, x] = 1
            elif shape == 'square':
                if abs(center[0] - x) <= radius and abs(center[1] - y) <= radius:
                    image[y, x] = 1
    return image

# Create a simple object
object_image = create_simple_object(shape='circle')

# Simulate X-ray projections (Radon transform) from different angles
theta = np.linspace(0., 180., max(object_image.shape), endpoint=False)
sinogram = radon(object_image, theta=theta)

# Reconstruct the image from projections (inverse Radon transform)
reconstruction = iradon(sinogram, theta=theta, filter_name='ramp')

# Plot the original object, the sinogram, and the reconstruction
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
axes[0].imshow(object_image, cmap='gray')
axes[0].set_title('Original Object')
axes[0].axis('off')

axes[1].imshow(sinogram, cmap='gray', extent=(0, 180, 0, sinogram.shape[0]), aspect='auto')
axes[1].set_title('Sinogram (Projections)')
axes[1].set_xlabel('Angle (degree)')
axes[1].set_ylabel('Projection position')

axes[2].imshow(reconstruction, cmap='gray')
axes[2].set_title('Reconstructed Image')
axes[2].axis('off')

plt.tight_layout()
plt.show()
