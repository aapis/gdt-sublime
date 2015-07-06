import os
import sublime
import sublime_plugin
import subprocess
import json
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
			converted = str(convert.from_ansi(output).encode('utf-8'))

			if(self.is_json(converted)):
				_list = json.loads(converted)
				output = "".join(_list)
			else:
				output = converted

			return (True, output.decode('utf-8'))
		else:
			return (False, "Error occurred running %s:\n%s" % (granify_command, error))

	def is_json(self, input):
		try:
			json_object = json.loads(input)
		except ValueError, e:
			return False
		return True