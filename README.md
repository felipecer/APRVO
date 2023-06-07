Visualization and Python bindings for Optimal Reciprocal Collision Avoidance
==========================================================

This repository containts the Python Bindings for ORCA developed by Sybren A. Stüvel 
(from [GitHub](https://github.com/sybrenstuvel/Python-RVO2) together with an OpenGL visualization 
of a navigation task.
The building and installing process follows that of https://github.com/sybrenstuvel/Python-RVO2:

Building & installing
----------------------

Building requires [CMake](http://cmake.org/) and [Cython](http://cython.org/) to be installed.
Run `pip install -r requirements.txt` to install the tested version of Cython, or run
`pip install Cython` to install the latest version.

Run `python setup.py build` to build, and `python setup.py install` to install.
Alternatively, if you want an in-place build that puts the compiled library right in
the current directory, run `python setup.py build_ext --inplace`

Only tested with Python 2.7, 3.4, and 3.6 on Ubuntu Linux. The setup.py script uses CMake to build
the RVO2 library itself, before building the Python wrappers. If you have success (or failure)
stories, please share them!

To build on Mac OSX, give an `export MACOSX_DEPLOYMENT_TARGET=10.xx` command first, before
running `python setup.py build`. Replace `10.xx` with your version of OSX, for example `10.11`.

For the visualization, PyOpenGL and PyOpenGL_accelerate are needed. I installed them 
using `pip install PyOpenGL PyOpenGL_accelerate==3.1.6` (versions 3.1.5 and older are not compatible).

To execute the example, use `python example.py`


Optimal Reciprocal Collision Avoidance
======================================

<http://gamma.cs.unc.edu/RVO2/>

[![Build Status](https://travis-ci.org/snape/RVO2.svg?branch=master)](https://travis-ci.org/snape/RVO2)
[![Build status](https://ci.appveyor.com/api/projects/status/0nyp7y4di8x1gh9o/branch/master?svg=true)](https://ci.appveyor.com/project/snape/rvo2)

Copyright 2008 University of North Carolina at Chapel Hill

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

<http://www.apache.org/licenses/LICENSE-2.0>

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Please send all bug reports for the Python wrapper to
[Python-RVO2](https://github.com/sybrenstuvel/Python-RVO2), and bug
report for the RVO2 library itself to [geom@cs.unc.edu](mailto:geom@cs.unc.edu).

The RVO2 authors may be contacted via:

Jur van den Berg, Stephen J. Guy, Jamie Snape, Ming C. Lin, and Dinesh Manocha  
Dept. of Computer Science  
201 S. Columbia St.  
Frederick P. Brooks, Jr. Computer Science Bldg.  
Chapel Hill, N.C. 27599-3175  
United States of America
