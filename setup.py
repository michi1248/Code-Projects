from setuptools import setup,find_packages


setup(
    name='Code-Projects',
    version='1.0.0',
    packages=find_packages(),
    author='Michael März',
    description='Some programming projects I have been working on',
    install_requires = ['numpy','turtles'],
    url='https://github.com/michi1248/Code-Projects',
    options={"bdist_wheel": {"python_tag": "py3"}},
)