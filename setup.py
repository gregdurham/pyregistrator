# -*- coding: utf-8 -*-

import re
from setuptools import setup

requires = [
    'PyYAML==3.11',
    'docopt==0.6.1',
    'pykwalify==14.08',
    'python-etcd==0.3.2'
]

setup(
    name = "pyregistrator",
    long_description=(
        '%s\n\n%s' % (
            open('README.md').read(),
            open('CHANGELOG.md').read()
        )
    ),
    package_dir={'pyregistrator': 'src'},
    packages=["pyregistrator", 
              "pyregistrator.backends",
              "pyregistrator.config",
              "pyregistrator.lib"],
    scripts=["src/bin/pyregistrator"],
    version=open('VERSION').read().strip(),
    description = "Python docker registration service for etcd.",
    author = "Gregory Durham",
    author_email = "gregory.durham@gmail.com",
    include_package_data=True,
    install_requires=requires
    )
