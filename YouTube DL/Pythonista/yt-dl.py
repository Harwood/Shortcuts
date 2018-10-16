#! /usr/bin/env python3
# -*- coding: utf-8 -*-
""" yt-dl.py: """

import json
import os
import sys
from logzero import logger
import youtube_dl

__author__ = "Harwood"
__copyright__ = ""
__credits__ = ["Harwood"]
__license__ = ""
__version__ = "0.1.0"
__maintainer__ = "Harwood"
__email__ = ""
__status__ = "Development"


def main(ydl_opts, urls):
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		ydl.download(urls)


if __name__ == '__main__':
	input = json.loads(sys.argv[1])
	urls = input['urls'].splitlines()

	sys.exit(main(input['options'], urls))

