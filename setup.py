import os
import os.path
import codecs

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def read_me():
    with codecs.open(os.path.join(os.path.dirname(__file__), 'README.rst')) as f:
        return f.read()


def get_version():
    with codecs.open(os.path.join(os.path.dirname(__file__), 'VERSION')) as f:
        return f.read()


setup(
    name='NaverShoppingParser',
    packages=['shopping_parser'],
    data_files=[('', ['README.rst'])],
    version=get_version(),
    description='Naver shopping parser',
    long_description=read_me(),
    license='MIT License',
    author='Jaeyoung Lee',
    author_email='jaeyoung@monodiary.net',
    maintainer='Jaeyoung Lee',
    maintainer_email='jaeyoung@monodiary.net',
    url='https://github.com/jeyraof/naver-shopping-parser',
    tests_require=[
        'pytest >= 2.3.0',
    ],
)