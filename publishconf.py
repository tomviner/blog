#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://tomviner.co.uk'
FEED_DOMAIN = SITEURL

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Uncomment following line for absolute URLs in production:
# RELATIVE_URLS = False

# Following items are often useful when publishing

DISQUS_SITENAME = 'viner'
GOOGLE_ANALYTICS = 'UA-38679370-1'
