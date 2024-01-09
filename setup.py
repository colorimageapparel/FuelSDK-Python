from setuptools import setup

with open("README.md") as f:
    readme = f.read()

setup(
    version="2.0.5",
    name="Salesforce-FuelSDK",
    description="Salesforce Marketing Cloud Fuel SDK for Python",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Alo",
    py_modules=["ET_Client"],
    packages=["FuelSDK"],
    url="https://github.com/colorimageapparel/FuelSDK-Python",
    license="MIT",
    install_requires=[
        "pyjwt>=2.7.0",
        "requests>=2.31.0",
        "suds-community>=1.1.2",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
        "Programming Language :: Python :: 3.11",
    ],
)
