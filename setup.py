# Robin Kalia
# robinkalia@berkeley.edu
# UC Berkeley
#
# Info 290T: Agile Engineering Practices - Final Project on Travis

#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='Travis Demo',
      version='0.1',
      description='Travis Django app - "Survey" demo.',
      author='Robin Kalia',
      author_email='robinkalia@berkeley.edu',
      url='https://github.com/robinkalia/aep_final_project_travis.git',
      packages=find_packages(),
      license='License :: Public Domain',
        
      # Enable django-setuptest
      test_suite='setuptest.setuptest.SetupTestSuite',
      tests_require=(
        'django-setuptest',
        # Required by django-setuptools on Python 2.6
        'argparse'
      ),
)
