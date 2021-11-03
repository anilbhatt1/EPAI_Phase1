import sys

import importer

module1 = importer.import_('module1', 'module1_source.py', '.')

import module2

module2.hello()