from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='draftbot',
    version='0.0.1',
    description='Algorithmic Drafting for Magic the Gathering',
    long_description=long_description,
    url='https://github.com/madrury/mtg-draftbot',
    author='Matthew Drury',
    author_email='matthew.drury.83@gmail.com',
    license='BSD',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Mathematics'
    ],
    packages=['draftbot'],
    install_requires=['numpy', 'pandas', 'torch'],
)
