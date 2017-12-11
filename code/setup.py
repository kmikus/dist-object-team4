# Project: Team 4 Distributed System Project
# Purpose Details: Demonstrate full cycle distributed system using json payloads and various python libraries/frameworks
# Course: IST411
# Authors: Kevin Mikus, Ian Roach, Dustin Dimarcello, Eugene Matavitski
# Date Developed: 2017-11-10
# Last Date Changed: 2017-12-09
# Rev: 1.0.0

"""
Setup for dist-object-team4 system to be used with pip3
"""

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Long description is obtained from README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    # General description
    name = 'IST411-Team4-Mikus',
    version = '1.0.0',
    description = 'A distributed system communication demonstration using JSON and various Python tools',
    long_description = long_description,

    # Main homepage
    url = 'https://github.com/kmikus/dist-object-team4',

    # Author details
    author = 'Kevin Mikus',
    author_email = 'kzm5599@psu.edu',

    # Generic license
    license = 'Other/Proprietary License',

    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Students',
        'Topic :: Software Development :: Education',
        'License :: Other/Proprietary License',
        'Programming Language :: Python :: 3'
],

    keywords = 'json python distributed cURL sftp rabbitmq socket smtp Pyro4 aes ssl hmac crc compression',

    # Packages and dependencies
    packages=['dist-object-team4'],
    install_requires = ['pika', 'pycrypto', 'pysftp', 'Pyro4', 'pymongo'],
    python_requires = '>=3',
    # extras_requires = {},
    # package_data = {},
    # data_files = [],
    # entry_points = {},
)
