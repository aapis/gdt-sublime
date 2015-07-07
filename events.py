import sublime
import sublime_plugin
import os.path

class GranifyEventListeners(sublime_plugin.EventListener):
	def on_post_save(self, view):
		settings = sublime.load_settings('Granify.sublime-settings')
		filename, extension = os.path.splitext(view.file_name())
		recompile_on = ['.coffee', '.sass', '.scss']

		if settings.get('granify_recompile_on_save'):
			if(extension in recompile_on):
				view.run_command('granify_recompile')