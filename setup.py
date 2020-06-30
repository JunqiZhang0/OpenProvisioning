import os
import re
import ast
"""
This is the ccit desgned open provisioning RESTful APIs, you could use this to provision your infrastructure
"""
from setuptools import setup, find_packages
packages_required = []
with open("requirements.txt", "r") as f:
    for line in f:
        packages_required.append(line[:-1])

version = "0.0.0.0"

with open ('openprov/version.py') as f:
    for line in f:
        version = ast.parse(line).body[0].value.s

setup(
    name='openprov',
    version=version,
    license='GPLv3',
    author='ccit',
    author_email="junqzhan@redhat.com",
    url="https://github.com/JunqiZhang0/OpenProvisioning",
    description='Open Provisioning RESTful API',
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=packages_required,

    classifiers=[
        'Development Status :: 1 - Planning'
    ],
    entry_points={
        'console_scripts': ['openprov=openprov.manage:main']
    }
)
