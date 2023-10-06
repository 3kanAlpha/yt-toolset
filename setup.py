from setuptools import setup

setup(
    name='yt-toolset',
    version='0.0.1',
    entry_points={
        'console_scripts': [
            'ytool = tool:parse'
        ]
    }
)