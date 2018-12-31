'''
Created on 31 déc. 2018

@author: rachid
'''
from setuptools import setup

setup(
    name="HelloWorld",
    version='1.0',
    py_modules=['hello'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        hello=hello:cli
    ''',
)