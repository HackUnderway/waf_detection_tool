from setuptools import setup, find_packages

setup(
    name="waf_detection_tool",
    version="1.0.0",
    author="Jey Zeta",
    author_email="info@hackunderway.com",
    description="Herramienta para detectar WAFs en URLs.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/HackUnderway/waf_detection_tool",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "requests",
        "termcolor",
        "emoji"
    ],
    entry_points={
        "console_scripts": [
            "waf_detection_tool=waf_detection_tool:main",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)

