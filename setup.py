from setuptools import setup, findpackages
import os
import codecs

setup(
    name='osbnr',
    version='0.1',
    description='One Side Behavioral Noise Reduction algorithm implementation',
    author='Salma EL HAJJAMI',
    author_email='s.elhajjami@uiz.ac.ma',
    packages=['osbnr'],
    install_requires=['scikit-learn', 'numpy'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
    ],
)
