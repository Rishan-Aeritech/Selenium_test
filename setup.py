from setuptools import setup, find_packages

setup(
    name="testproj",
    version="1.1.0",  # Set dynamically if possible
    description="A powerful web automation and testing framework",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Dynamic Author",  # Replace if not dynamic
    project_urls={
    },
    packages=find_packages(include=[
        "seleniumbase",
        "sbase",
        "seleniumbase.behave",
        "seleniumbase.common",
        "seleniumbase.config",
        "seleniumbase.console_scripts",
        "seleniumbase.core",
        "seleniumbase.drivers",
        "seleniumbase.extensions",
        "seleniumbase.fixtures",
        "seleniumbase.js_code",
        "seleniumbase.masterqa",
        "seleniumbase.plugins",
        "seleniumbase.resources",
        "seleniumbase.translate",
        "seleniumbase.undetected",
        "seleniumbase.undetected.cdp_driver",
        "seleniumbase.utilities",
        "seleniumbase.utilities.selenium_grid",
        "seleniumbase.utilities.selenium_ide",
    ]),
    include_package_data=True,
    install_requires=[
        "setuptools>=70.2.0",
        "wheel>=0.44.0",
        'pytest==8.3.4',
        "pytest-html==4.0.2",
        'pytest-metadata==3.1.1',
        "pytest-ordering==0.6",
        'pytest-rerunfailures==15.0',
        'pytest-xdist==3.6.1',
    ],
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
    },
    extras_require={
        # Define optional dependencies here
        # Example:
        # "dev": ["pytest", "flake8"],
    },
    keywords=[
        "automation",
        "testing",
        "selenium",
        "pytest",
        # Add other keywords
    ],
    test_suite="pytest",
)

# pip install -e . --use-pep517 --config-settings="editable_mode=compat"