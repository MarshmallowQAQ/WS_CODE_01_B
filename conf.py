# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/WS_CODE_01_B/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
template = {
    "name": "Galileo",
    "type": "local",
    "path": "../Galileo"
}
enable_jsdelivr = {
    "enabled": True,
    "repo": "MarshmallowQAQ/WS_CODE_01_B@gh-pages"
}

# 站点设置
site_name = "MarshmallowQAQ"
site_logo = "${static_prefix}main-logo.png"
site_build_date = "2019-12-31T22:07+08:00"
author = ""
email = ""
author_homepage = ""
description = "Uh... what should I write?"
key_words = []
language = 'zh-CN'
external_links = [
    {
        "name": "Maverick",
        "url": "https://github.com/AlanDecode/Maverick",
        "brief": "🏄‍ Go My Own Way."
    },
    {
        "name": "MarshmallowQAQ",
        "url": "https://marsqwq.top",
        "brief": "MarshmallowQAQ's Website."
    }
]
nav = [
    {
        "name": "Home",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "Archives",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "About",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [

]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''
