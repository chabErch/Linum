from os import path

from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md")) as f:
    long_description = f.read()

setup(
    name='Linum',
    version='0.1',
    packages=find_packages(exclude=["tests", "examples"]),
    package_data={"": ["*.yaml"]},
    url='https://github.com/chabErch/Linum',
    license='MIT',
    author='chaberch',
    author_email='chaberch@yandex.ru',
    description='The tool for tasks visualization — like Gantt chart, but compact.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    entry_points={
        'console_scripts': [
            'linum = linum.cli:cli',
        ],
    }
)
