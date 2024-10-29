from setuptools import setup, find_packages
setup(
    name="image_package",
    version="0.0.1",
    author="LucRodrik",
    author_email="lucianf3d@gmail.com",
    description="A basic image processing package with scikit-image",
    long_description=open('README.md').read().
    long_description_content_type="text/markdown",
    url="https://github.com/LucRodrik/image_package"
    packages=find_packages(),
    install_requires=[
        'scikit-image'
    ],
    python_requires='>=3.6',
)