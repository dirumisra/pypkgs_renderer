from ensurepip import version
from importlib.metadata import packages_distributions
from pytz import VERSION
import setuptools
with open("README.md","r",encoding= "utf-8") as f:
    long_descripiton = f.read()
    
__version__ = "0.0.0"

REPO_NAME = "pypkg"
AUTHOR_USER_NAME = "dirumisra"
AUTHOR_EMAIL = "DHIRAJK266@GMAIL.COM"
SRC_REPO = "pypkg"

setuptools.setup(
    
    name= SRC_REPO,
    author= AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    version= __version__,
    description= "A Small python package",
    long_description = long_descripiton,
    long_descripiton_content = "text/markdown",
    url= f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
        },
    package_dir = {"":"src"},
    packages_ = setuptools.find_packages(where='src')
    )
    
