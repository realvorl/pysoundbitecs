#!/usr/bin/env python
import os
import web
import json

urls = (
	'/','index',
	'/soundBites', 'list_sound_bites',
	'/soundBite/(.*)', 'get_sound_bite'
)

render = web.template.render('templates/')

class anItem:
	def __init__(self, id, title, img):
		self.id = id
		self.title = title
		self.img = img

class index:
	def GET(self):
		return render.index()

def pullListing(fileList, imgList):
	mp3JsonList = []
	extensions = [".gif", ".jpg",".png"]
	n=0
	foundImg = ""
	for fileName in fileList:
		for ext in extensions:
			if (fileName+ext) in imgList:
				foundImg = ext
				break
		if (foundImg == ""):
			mp3JsonList.append(anItem(n, fileName, "default.png").__dict__)
		else:
			mp3JsonList.append(anItem(n, fileName, fileName+ext).__dict__)
			foundImg = ""
		n+=1
	return mp3JsonList

class list_sound_bites:
	def GET(self):
		web.header('Access-Control-Allow-Origin','*')
		web.header('Content-Type','application/json')
		mp3JsonList=pullListing(os.listdir("mp3"), os.listdir("images"))
		resp = json.dumps(mp3JsonList)
		return resp

class get_sound_bite:
	def GET(self, soundBite):
		web.header('Access-Control-Allow-Origin','*')
		web.header('Content-Type','application/json')
		mp3JsonList=pullListing(os.listdir("mp3"), os.listdir("images"))

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
	app = web.application(urls, globals())
	app.run()
