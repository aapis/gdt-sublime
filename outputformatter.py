import re

class Convert:
	def from_ansi(self, string):
		ansi_escape = re.compile(r'\x1b[^m]*m')
		
		return ansi_escape.sub('', string)
