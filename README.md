# Introduction

This is a python package installer which can be used to create an installable binary distribution to install [Facebook's pyre2](https://github.com/facebook/pyre2) module (which uses [Google's re2](https://github.com/google/re2) library) on a Python distribution for fast parsing of complex regular expressions

#### Requirements to build binary distribution

- Built DLL for RE2
- Built pyd and egg-info file for re2

## Building the Binary Distribution

Download the source, and run command `python setup.py sdist --formats=zip,gztar`. This will create a dist folder, with the built binaries present inside, according to the formats specified.
The formats can be changed to any desired ones. Here is the [full list of available formats](https://docs.python.org/2/distutils/sourcedist.html)

## Installing the Binary Distribution

Since a python package has been built, it can be installed by any of the standard methods, like `pip` or `easy_install`. For eg:
`pip install re2-1.0.win-amd64.tar.gz`