from __future__ import unicode_literals
import os
import argparse

import youtube_dl
import ffmpeg

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': 'output.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
    }],
}


def main():
	parser = argparse.ArgumentParser(prog='y2wav',
									 description='Youtube to Wav converter')

	parser.add_argument('link', help='youtube_url')

	args = parser.parse_args()
	link = args.link

	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		ydl.download([link])
		stream = ffmpeg.input('output.m4a')
		stream = ffmpeg.output(stream, 'output.wav')

