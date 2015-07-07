import sublime
import sublime_plugin
import Queue
import datetime
from commander import Commander

class GranifyGithubMergedTodayCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		window = sublime.active_window()
		command = "granify github merged_today"
		queue = Queue.Queue()
		general = Commander(command, queue)
		general.start()
		command_executed, message = queue.get()
		
		if(command_executed):
			log_window = window.new_file()
			log_window.insert(edit, 0, message)
			log_window.set_name("Pull Requests Merged Today")
			log_window.set_scratch(True)
			log_window.set_status("granify_generated_on", "Generated on "+ str(datetime.datetime.now().strftime("%y-%m-%d @ %H:%M")))
		else:
			sublime.message_dialog("No PRs were merged today!\n%s" % message)

class GranifyGithubMergedOnCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		window = sublime.active_window()
		self.edit = edit
		window.show_input_panel("Date (YYYY-MM-DD):", "", self.on_done, None, None)

	def on_done(self, date):
		if(date):
			command = "granify github merged_on --start=%s" % date
			queue = Queue.Queue()
			general = Commander(command, queue)
			general.start()
			command_executed, message = queue.get()
			
			if(command_executed):
				window = sublime.active_window()
				log_window = window.new_file()
				log_window.insert(self.edit, 0, message)
				log_window.set_name("Pull Requests Merged On %s" % message)
				log_window.set_scratch(True)
				log_window.set_status("granify_generated_on", "Generated on "+ str(datetime.datetime.now().strftime("%y-%m-%d @ %H:%M")))
			else:
				sublime.message_dialog("No PRs were merged on that day\n%s" % message)

class GranifyGithubMergedBetweenCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		window = sublime.active_window()
		self.edit = edit
		window.show_input_panel("Date Range:", "", self.on_done, None, None)
	
	def on_done(self, d_range):
		date_range = d_range.split(' to ')
		command = "granify github merged_between --start=%s --end=%s" % (date_range[0], date_range[1])
		queue = Queue.Queue()
		general = Commander(command, queue)
		general.start()
		command_executed, message = queue.get()
		
		if(command_executed):
			window = sublime.active_window()
			log_window = window.new_file()
			log_window.insert(self.edit, 0, message)
			log_window.set_name("Pull Requests Merged Between %s and %s" % (date_range[0], date_range[1]))
			log_window.set_scratch(True)
			log_window.set_status("granify_generated_on", "Generated on "+ str(datetime.datetime.now().strftime("%y-%m-%d @ %H:%M")))
		else:
			sublime.message_dialog("No PRs were merged in that range\n%s" % message)
