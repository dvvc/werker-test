from setuptools import setup, find_packages

from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(

    name='werckertest',

    version='0.0.1',

    description='Testing wercker and python packages',
    long_description=long_description,

    url='https://github.com/dvvc/werker-test',

    author='David Villegas',
    author_email='dville00@gmail.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3.4',
    ],

    keywords='sample packaging wercker',

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    install_requires=[],

    extras_require={
        'dev': [],
        'test': ['coverage'],
    },

    #data_files=[(
    entry_points={
        'console_scripts': [
            'wercker-test=wercktest:main',
        ],
    },
)
