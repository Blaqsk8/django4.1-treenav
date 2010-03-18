import os
from setuptools import setup, find_packages

setup(
    name='django-treenav',
    version='0.0.0',
    author='Caktus Consulting Group',
    author_email='solutions@caktusgroup.com',
    packages=find_packages(),
    install_requires = ['Django >= 1.1,==dev',],
    include_package_data = True,
    exclude_package_data={
        '': ['*.sql', '*.pyc',],
        'treenav': ['media/*',]
    },
    url='http://code.google.com/p/django-treenav/',
    license='LICENSE.txt',
    description='Extensible, hierarchical, and pluggable navigation system for Django sites.',
    long_description=open('README.txt').read(),
)
