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
    'install_requires': ['nose'],  # this will check pypi
    # this will install local packages, NAMED folders with __init__.py initially.
    'packages': ['NAME'],
    # if you only need part of a package: py_modules = ['mod1', 'pkg.mod2']
    'py_modules': ['bin/'],
    'name': 'NAME',
}

setup(**config)

# how to add a script:
# https://docs.python.org/3/distutils/introduction.html#distutils-simple-example

# more imports and the adding of libs and such:
# https://docs.python.org/3/distutils/setupscript.html?highlight=module#installing-package-data
