import os
import sublime
import sublime_plugin
import subprocess
from outputformatter import OutputFormatter

class Commander():
	def __init__(self, command):
		self.command = "source $HOME/.bash_profile && %s" %command

	def send_order(self, granify_command):
		convert = OutputFormatter()

		pipe = subprocess.Popen(self.command, shell=True, stdout=subprocess.PIPE)
		output, error = pipe.communicate()
		return_code = pipe.poll()
		
		if return_code == 0 and error == None:
			return (True, convert.from_ansi(output))
		else:
			return (False, "Error occurred running %s:\n%s" % (granify_command, error))