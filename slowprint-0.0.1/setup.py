from setuptools import setup


def readme():
    with open("README.md") as f:
        return f.read()


setup(
    name="slowprint",
    version="0.0.1",
    description="to print slow",
    long_description=readme(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
    url="https://github.com/dead-zone-termux",
    author="kanish",
    author_email="kanish.ravikumar@gmail.com",
    keywords="core",
    license="MIT",
    packages=["slowprint"],
    install_requires=[],
    include_package_data=True,
    zip_safe=False,
)