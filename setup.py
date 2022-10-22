import os
import setuptools

setuptools.setup(
    name=os.getenv('PACKAGE_NAME'),
    version=os.getenv('PACKAGE_VERSION'),
    author="ShomyApp",
    description=os.getenv('PACKAGE_VERSION'),
    packages=setuptools.find_packages(),
    python_requires='>=3.7',
)
