from skimage import io, color, transform, filters


def resize_image(image_path, width, height):
    image = io.imread(image_path)
    resized_image = transform.resize(image, (height, width))
    return resized_image


def convert_to_grayscale(image_path):
    image = io.imread(image_path)
    grayscale_image = color.rgb2gray(image)
    return grayscale_image


def apply_edge_filter(image_path):
    image = io.imread(image_path)
    edge_image = filters.sobel(color.rgb2gray(image))
    return edge_image