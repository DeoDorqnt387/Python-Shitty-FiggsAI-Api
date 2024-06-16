	
from setuptools import setup, find_packages

	
VERSION = "0.0.7"

	
def desc():
    with open("README.md", encoding="utf-8") as f:
        desc = f.read()
        return desc

setup(
    name='figgs-ai',
    version=VERSION,
    packages=find_packages(),
    include_package_data=True,
    long_description_content_type='text/markdown',
    author='Pandora',
    author_email='yigitcankocabiyik@gmail.com',
    url="https://github.com/DeoDorqnt387/Unofficial-the-worst-figgs.ai-API.git",
    description='a simple figgs.ai api',
    long_description=desc(),
    install_requires=[
        'requests',
        'beautifulsoup4',
        'urllib3'
    ],
    keywords=['figgs', 'figgs.ai', 'figgsai api', 'figgs ai'],
)