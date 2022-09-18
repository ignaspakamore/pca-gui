from setuptools import setup

setup(
    name='pca-gui',
    version='1.0',
    author='Ignas Pakamore',
    description='Graphical user interface to visualise principle component analysis',
    maintainer='Ignas Pakamore',
    url='https://github.com/ignaspakamore/pca-gui',
    python_requires='>=3.7, <4',
    license='MIT',
    keywords=['PCA', 'principle component analysis'],
    install_requires=[
       'pandas', 
       'numpy', 
       'PySimpleGUI', 
       'sklearn', 
       'matplotlib', 
    ],
)