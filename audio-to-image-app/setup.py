from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="dream-synthesizer",
    version="0.1.0",
    author="Dream Synthesizer Team",
    author_email="author@example.com",
    description="An application that transforms spoken dream narrations into images",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/sandman",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "streamlit>=1.33.0",
        "groq>=0.11.0",
        "python-dotenv>=1.0.1",
        "requests>=2.31.0",
        "pydub>=0.25.1",
        "mistralai>=1.0.1",
        "Pillow>=10.2.0",
        "audio-recorder-streamlit>=0.0.10",
    ],
    entry_points={
        "console_scripts": [
            "dream-synthesizer=src.app:main",
            "dream-cleanup=scripts.cleanup:main",
        ],
    },
)
