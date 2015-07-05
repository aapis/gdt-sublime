import sublime
import sublime_plugin

class GranifyGithubMergedTodayCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sublime.status_message("Testing!")

		command = "granify github merged_today"
		general = Commander(command)
		general.send_order()

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