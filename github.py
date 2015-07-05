import sublime
import sublime_plugin
from commander import Commander

class GranifyGithubMergedTodayCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sublime.status_message("Testing!")
		
		command = "granify github merged_today"
		general = Commander(command)
		
		window = self.view.window()
		log_window = window.new_file()
		log_window.insert(edit, 0, general.send_order())

class GranifyGithubMergedOnCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sublime.status_message("Testing!")

		command = "granify github "
		general = Commander(command)
		general.send_order()

class GranifyGithubMergedBetweenCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sublime.status_message("Testing!")

		command = "granify github "
		general = Commander(command)
		general.send_order()