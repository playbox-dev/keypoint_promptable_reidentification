import numpy as np
import os.path as osp
from setuptools import setup, find_packages
from distutils.extension import Extension
from Cython.Build import cythonize

def readme():
    with open('README.md') as f:
        content = f.read()
    return content


def find_version():
    version_file = 'torchreid/__init__.py'
    with open(version_file, 'r') as f:
        exec(compile(f.read(), version_file, 'exec'))
    return locals()['__version__']


def numpy_include():
    try:
        numpy_include = np.get_include()
    except AttributeError:
        numpy_include = np.get_numpy_include()
    return numpy_include


ext_modules = []


def get_requirements(filename='requirements.txt'):
    here = osp.dirname(osp.realpath(__file__))
    with open(osp.join(here, filename), 'r') as f:
        requires = [line.replace('\n', '') for line in f.readlines()]
    return requires


setup(
    description='A library for deep learning person re-ID in PyTorch',
    license='MIT',
    long_description=readme(),
    packages=find_packages(),
    install_requires=get_requirements(),
    keywords=['Person Re-Identification', 'Deep Learning', 'Computer Vision'],
    ext_modules=cythonize(ext_modules)
)
