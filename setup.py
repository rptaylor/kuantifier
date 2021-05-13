#!/usr/bin/env python3

from setuptools import setup, find_packages
from os import environ

setup(
    name='kapel',
    version='0.6',
    packages=['kapel'],
#    packages=find_packages(),
    install_requires=[
        'environs',			# for handling configuration
        'dirq',				# for sending messages
        'prometheus-api-client'		# for querying Prometheus
    ],
    entry_points={
        'console_scripts': [
            'kapel = kapel:main',
        ],
    },
)
