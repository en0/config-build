#!/usr/bin/env python2

from setuptools import setup

setup(
    name="config-build",
    version="1.0",
    packages=['config_build'],
    description="Create configuration object from ini file.",
    author="Ian Laird",
    author_email="en0@mail.com",
    url="https://github.com/en0/config-build/",
    install_requires=['jinja2'],
    package_data={'': ['template']},
    entry_points={
        'console_scripts': [
            'config-build = config_build.__main__:main',
        ]
    }
)
