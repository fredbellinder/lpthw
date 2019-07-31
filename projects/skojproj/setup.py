try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'A first skeleton project',
    'author': 'Fred Bellinder',
    'url': 'URL to deployed project',
    'download_url': 'link',
    'author_email': 'fred.goteborg@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['Skojproj'],
    'scripts': ['./bin/example_fredd414'],
    'py_modules': ['mikumorkis'],
    'name': 'Skojproj',
}

setup(**config)
