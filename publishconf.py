#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os
import sys

sys.path.append(os.curdir)

from pelicanconf import *

SITEURL = 'http://pynorte.python.org.br'
RELATIVE_URLS = True

FEED_ALL_ATOM = 'blog/feeds.atom'
FEED_ALL_RSS = 'blog/feeds.rss'

DELETE_OUTPUT_DIRECTORY = True

DISQUS_SITENAME = "pynorte"
DISQUS_NO_ID = True

# Following items are often useful when publishing

#GOOGLE_ANALYTICS = ""
