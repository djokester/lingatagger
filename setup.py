#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: djokester
Samriddhi Sinha,
IIT Kharagpur
"""

import sys
from setuptools import setup

if sys.argv[-1] == 'setup.py':
    print('To install, run \'python setup.py install\'')
    print()

if sys.version_info[:2] < (3, 5):
    print(('lingatagger requires Python version 3.5 or later (%d.%d detected).' %sys.version_info[:2]))
    sys.exit(-1)

try:                  
    import gensim
except ImportError:
    print('gensim must be installed to use lingatagger')
    sys.exit(-1)

try:                  
    import re
except ImportError:
    print('re must be installed to use lingatagger')
    sys.exit(-1)

try:                  
    import sklearn
except ImportError:
    print('sklearn must be installed to use lingatagger')
    sys.exit(-1)

sys.path.insert(0, 'lingatagger')


if __name__ == "__main__":
    setup(
        name = "lingatagger",
        version = "1.0",
        author = "Samriddhi Sinha",
        author_email = "samridhhisinha.iitkgp@gmail.com",
        description = "A simple gender tagger for Hindi based on an Multi Layer Perceptron Classifier trained with gensim's word2vec. It is backed off by Regex and Lookup Tagger",
        url='https://github.com/djokester/lingatagger',
        keywords= ['nlp', 'hindi', 'linguistics'],
        packages = ['lingatagger'],
        license = 'Apache License',
        install_requires = ['gensim', 'regex', 'sklearn']
    )

