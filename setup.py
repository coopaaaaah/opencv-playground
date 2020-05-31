from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='opencv-playground-david',
    version='0.0.1',
    description='A Playground for Learning OPEN CV',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/coopaaaaah/opencv-playground',
    author='David Cooper',
    packages=find_packages(where='src'),
    python_requires='>=3.6',
)
