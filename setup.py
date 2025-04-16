from os.path import dirname, join

import setuptools


def readme() -> str:
    """Utility function to read the README file.
    Used for the long_description.  It's nice, because now 1) we have a top
    level README file and 2) it's easier to type in the README file than to put
    a raw string in below.
    :return: content of README.md
    """
    return open(join(dirname(__file__), "README.md")).read()


setuptools.setup(
    name="streamlit-drawable-canvas-fix",
    version="0.9.6",
    author="Andreas Bauer",
    author_email="Andreas.Bauer2@gmx.net",
    description="Fix of orignal streamlit-drawable-canvas for new streamlit versions.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/AndreasBauerGit/streamlit-drawable-canvas-fix",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.6",
    install_requires=[
        "Pillow",
        "numpy",
        "streamlit >= 1.40.0",
    ],
)
