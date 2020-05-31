#!/usr/bin/env python
from setuptools import setup, find_packages


def find_requirements(fn):
    lines = []
    with open(fn) as f:
        for line in f:
            line = line.strip()
            if not line.startswith('#'):
                lines.append(line)
    return lines


setup(
    name='docker-make',
    description='build,tag,and push a bunch of related docker images via a single command',
    version='2.0.0',
    author='jizhilong',
    author_email='zhilongji@gmail.com',
    url='https://github.com/CtripCloud/docker-make',
    license='Apache',
    keywords=['docker', 'image', ' build'],
    packages=find_packages(exclude=['tests']),
    entry_points={
        'console_scripts': [
            'docker-make = dmake.cli:main'
        ]
    },
    install_requires=find_requirements('requirements.txt'),
    tests_require=find_requirements('test-requirements.txt'),
    test_suite='nose.collector',
    classifiers=[],
    )
