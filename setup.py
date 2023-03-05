from setuptools import find_packages, setup
setup(
    name='sngtolib',
    packages=find_packages(include=['sngtolib']),
    version='0.1.0',
    description='My first Python library',
    author='DavidBisky',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)