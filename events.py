import sublime
import sublime_plugin
import os.path

class GranifyEventListeners(sublime_plugin.EventListener):
	def on_post_save(self, view):
		settings = sublime.load_settings('Granify.sublime-settings')
		filename, extension = os.path.splitext(view.file_name())

		recompile_on = []
		recompile_on.append('.coffee')
		recompile_on.append('.sass')
		recompile_on.append('.scss')
		recompile_on.append('.rb')

		if settings.get('granify_recompile_on_save'):
			if(extension in recompile_on):
				view.run_command('granify_recompile')