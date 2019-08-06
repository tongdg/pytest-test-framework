"""Minimal setup file for tasks project."""

from setuptools import setup, find_packages

setup(
    name='ykb',
    version='0.1.0',
    license='proprietary',
    description='Ykb Project',

    author='tongdg',
    author_email='892431872@qq.com',
    url='',

    packages=find_packages(where='src'),
    package_dir={'': 'src'},
)
