from os import path
from setuptools import setup

with open(path.join(path.dirname(path.abspath(__file__)), 'README.rst')) as f:
    readme = f.read()

setup(
    name             = 'watermark',
    version          = '0.1',
    description      = 'Add watermark to images',
    long_description = readme,
    author           = 'Adithya Krishna, Yati Padia',
    author_email     = 'adikrish@redhat.com, ypadia@redhat.com',
    url              = 'http://wiki',
    packages         = ['watermark'],
    install_requires = ['chrisapp'],
    test_suite       = 'nose.collector',
    tests_require    = ['nose'],
    license          = 'MIT',
    zip_safe         = False,
    python_requires  = '>=3.6',
    entry_points     = {
        'console_scripts': [
            'watermark = watermark.__main__:main'
            ]
        }
)
