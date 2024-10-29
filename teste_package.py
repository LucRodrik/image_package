from image_package import resize_image, convert_to_grayscale, apply_edge_filter
from matplotlib import pyplot as plt


# Teste image resizing
resized_image = resize_image('path/to/image.jpg', 200, 200)
plt.imshow(resized_image)
plt.title('Resized Image')
plt.show()

# Test grayscale conversion
grayscale_image = convert_to_grayscale('path/to/image.jpg')
plt.imshow(grayscale_image, cmap='gray')
plt.title('Grayscale Image')
plt.show()


# Test edge detection filter
edge_image = apply_edge_filter('path/to/image.jpg')
plt.imshow(edge_image, cmap='gray')
plt.title('Edge Detected Image')
plt.show()