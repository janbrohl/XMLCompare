#!/usr/bin/env python

from distutils.core import setup
import xmlcompare

setup(name="XMLCompare",
      version=xmlcompare.__version__,
      description="XMLCompare checks XML documents/elements for semantic equality",
      author="Jan Brohl",
      author_email="janbrohl@t-online.de",
      url="https://github.com/janbrohl/xmlcompare",
      py_modules=[
          'xmlcompare'
      ],
      classifiers=[
          "Intended Audience :: Developers",
          "License :: OSI Approved :: BSD License",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.2",
          "Programming Language :: Python :: 3.3",
          "Programming Language :: Python :: 3.4",
          "Programming Language :: Python :: 3.5",
      ]
      )
