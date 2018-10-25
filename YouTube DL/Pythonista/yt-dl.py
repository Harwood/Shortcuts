#! /usr/bin/env python3
# -*- coding: utf-8 -*-
""" yt-dl.py '{"options": [], "urls": ["https://www.youtube.com/watch?v=BaW_jenozKc"]}' """

import json
import os
import sys
import youtube_dl

__author__ = "Harwood"
__copyright__ = ""
__credits__ = ["Harwood"]
__license__ = ""
__version__ = "0.1.1"
__maintainer__ = "Harwood"
__email__ = ""
__status__ = "Development"


def main(input):
	# TODO: validate JSON structure of input
	
	with youtube_dl.YoutubeDL(input['options']) as ydl:
		ydl.download(input['urls'].splitlines())


if __name__ == '__main__':
	sys.exit(main(json.loads(sys.argv[1])))
