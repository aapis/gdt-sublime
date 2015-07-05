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
		response = general.send_order(self.__class__.__name__)

		if(response[0]):
			sublime.message_dialog("Granify and Goliath were recompiled")
		else:
			sublime.error_message("Problem recompiling granify/goliath")

class GranifyStartupCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		command = "granify startup both"
		general = Commander(command)
		response = general.send_order(self.__class__.__name__)

		if(response[0]):
			sublime.message_dialog("Granify and Goliath started")
		else:
			sublime.error_message("Problem starting granify/goliath")

class GranifyRunCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		command = "granify run granify"
		general = Commander(command)
		response = general.send_order(self.__class__.__name__)

		if(response[0]):
			sublime.message_dialog("Granify and Goliath are running (attached to logs)")
		else:
			sublime.error_message("Problem running granify/goliath")
		