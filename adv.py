from setuptools import setup, Extension

module = Extension('hrll', sources=['encrypted.py'])

setup(
    name='Hrll cryptocode',
    version='1.0',
    description='ruh',
    ext_modules=[module]
)
