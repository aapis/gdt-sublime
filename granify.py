import os
import sublime
import sublime_plugin
import threading
import subprocess
import functools
import os.path
import time
from subprocess import call

PLUGIN_DIRECTORY = os.getcwd().replace(os.path.normpath(os.path.join(os.getcwd(), '..', '..')) + os.path.sep, '').replace(os.path.sep, '/')

def main_thread(callback, *args, **kwargs):
  # sublime.set_timeout gets used to send things onto the main thread
  # most sublime.[something] calls need to be on the main thread
  sublime.set_timeout(functools.partial(callback, *args, **kwargs), 0)


class RecompileCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		print "Recompiling granify/goliath"

		call(["granify", "recompile"])

class StartupCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		print "Starting granify/goliath"

		call(["granify", "startup", "both"])

class TestingCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		print "Testing!"
		print os.popen("evertils get info").read()

		#print call(["evertils", "get", "info"])
		