import setuptools

setuptools.setup(
    name="pynemaiqpet",
    use_scm_version={'fallback_version':'unkown'},
    setup_requires=['setuptools_scm','setuptools_scm_git_archive'],
    author="Georg Schramm",
    author_email="georg.schramm@kuleuven.be",
    description="Analysis of PET NEMA IQ phantom scans"
    license='MIT',
    long_description_content_type="text/markdown",
    url="https://github.com/gschramm/pynemaiqpet",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['pymirc @ https://github.com/gschramm/pymirc/archive/v0.19.zip',
                      'nibabel>=3.0',
                      'matplotlib>=3.1',
                      'pydicom>=2.0',
                      'scipyi>=2.14',
                      'pandas>=1.0',
                      'lmfiti>=1.0'],
    include_package_data=True,
)
