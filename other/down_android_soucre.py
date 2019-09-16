# coding=utf-8

import xml.dom.minidom
import os

############### 需要配置 #######################
# 源码存储路径，替换成你自己的路径
DOWNLOAD_PATH = r"G:\source\android source\android-9.0.0_r42"
# 清单文件路径
MANIFEST_PATH = r"G:\source\android source\manifest\default.xml"

###############################################

# GIT_PREFIX = "git clone https://android.googlesource.com/"
GIT_PREFIX = "git clone git://mirrors.ustc.edu.cn/aosp/"
GIT_SUFFIX = ".git"

# 新建目录
if not os.path.exists(DOWNLOAD_PATH):
    os.makedirs(DOWNLOAD_PATH)

root = xml.dom.minidom.parse(MANIFEST_PATH).documentElement
for project in root.getElementsByTagName("project"):
    path = project.getAttribute("path")
    name = project.getAttribute("name")

    os.chdir(DOWNLOAD_PATH)
    last = path.rfind("/")
    if last != -1:
        path = os.path.join(DOWNLOAD_PATH, path[:last])
        if not os.path.exists(path):
            os.makedirs(path)
        os.chdir(path)
    cmd = GIT_PREFIX + name + GIT_SUFFIX
    print(cmd)
    os.system(cmd)