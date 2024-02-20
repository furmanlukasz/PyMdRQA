from setuptools import setup, find_packages

setup(
    name='PyMdRQA',
    version='0.1.0',
    author='Łukasz Furman',
    author_email='cracer.net@gmail.com',
    packages=find_packages(),
    description='A Python implementation of Multidimensional Recurrence Quantification Analysis (MdRQA).',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        'numpy',
        'scipy',
        'pyrqa',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
