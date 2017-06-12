from setuptools import setup

setup(
    name='re2',
    version='1.0',
    description='RE2 Custom Library',
    packages=['re2'],
    data_files=[('lib\\site-packages\\',["re2/re2.dll", "re2/re2.pyd"])],
    include_package_data=True,
)