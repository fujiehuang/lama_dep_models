from setuptools import setup, find_packages

setup(
    name='models',
    version='0.1.0',
    packages=find_packages(include=['models', 'models.*']),
    include_package_data=True
)