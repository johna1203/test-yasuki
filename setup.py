from setuptools import setup

setup(
    name="yasuki",
    packages=['yasuki'],
    entry_points={
        'console_scripts': ['yasuki=yasuki.start:main'],
    }
)
