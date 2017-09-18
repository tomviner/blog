#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Tom Viner'
SITENAME = 'Tom Viner'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
     # ('Python.org', 'http://python.org/'),
)

# Social widget
SOCIAL = (
    ('Twitter', 'http://twitter.com/tomviner'),
    ('Github', 'https://github.com/tomviner'),
    ('BitBucket', 'https://bitbucket.com/tomviner'),
    ('Lanyrd', 'http://lanyrd.com/profile/tomviner/'),
    ('LinkedIn', 'http://www.linkedin.com/in/tomviner'),
)
TWITTER_USERNAME = 'tomviner'
GITHUB_ACTIVITY_FEED = 'https://github.com/tomviner.atom'

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# path-specific metadata
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
}

# static paths will be copied without parsing their contents
STATIC_PATHS = [
    'images',
    'talks',
    'extra/robots.txt',
    'extra/favicon.ico',
]

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['sitemap', 'gravatar']

# http://freewisdom.org/projects/python-markdown/Available_Extensions
MD_EXTENSIONS = [
    'codehilite', 'extra',
    # 'video', # https://github.com/skeet70/django-markdown-video/blob/master/mdx_video.py
    # 'urlize', # https://github.com/r0wb0t/markdown-urlize/blob/master/urlize.py
]

SITEURL = 'http://0.0.0.0:8000'
FEED_DOMAIN = SITEURL

SITEMAP = {'format':'txt'}

DEFAULT_DATE = 'fs'

# FEED_ALL_ATOM = 'feeds/all.atom.xml'
# FEED_ALL_RSS = 'feeds/all.rss.xml'
