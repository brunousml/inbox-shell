#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    # TODO: put package requirements here
]

test_requirements = [
    'nose',
    'coverage'
]

setup(
    name='penne_shell',
    version='0.1.0',
    description="Python Boilerplate contains all the boilerplate you need to create a Python package.",
    long_description=readme + '\n\n' + history,
    author="Fabio Batalha",
    author_email='fabio.batalha@scielo.org',
    url='https://github.com/fabiobatalha/penne_shell',
    packages=[
        'penne_shell',
    ],
    package_dir={
        'penne_shell': 'penne_shell'
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='penne_shell',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=["nose>=1.0", "coverage"],
    entry_points={
        'console_scripts': [
            'penne_monitor=penne_shell.cli:main'
        ]
    }
)
