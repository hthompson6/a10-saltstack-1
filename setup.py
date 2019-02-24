
from setuptools import setup
setup(name='a10_saltstack',
      version='0.0.1',
      description='SaltStack support for A10 AXAPI',
      url='http://github.com/a10networks/a10-saltstack',
      author='A10 Networks',
      author_email='hthompson@a10networks.com',
      license='MIT',
      packages=['a10_saltstack'],
      zip_safe=False,
      # Install scripts for calling this easily.
      # Need to figure out an easy way of making this a script.
     )
