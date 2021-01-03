# coding=utf-8
# 程序打包，上面第一个设置文件编码
from setuptools import setup
setup(name='zhello',
      version='1.0',
      description='A simple example',
      author='wangshu',
      py_modules=['zhello'])
# 运行命令 python dSetuptools.py bulid
# 生成文件目录bulid/lib/zhello.py
# 安装命令python dSetuptools.py install
# 生成目录dist和zhello.egg-info
