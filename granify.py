import os
import sublime
import sublime_plugin
import subprocess
import os.path
from subprocess import call

PLUGIN_DIRECTORY = os.getcwd().replace(os.path.normpath(os.path.join(os.getcwd(), '..', '..')) + os.path.sep, '').replace(os.path.sep, '/')

class RecompileCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		print "Recompiling granify/goliath"
		print os.popen("granify recompile").read()

class StartupCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		print "Starting granify/goliath"
		print os.popen("granify startup both").read()

class TestingCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		print "Testing!"
		print os.popen("EVERTILS=test evertils get info").read()
		