import sublime
import sublime_plugin
import os.path

class GranifyEventListeners(sublime_plugin.EventListener):
	def on_post_save(self, view):
		settings = sublime.load_settings('Granify.sublime-settings')
		filename, extension = os.path.splitext(view.file_name())

		extensions = []
		extensions.append('.coffee')
		extensions.append('.sass')
		extensions.append('.scss')

		if settings.get('granify_recompile_on_save'):
			if(extension in extensions):
				view.run_command('granify_recompile')