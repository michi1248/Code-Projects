from setuptools import find_packages
from distutils.core import setup


setup(
    name='snowflake',
    version='0.1',
    #py_modules=['snowflake'],
    packages=find_packages(),
    #scripts='let_it_snow-py',
    author='Michael März',
    description='Some programming projects I have been working on',
    install_requires = ['numpy','turtles'],
    url='https://github.com/michi1248/Code-Projects',
    #options={"bdist_wheel": {"python_tag": "py3"}},
)