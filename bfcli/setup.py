from setuptools import setup

setup(
    name='xx',
    version='0.1',
    py_modules=['xx'],
    url = "http://blog.coderhelper.cn",
    author = "limhang",
    author_email = "lm_hang@163.com",
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        xx=xx:cli
    ''',
)
