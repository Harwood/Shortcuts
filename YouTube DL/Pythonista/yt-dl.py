#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''
yt-dl.py '{"options": [], "urls": ["https://www.youtube.com/watch?v=BaW_jenozKc"]}'
'''

import json
import notification
import os
import sys
import webbrowser
import youtube_dl

__author__ = "Harwood"
__copyright__ = ""
__credits__ = ["Harwood"]
__license__ = "MIT"
__version__ = "0.1.2"
__maintainer__ = "Harwood"
__email__ = ""
__status__ = "Development"


class Shortcut:
	def __init__(self, options):
		# TODO: validate options
		options['progress_hooks'] = [Shortcut.hook]
		self.ytdl = youtube_dl.YoutubeDL(options)

	def __enter__(self):
		return self

	def __exit__(self, exc_type, exc_val, exc_tb):
		pass

	def download(self, urls):
		# TODO: validate urls
		self.ytdl.download(urls)

		webbrowser.open('shortcuts://')

	def hook(d):
		if d['status'] == 'finished':
			title = d['filename'].split('/')[-1].split(' - ', 1)[-1].rsplit(' - ', 1)[0]

			notification.schedule(f'Download of "{title}" completed', 1, 'default', '')


def main(input):
	# TODO: validate JSON structure of input
	with Shortcut(input['options']) as shortcut:
		shortcut.download(input['urls'].splitlines())


if __name__ == '__main__':
	sys.exit(main(json.loads(sys.argv[1])))
