import os
import setuptools

setuptools.setup(
    name=os.getenv('PACKAGE_NAME'),
    version='0.0.1',
    author="ShomyApp",
    description=os.getenv('PACKAGE_DESCRIPTION'),
    packages=setuptools.find_packages(),
    python_requires='>=3.7',
)
