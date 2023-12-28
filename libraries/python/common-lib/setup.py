from setuptools import setup, find_packages

setup(
    name='common-lib',
    version='0.1.0',
    description='Common logic utilized in several services and applications',
    author='MGTheTrain',
    author_email='mgthetrain@email.com',
    packages=find_packages(),
    install_requires=[
        'pydantic',
    ],
)