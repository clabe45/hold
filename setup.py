from setuptools import setup, find_packages

setup(
    name='hold',
    version='0.1',
    description="A simple storage cli",
    packages=find_packages(),
    include_package_data=True,
    install_requires=['click'],
    entry_points='''
        [console_scripts]
        hold=hold.main:cli
    '''
)
