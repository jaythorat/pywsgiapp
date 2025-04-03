from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pywsgiapp",
    version="0.0.4",
    description="Bring Your Code to the Web with Ease using a Lightweight WSGI Application.",
    long_description=long_description, 
    long_description_content_type="text/markdown",  
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