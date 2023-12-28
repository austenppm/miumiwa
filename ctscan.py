import numpy as np
import matplotlib.pyplot as plt

def create_circle_image(radius=50, velocity=0, image_size=(100, 100)):
    """
    Create an image of a circle. If velocity is applied, the circle will appear smeared in the x-direction.
    :param radius: Radius of the circle.
    :param velocity: Velocity of the circle in the x-direction.
    :param image_size: Size of the image (width, height).
    :return: Numpy array representing the image.
    """
    image = np.zeros(image_size)
    center = (image_size[0] // 2, image_size[1] // 2)

    for y in range(image_size[1]):
        for x in range(image_size[0]):
            # Adjust x-coordinate based on velocity and y-coordinate
            adjusted_x = x + int(velocity * y)
            if 0 <= adjusted_x < image_size[0]:
                # Check if the point lies inside the circle
                if (center[0] - adjusted_x) ** 2 + (center[1] - y) ** 2 <= radius ** 2:
                    image[y, adjusted_x] = 1
    return image

# Create images of a stationary and a moving circle
stationary_circle = create_circle_image()
moving_circle = create_circle_image(velocity=0.1)

# Plot the images
fig, axes = plt.subplots(1, 2, figsize=(12, 6))
axes[0].imshow(stationary_circle, cmap='gray')
axes[0].set_title('Stationary Circle')
axes[0].axis('off')

axes[1].imshow(moving_circle, cmap='gray')
axes[1].set_title('Moving Circle (with Velocity)')
axes[1].axis('off')

plt.show()

# # Create an image of the moving circle with a higher velocity
# higher_velocity_circle = create_circle_image(velocity=1)

# # Plot the image with higher velocity
# plt.figure(figsize=(6, 6))
# plt.imshow(higher_velocity_circle, cmap='gray')
# plt.title('Moving Circle with Higher Velocity')
# plt.axis('off')
# plt.show()
