from setuptools import setup
from codecs import open  # To use a consistent encoding
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='celery-message-consumer',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='1.0.2',

    description='Tool for using the bin/celery worker to consume vanilla AMQP messages (i.e. not Celery tasks)',
    long_description=long_description,

    url='https://github.com/depop/celery-message-consumer',

    author='Depop',
    author_email='dev@depop.com',

    license='Apache 2.0',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Celery',
    ],
    install_requires=[
        'configloader[attrdict,yaml]>=1.0.1,<1.1',
        'wrapt>=1.10,<2.0',
        'typing>=3.6.2,<4.0',
        'six',
    ],

    packages=[
        'event_consumer',
        'event_consumer.conf',
        'event_consumer.test_utils',
    ],
)