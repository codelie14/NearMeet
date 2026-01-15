"""Setup configuration for NearMeet"""

from setuptools import setup, find_packages
from pathlib import Path

# Read the README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="nearmeet",
    version="1.0.0",
    author="IndraLabs",
    author_email="contact@indralabs.ai",
    description="A local network communication application with chat, video, and file sharing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/NearMeet",
    project_urls={
        "Bug Tracker": "https://github.com/yourusername/NearMeet/issues",
        "Documentation": "https://github.com/yourusername/NearMeet/docs",
        "Source Code": "https://github.com/yourusername/NearMeet",
    },
    packages=find_packages(exclude=["tests", "docs", "assets"]),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Communications :: Chat",
        "Topic :: Multimedia :: Video",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",
    install_requires=[
        "PyQt6>=6.7.0",
        "pyaudio>=0.2.13",
        "sounddevice>=0.4.6",
        "numpy>=1.24.3",
        "opencv-python>=4.8.1.78",
        "mss>=9.0.1",
        "Pillow>=10.1.0",
        "cryptography>=41.0.7",
        "PyNaCl>=1.5.0",
        "plyer>=2.1.0",
        "python-dotenv>=1.0.0",
        "requests>=2.31.0",
        "pydantic>=2.5.0",
        "colorlog>=6.8.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.3",
            "pytest-cov>=4.1.0",
            "pytest-asyncio>=0.21.1",
            "black>=23.12.0",
            "flake8>=6.1.0",
            "isort>=5.13.2",
            "mypy>=1.7.1",
            "sphinx>=7.2.6",
            "sphinx-rtd-theme>=2.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "nearmeet=src.__main__:main",
        ],
    },
    include_package_data=True,
    keywords=[
        "chat",
        "video",
        "local-network",
        "communication",
        "file-sharing",
        "lan",
    ],
    zip_safe=False,
)
