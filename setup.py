from setuptools import setup

setup(
    name='BFScratch',
    version='0.0.5',
    packages = ['BFScratch'],
    url = "http://blog.coderhelper.cn",
    author = "limhang",
    author_email = "lm_hang@163.com",
    install_requires=[
        'requests','lxml','pymysql'
    ],
    entry_points='''
        [console_scripts]
        BFStringDeal=BFScratch:BFStringDeal
    ''',)
