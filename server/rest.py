#!/usr/bin/env python
import os
import web
import json

with open('sound_bites.js') as data_file:    
    data = json.load(data_file)

urls = (
    '/soundBites', 'list_sound_bites',
    '/soundBite/(.*)', 'get_sound_bite'
)

app = web.application(urls, globals())

class os_operations:
	def playMeOut(fileToPlay):
		os.system('xmms2 add "mp3/'+fileToPlay+'"')
		os.system('xmms2 play')
		os.system('xmms2 remove 1')

class list_sound_bites:        
    def GET(self):
	return str(data).replace("u'","'")

class get_sound_bite:
    def GET(self, soundBite):
	print 'soundBite->', soundBite
	for child in data:
		if child['id'] == int(soundBite):
			print str(child).replace("u'","'")
			fileToPlay = child['name']
			os.system('xmms2 add "mp3/'+fileToPlay+'"')
			os.system('xmms2 play')
			os.system('xmms2 remove 1')
			return str(child).replace("u'","'")

if __name__ == "__main__":
    app.run()
