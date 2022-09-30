from setuptools import setup, find_packages

with open('requirements.txt') as fp:
	requirements = fp.readlines()

long_description = 'Youtube to wav converter'

setup(
	name='y2wav',
	version='1.0.0',
	author='ovuruska',
	author_email='oguzvuruskaner@gmail.com',
	url='https://github.com/ovuruska/y2wav',
	description='Demo Package for GfG Article.',
	long_description=long_description,
	long_description_content_type="text/markdown",
	license='MIT',
	packages=find_packages(),
	entry_points={
		'console_scripts': [
			'y2wav = y2wav.y2wav:main'
		]
	},
	classifiers=(
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	),
	keywords='youtube wav downloader mp3l',
	install_requires=requirements,
	zip_safe=False
)