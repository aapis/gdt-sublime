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

class GranifyResyncCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sublime.status_message("Syncing granify/goliath")

		command = "granify recompile resync"
		queue = Queue.Queue()
		general = Commander(command, queue)
		general.start()
		settings = sublime.load_settings('Granify.sublime-settings')

		if settings.get('granify_always_wait_for_threads'):
			# The following code gets the response from the executed command, it's more
			# accurate but also requires you to wait for the thread to finish
			command_executed, message = queue.get()

			if(command_executed):
				sublime.message_dialog("Granify and Goliath are in sync")
			else:
				sublime.error_message("Problem syncing granify/goliath")
		else:
			sublime.message_dialog("Syncing in progress")

class GranifyRecompileCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sublime.status_message("Compiling granify and goliath")

		command = "granify recompile"
		queue = Queue.Queue()
		general = Commander(command, queue)
		general.start()
		settings = sublime.load_settings('Granify.sublime-settings')

		if settings.get('granify_always_wait_for_threads'):
			# The following code gets the response from the executed command, it's more
			# accurate but also requires you to wait for the thread to finish
			command_executed, message = queue.get()

			if(command_executed):
				sublime.message_dialog('Granify and Goliath compiled successfully')
			else:
				sublime.error_message("Problem compiling granify/goliath")
		else:
			sublime.message_dialog("Compilation in progress")

class GranifyMigrateDevelopmentCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sublime.status_message("Compiling granify and goliath")

		command = "granify migrate development"
		queue = Queue.Queue()
		general = Commander(command, queue)
		general.start()
		settings = sublime.load_settings('Granify.sublime-settings')

		if settings.get('granify_always_wait_for_threads'):
			# The following code gets the response from the executed command, it's more
			# accurate but also requires you to wait for the thread to finish
			command_executed, message = queue.get()

			if(command_executed):
				sublime.message_dialog('Development environment migration completed successfully')
			else:
				sublime.error_message("An error occurred while migrating to development")
		else:
			sublime.message_dialog("Migration in progress")

class GranifyMigrateTestCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sublime.status_message("Compiling granify and goliath")

		command = "granify migrate test"
		queue = Queue.Queue()
		general = Commander(command, queue)
		general.start()
		settings = sublime.load_settings('Granify.sublime-settings')

		if settings.get('granify_always_wait_for_threads'):
			# The following code gets the response from the executed command, it's more
			# accurate but also requires you to wait for the thread to finish
			command_executed, message = queue.get()

			if(command_executed):
				sublime.message_dialog('Test environment migration completed successfully')
			else:
				sublime.error_message("An error occurred while migrating to test")
		else:
			sublime.message_dialog("Migration in progress")

class GranifyStartupCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		command = "granify startup both"
		queue = Queue.Queue()
		general = Commander(command, queue)
		settings = sublime.load_settings('Granify.sublime-settings')

		if settings.get('granify_always_wait_for_threads'):
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
