import sublime
import sublime_plugin
import os.path

class GranifyEventListeners(sublime_plugin.EventListener):
	def on_post_save(self, view):
		settings = sublime.load_settings('Granify.sublime-settings')
		filename, extension = os.path.splitext(view.file_name())

		resync_on = []
		resync_on.append('.coffee')
		resync_on.append('.sass')
		resync_on.append('.scss')

		if settings.get('granify_resync_on_save'):
			if(extension in resync_on):
				view.run_command('granify_resync')