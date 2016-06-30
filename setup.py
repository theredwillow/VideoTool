from setuptools import setup, find_packages

setup(
    name='VideoTool',
    description='A handy tool for watching videos from the internet.',
    version='0.1dev',
    packages=find_packages(),
    long_description=open('README.md').read(),
    install_requires=["requests", "os", "bs4", "selenium", "xml", "random"]
)
