from setuptools import  find_packages, setup

with open("SSQL/README.md", "r") as file:
    long_desc = file.read()

setup(
    name="ssql",
    version="1.0.0",
    description="A simple library that simplify MySQL actions",
    package_dir={"": "SSQL/src"},
    packages=find_packages(where="SSQL/src"),
    long_description=long_desc,
    long_description_content_type="text/markdown",
    url="https://github.com/BazzoniEdoardo/SSQL",
    author="BazzoniEdoardo",
    author_email="bazzoni.edoardo@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.11"
    ],
    install_requires=["mysql-connector-python >= 9.0.0"],
    extras_require={
        "dev": ["twine >= 5.0.0"]
    },
    python_requires =">=3.10"
)