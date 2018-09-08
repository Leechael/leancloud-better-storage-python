import setuptools
from setuptools import find_packages

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

packages = find_packages(exclude=('tests',))

setuptools.setup(
    name="better-leancloud-storage",
    version="0.0.1",
    author="weak_ptr",
    author_email="weak_ptr@outlook.com",
    description="better ORM wrapper of leancloud storage python sdk.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nnnewb/better-leancloud-storage-python",
    packages=packages,
    install_requires=['leancloud==2.1.8', ],
    license='LGPL',
    classifiers=[
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Operating System :: OS Independent",
    ],
)
