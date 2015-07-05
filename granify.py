import os
import sublime
import sublime_plugin
import os.path
from commander import Commander

class GranifyRecompileCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sublime.status_message("Recompiling granify/goliath")

		command = "granify recompile"
		general = Commander(command)
		general.send_order()

class GranifyStartupCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sublime.status_message("Starting granify/goliath")

		command = "granify startup both"
		general = Commander(command)
		general.send_order()

# REMOVE ME
class GranifyTestingCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sublime.status_message("Testing!")

		command = "evertils get info"
		general = Commander(command)
		general.send_order()
		