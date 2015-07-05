import os
import sublime
import sublime_plugin
import subprocess
from outputformatter import Convert

class Commander():
	def __init__(self, command):
		self.command = "source $HOME/.bash_profile && %s" %command

	def send_order(self):
		convert = Convert()

		pipe = subprocess.Popen(self.command, shell=True, stdout=subprocess.PIPE)
		result = pipe.communicate()

		if pipe.returncode == 0:
			print convert.from_ansi(result[0])
		else:
			sublime.status_message("Error occurred running Granify command")