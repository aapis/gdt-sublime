import os
import sublime
import sublime_plugin
import os.path
import Queue
import shutil
from commander import Commander

PACKAGE_DIR = sublime.packages_path()
USER_SETTINGS = PACKAGE_DIR + '/User/Granify.sublime-settings'
PACKAGE_SETTINGS = PACKAGE_DIR + '/Granify/Granify.sublime-settings'

class GranifyRecompileCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sublime.status_message("Recompiling granify/goliath")

		command = "granify recompile"
		queue = Queue.Queue()
		general = Commander(command, queue)
		general.start()
		settings = sublime.load_settings('Granify.sublime-settings')

		if settings.get('always_wait_for_threads'):
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
		settings = sublime.load_settings('Granify.sublime-settings')

		if settings.get('always_wait_for_threads'):
			# The following code gets the response from the executed command, it's more
			# accurate but also requires you to wait for the thread to finish
			command_executed, message = queue.get()

			if(command_executed):
				sublime.message_dialog("Granify and Goliath started")
			else:
				sublime.error_message("Problem starting granify/goliath")
		else:
			sublime.message_dialog("Startup in progress")

class GranifyOpenSettingsCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		window = self.view.window()
		
		if(not os.path.isfile(USER_SETTINGS)):
			shutil.copyfile(PACKAGE_SETTINGS, USER_SETTINGS)

		window.open_file(USER_SETTINGS)

class GranifyWorkingOnCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		window = sublime.active_window()
		window.show_input_panel("WorkingOn Status", "", self.on_done, None, None)

	def on_done(self, message):
		sublime.status_message("Sending new WorkingOn status")

		command = "granify send workingon \"%s\"" % message.encode('utf-8')
		queue = Queue.Queue()
		general = Commander(command, queue)
		general.start()
