from setuptools import setup

setup(
    name='snapshotalyzer-30000',
    version='0.1',
    author='Brent Slater',
    author_email='brentslater@gmail.com',
    description='SnapshotAlyzer 30000 is a too; to manage AWS EC2 Snapshots',
    license='GPLv3+',
    packages=['shotty'],
    url='https://github.com/brentslater/snapshotalyzer-30000',
    install_reqiures=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
    ''',
)
