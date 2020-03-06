from setuptools import setup, find_packages

PACKAGE_NAME = 'Demo'
PACKAGE_VERSION = '0.1'
INSTALL_REQUIRES = [
    'selene==2.0.0a21',
    'pytest-bdd',
    'pyhamcrest',
    'addict',
    'pytest-xdist',
    'allure-pytest-bdd'
]
setup(
    name=PACKAGE_NAME,
    version=PACKAGE_VERSION,
    description=('Demo Test Project for pytest-bdd',),
    packages=find_packages(),
    install_requires=INSTALL_REQUIRES
)
