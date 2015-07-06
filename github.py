import sublime
import sublime_plugin
from commander import Commander

class GranifyGithubMergedTodayCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		window = self.view.window()
		command = "granify github merged_today"
		general = Commander(command)
		response = general.send_order(self.__class__.__name__)
		
		if(response[0]):
			log_window = window.new_file()
			log_window.insert(edit, 0, response[1])
			log_window.set_name("Pull Requests Merged Today")
			log_window.set_read_only(True)
		else:
			sublime.message_dialog("No PRs were merged today!\n%s" % response[1])

class GranifyGithubMergedOnCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		window = self.view.window()
		window.show_input_panel("Date:", "", self.on_done, None, None)
		
	def on_done(self, date):
		if(date != None):
			command = "granify github merged_on --start=%s" % date
			general = Commander(command)
			response = general.send_order(self.__class__.__name__)
			
			if(response[0]):
				window = self.view.window()
				log_window = window.new_file()
				log_window.insert(edit, 0, response[1])
				log_window.set_name("Pull Requests Merged On %s" % response[1])
				log_window.set_read_only(True)
			else:
				sublime.message_dialog("No PRs were merged on that day\n%s" % response[1])

class GranifyGithubMergedBetweenCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		window = self.view.window()
		window.show_input_panel("Date Range:", "", self.on_done, None, None)
	
	def on_done(self, d_range):
		date_range = d_range.split(' to ')
		command = "granify github merged_between --start=%s --end=%s" % (date_range[0], date_range[1])
		general = Commander(command)
		response = general.send_order(self.__class__.__name__)
		
		if(response[0]):
			window = self.view.window()
			log_window = window.new_file()
			log_window.insert(edit, 0, response[1])
			log_window.set_name("Pull Requests Merged Between %s and %s" % (date_range[0], date_range[1]))
			log_window.set_read_only(True)
		else:
			sublime.message_dialog("No PRs were merged in that range\n%s" % response[1])