"""License
"""


"""Dependencies
"""
from setuptools import setup
import re
import os


"""Globals
"""
__path__ = os.path.dirname(os.path.realpath(__file__))
__pkg_name__ = ''
__pkg_url__ = 'https://github.com/.../...'
__license__ = 'MIT'
__description__ = ''
__author__ = ''
__email__ = ''

__excludes = [
    'tests',
    'docs',
    '.git',
    '.github'
]


"""Get version
"""
with open(os.path.join(__path__, 'bin', '__init__.py'), 'r') as fd:
    __version__ = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
        fd.read(),
        re.MULTILINE
    ).group(1)


"""Get requirements
"""
__reqs__ = []
with open(
        os.path.join(__path__, 'requirements.txt'), 'r') as fd:
    Lines = fd.readlines()
    for line in Lines:
        __reqs__.append(line.strip())


"""Setup arguments
"""
setup(
    name = __pkg_name__,
    version = __version__,
    description = __description__,
    long_description = open('README.md').read(),
    long_description_content_type='text/markdown',
    author = __author__,
    author_email = __email__,
    url = __pkg_url__,
    packages = ['bin'],
    exclude = __excludes__,
    package_dir = {__pkg_name__: 'bin'},
    license = __license__,
    zip_safe = False,
    install_requires = __reqs__,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Bio-Informatics'
        ]
)
