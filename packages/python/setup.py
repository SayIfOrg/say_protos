from setuptools import setup, find_packages

__version__ = "0.1.0"

setup(
    name="sayif_protos",
    version=__version__,
    url="https://github.com/SayIfOrg/say_protos",
    author="Amir Khalife",
    author_email="eng.amir.bu@gmail.com",
    py_modules=find_packages(),
    install_requires=[
        "grpcio>=1.50,<1.51",
        "grpcio-tools>=1.50,<1.51"
    ],
)
