import os
import sublime
import sublime_plugin
import os.path
import Queue
from commander import Commander

class GranifyRecompileCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sublime.status_message("Recompiling granify/goliath")
		threads = {}

		command = "granify recompile"
		queue = Queue.Queue()
		general = Commander(command, queue)
		general.start()
		# command_executed, message = queue.get()

		# if(command_executed):
		# 	sublime.message_dialog("Granify and Goliath were recompiled")
		# else:
		# 	sublime.error_message("Problem recompiling granify/goliath")

class GranifyStartupCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		command = "granify startup both"
		queue = Queue.Queue()
		general = Commander(command, queue)
		command_executed, message = queue.get()

		if(command_executed):
			sublime.message_dialog("Granify and Goliath started")
		else:
			sublime.error_message("Problem starting granify/goliath")