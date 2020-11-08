from setuptools import setup, find_packages
import textrank

setup(
    name=textrank.__name__,
    version=textrank.__version__,
    url='http://khuhub.khu.ac.kr/2020-2-capstone-design1/HCG_project.git/',
    author=textrank.__author__,
    author_email='2015104194@khu.ac.kr',
    description='YouTube captions summary based TextRank(Keyword and key-sentence extractor)',
    packages=find_packages(),
    #long_description=open('README.md', encoding="utf-8").read(),
    zip_safe=False,
    setup_requires=[]
)