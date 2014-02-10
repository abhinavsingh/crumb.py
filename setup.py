from setuptools import setup
import crumb

classifiers = [
    'Development Status :: 4 - Beta',
    'Environment :: Web Environment',
    'Intended Audience :: Developers',
    'Intended Audience :: System Administrators',
    'License :: OSI Approved :: BSD License',
    'Operating System :: MacOS',
    'Operating System :: POSIX',
    'Operating System :: Unix',
    'Operating System :: Microsoft',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 2.7',
    'Topic :: Internet :: Proxy Servers',
    'Topic :: Internet :: WWW/HTTP :: HTTP Servers',
]

setup(
    name                = 'crumb.py',
    version             = crumb.__version__,
    description         = crumb.__description__,
    long_description    = open('README.md').read().strip(),
    author              = crumb.__author__,
    author_email        = crumb.__author_email__,
    url                 = crumb.__homepage__,
    license             = crumb.__license__,
    py_modules          = ['crumb'],
    install_requires    = [],
    classifiers         = classifiers
)
