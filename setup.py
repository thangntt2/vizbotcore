
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='vizbot core',
    version='0.1.0',
    description='NLP core engine for Vizbot',
    long_description=readme,
    author='Thangntt',
    author_email='thangntt@hotmail.com',
    url='https://github.com/thangntt2/vizbotcore.git',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
