from setuptools import setup, find_packages

setup(
    name="seleniumbase",
    version="0.1.0",  # Set dynamically if possible
    description="A powerful web automation and testing framework",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Dynamic Author",  # Replace if not dynamic
    url="https://github.com/seleniumbase/SeleniumBase",
    project_urls={
        "Homepage": "https://github.com/seleniumbase/SeleniumBase",
        "Changelog": "https://github.com/seleniumbase/SeleniumBase/releases",
        "Download": "https://pypi.org/project/seleniumbase/#files",
        "Blog": "https://seleniumbase.com/",
        "Discord": "https://discord.gg/EdhQTn3EyE",
        "PyPI": "https://pypi.org/project/seleniumbase/",
        "Source": "https://github.com/seleniumbase/SeleniumBase",
        "Repository": "https://github.com/seleniumbase/SeleniumBase",
        "Documentation": "https://seleniumbase.io/",
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
        # Add other required dependencies here
    ],
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "seleniumbase=seleniumbase.cli:main",
            "sbase=seleniumbase.cli:main",
        ],
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
