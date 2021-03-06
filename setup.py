#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ----------------------------------------------------------------------------
# Copyright (c) 2011-2013, The BIOM Format Development Team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
# ----------------------------------------------------------------------------

import os
from setuptools import setup
from setuptools.extension import Extension
from glob import glob

import numpy as np

__author__ = "Daniel McDonald"
__copyright__ = "Copyright 2011-2013, The BIOM Format Development Team"
__credits__ = ["Greg Caporaso", "Daniel McDonald", "Jose Clemente",
               "Jai Ram Rideout", "Jorge Cañardo Alastuey"]
__license__ = "BSD"
__version__ = "1.3.1-dev"
__maintainer__ = "Daniel McDonald"
__email__ = "mcdonadt@colorado.edu"

long_description = """BIOM: Biological Observation Matrix
http://www.biom-format.org

The Biological Observation Matrix (BIOM) format or: how I learned to stop
worrying and love the ome-ome
Daniel McDonald, Jose C Clemente, Justin Kuczynski, Jai Ram Rideout,
Jesse Stombaugh, Doug Wendel, Andreas Wilke, Susan Huse, John Hufnagle,
Folker Meyer, Rob Knight, J Gregory Caporaso
GigaScience 2012, 1:7.
"""

classes = """
    Development Status :: 4 - Beta
    License :: OSI Approved :: BSD License
    Topic :: Scientific/Engineering :: Bio-Informatics
    Topic :: Software Development :: Libraries :: Application Frameworks
    Topic :: Software Development :: Libraries :: Python Modules
    Programming Language :: Python
    Programming Language :: Python :: 2.7
    Programming Language :: Python :: Implementation :: CPython
    Operating System :: OS Independent
    Operating System :: POSIX :: Linux
    Operating System :: MacOS :: MacOS X
"""
classifiers = [s.strip() for s in classes.split('\n') if s]

# Dealing with Cython
USE_CYTHON = os.environ.get('USE_CYTHON', False)
ext = '.pyx' if USE_CYTHON else '.c'
extensions = [Extension("biom._filter",
                        ["biom/_filter" + ext]),
              Extension("biom._transform",
                        ["biom/_transform" + ext])]

if USE_CYTHON:
    from Cython.Build import cythonize
    extensions = cythonize(extensions)

setup(name='biom-format',
      version=__version__,
      description='Biological Observation Matrix (BIOM) format',
      long_description=long_description,
      license=__license__,
      author=__maintainer__,
      author_email=__email__,
      maintainer=__maintainer__,
      maintainer_email=__email__,
      url='http://www.biom-format.org',
      packages=['biom',
                'biom/commands',
                'biom/interfaces',
                'biom/interfaces/optparse',
                'biom/interfaces/optparse/config',
                'biom/interfaces/html',
                'biom/interfaces/html/config'
                ],
      ext_modules=extensions,
      include_dirs=[np.get_include()],
      scripts=glob('scripts/*'),
      install_requires=["numpy >= 1.3.0",
                        "pyqi == 0.3.1",
                        "scipy >= 0.13.0"],
      extras_require={'test': ["nose >= 0.10.1",
                               "tox >= 1.6.1"],
                      'hdf5': ["h5py >= 2.2.0"]
                      },
      dependency_links=[
          'https://github.com/bipy/pyqi/archive/master.zip#egg=pyqi-0.3.1-dev'
      ],
      classifiers=classifiers
      )
