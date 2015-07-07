import os
import sublime
import sublime_plugin
import os.path
import Queue
from commander import Commander

WAIT_FOR_THREAD = False

class GranifyRecompileCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sublime.status_message("Recompiling granify/goliath")

		command = "granify recompile"
		queue = Queue.Queue()
		general = Commander(command, queue)
		general.start()

		if WAIT_FOR_THREAD:
			# The following code gets the response from the executed command, it's more
			# accurate but also requires you to wait for the thread to finish
			command_executed, message = queue.get()

			if(command_executed):
				sublime.message_dialog("Granify and Goliath were recompiled")
			else:
				sublime.error_message("Problem recompiling granify/goliath")
		else:
			sublime.message_dialog("Recompiling in progress")
		

class GranifyStartupCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		command = "granify startup both"
		queue = Queue.Queue()
		general = Commander(command, queue)

		if WAIT_FOR_THREAD:
			# The following code gets the response from the executed command, it's more
			# accurate but also requires you to wait for the thread to finish
			command_executed, message = queue.get()

			if(command_executed):
				sublime.message_dialog("Granify and Goliath started")
			else:
				sublime.error_message("Problem starting granify/goliath")
		else:
			sublime.message_dialog("Startup in progress")