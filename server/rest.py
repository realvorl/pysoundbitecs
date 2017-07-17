#!/usr/bin/env python
import os
import web
import json

mp3List = os.listdir("mp3")


urls = (
	'/soundBites', 'list_sound_bites',
	'/soundBite/(.*)', 'get_sound_bite'
)

app = web.application(urls, globals())


class anItem:
	def __init__(self, id, title, img):
		self.id = id
		self.title = title
		self.img = img

def pullListing(fileList):
	mp3JsonList = []
	n=0
	for x in fileList:
		mp3JsonList.append(anItem(n, x, x+".jpg").__dict__)
		n+=1
	return mp3JsonList

class list_sound_bites:
	def GET(self):
		web.header('Access-Control-Allow-Origin','*')
		web.header('Content-Type','application/json')
		mp3JsonList=pullListing(os.listdir("mp3"))
		resp = json.dumps(mp3JsonList)
		return resp

class get_sound_bite:
	def GET(self, soundBite):
		web.header('Access-Control-Allow-Origin','*')
		web.header('Content-Type','application/json')
		mp3JsonList=pullListing(os.listdir("mp3"))
		for child in mp3JsonList:
			if child['id'] == int(soundBite):
				print child
				fileToPlay = child['title']
				os.system('xmms2 add "mp3/'+fileToPlay+'"')
				os.system('xmms2 play')
				os.system('xmms2 remove 1')
				resp = json.dumps(child)
				return resp

if __name__ == "__main__":
	app.run()
