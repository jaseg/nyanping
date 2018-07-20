#!/usr/bin/env python3

from setuptools import setup, find_packages
setup(
    name = 'nyanping',
    version = '0.0.3',
    py_modules = ['ping'],
    scripts = ['nyanping'],
    description = ('Improved graphical ping tool'),
    url = 'https://github.com/jaseg/nyanping',
    author = 'jaseg',
    author_email = 'github@jaseg.net',
    install_requires = ['python-mpv'],
    license = 'GPLv3',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Manufacturing',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Religion',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Topic :: Utilities'
        ]
)
