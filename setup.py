from setuptools import setup, find_packages

setup(
    name="pywsgiapp",
    version="0.0.1",
    description="A lightweight WSGI application",
    author="Jay Thorat",
    author_email="dev.jaythorat@gmail.com",
    url="https://github.com/jaythorat/pywsgiapp",
    packages=find_packages(include=["pywsgiapp", "pywsgiapp.*"]),
    install_requires=["gunicorn>=23.0.0"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.12",
)