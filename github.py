import sublime
import sublime_plugin
from commander import Commander

class GranifyGithubMergedTodayCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		command = "granify github merged_today"
		general = Commander(command)
		response = general.send_order(self.__class__.__name__)
		
		if(response[0]):
			window = self.view.window()
			log_window = window.new_file()
			log_window.insert(edit, 0, response[1])
			log_window.set_name("Pull Requests Merged Today")
			log_window.set_read_only(True)
		else:
			sublime.message_dialog("No PRs were merged today!")

class GranifyGithubMergedOnCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		command = "granify github merged_on"
		general = Commander(command)
		response = general.send_order(self.__class__.__name__)
		
		if(response[0]):
			window = self.view.window()
			log_window = window.new_file()
			log_window.insert(edit, 0, response[1])
			log_window.set_name("Pull Requests Merged On {DATE}")
			log_window.set_read_only(True)
		else:
			sublime.message_dialog("No PRs were merged on that day")

class GranifyGithubMergedBetweenCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sublime.status_message("Testing!")

		command = "granify github merged_between"
		general = Commander(command)
		response = general.send_order(self.__class__.__name__)
		
		if(response[0]):
			window = self.view.window()
			log_window = window.new_file()
			log_window.insert(edit, 0, response[1])
			log_window.set_name("Pull Requests Merged Between {DATE} and {DATE}")
			log_window.set_read_only(True)
		else:
			sublime.message_dialog("No PRs were merged in that range")