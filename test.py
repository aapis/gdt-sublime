import sublime
import sublime_plugin
from commander import Commander

class GranifyTestGranify(sublime_plugin.TextCommand):
	def run(self, edit):
		command = "granify test granify"
		general = Commander(command)
		response = general.send_order(self.__class__.__name__)
		
		if(response[0]):
			window = self.view.window()
			log_window = window.new_file()
			log_window.insert(edit, 0, response[1])
			log_window.set_name("Granify Spec Test Results")
			log_window.set_read_only(True)
		else:
			sublime.message_dialog(response[1])

class GranifyTestGoliath(sublime_plugin.TextCommand):
	def run(self, edit):
		command = "granify test goliath"
		general = Commander(command)
		response = general.send_order(self.__class__.__name__)
		
		if(response[0]):
			window = self.view.window()
			log_window = window.new_file()
			log_window.insert(edit, 0, response[1])
			log_window.set_name("Goliath Test Results")
			log_window.set_read_only(True)
		else:
			sublime.message_dialog(response[1])

class GranifyTestJs(sublime_plugin.TextCommand):
	def run(self, edit):
		command = "granify test js"
		general = Commander(command)
		response = general.send_order(self.__class__.__name__)
		
		if(response[0]):
			window = self.view.window()
			log_window = window.new_file()
			log_window.insert(edit, 0, response[1])
			log_window.set_name("JS Integration Test Results")
			log_window.set_read_only(True)
		else:
			sublime.message_dialog(response[1])