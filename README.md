# image_processing_package

Description. 
This package provides basic functions for loading, converting and resizing images using `scikit-image`.


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install package_name

```bash
pip install image_package
```

## Usage

```from image_processing import load_image, convert_to_grayscale, resize_image

# Load image
image = load_image("caminho/para/imagem.jpg")

# Convert to gray scale
grayscale_image = convert_to_grayscale(image)

# Resize image
resized_image = resize_image(grayscale_image, 100, 100)

```

