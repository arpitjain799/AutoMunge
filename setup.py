import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Automunge",
    version="8.32",
    author="Nicholas Teague",
    author_email="pitg888@gmail.com",
    description="platform for preparing tabular data for machine learning",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Automunge/AutoMunge",
    packages=setuptools.find_packages(),
    install_requires=['numpy', 'pandas', 'scikit-learn', 'scipy'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
)

