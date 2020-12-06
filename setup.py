"""findTarget"""
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

install_requires = ['setuptools>=18.0', 'biopython']

setup(
    name='findTarget',
    version='0.0.1',
    description='pipeline for searching phi29 homologs',
    author='Trituration',
    url='http://github.com/ubercomrade/Trituration',
    scripts=['findTarget.py',],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Unix",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        'Programming Language :: Cython',
        "Topic :: Scientific/Engineering :: Bio-Informatics"
    ],
    zip_safe=False,
    install_requires=install_requires,
    setup_requires=install_requires,
    python_requires='>=3.7',
)