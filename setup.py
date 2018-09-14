from setuptools import setup

setup(
    name='flask-template-app',
    packages=['ftapp'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask_restful'
    ],
)
