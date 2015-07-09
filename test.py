import sublime
import sublime_plugin
from commander import Commander

class GranifyTestGranify(sublime_plugin.TextCommand):
	def run(self, edit):
		command = "granify test granify"
		queue = Queue.Queue()
		general = Commander(command, queue)
		general.start()
		command_executed, message = queue.get()
		
		if(command_executed):
			window = self.view.window()
			log_window = window.new_file()
			log_window.insert(edit, 0, message)
			log_window.set_name("Granify Spec Test Results")
			log_window.set_read_only(True)
		else:
			sublime.message_dialog(message)

class GranifyTestGoliath(sublime_plugin.TextCommand):
	def run(self, edit):
		command = "granify test goliath"
		queue = Queue.Queue()
		general = Commander(command, queue)
		general.start()
		command_executed, message = queue.get()
		
		if(command_executed):
			window = self.view.window()
			log_window = window.new_file()
			log_window.insert(edit, 0, message)
			log_window.set_name("Goliath Test Results")
			log_window.set_read_only(True)
		else:
			sublime.message_dialog(message)

class GranifyTestJs(sublime_plugin.TextCommand):
	def run(self, edit):
		command = "granify test js"
		queue = Queue.Queue()
		general = Commander(command, queue)
		general.start()
		command_executed, message = queue.get()
		
		if(command_executed):
			window = self.view.window()
			log_window = window.new_file()
			log_window.insert(edit, 0, message)
			log_window.set_name("JS Integration Test Results")
			log_window.set_read_only(True)
		else:
			sublime.message_dialog(message)