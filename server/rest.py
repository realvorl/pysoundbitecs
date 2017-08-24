#!/usr/bin/env python
import os
import web
import json

urls = (
    '/', 'index',
    '/soundBites', 'ListSoundBites',
    '/soundBite/(.*)', 'GetSoundBite'
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
    extensions = [".gif", ".jpg", ".png"]
    n = 0
    found_img = ""
    for fileName in fileList:
        for ext in extensions:
            if (fileName + ext) in imgList:
                found_img = ext
                break
        if found_img == "":
            mp3JsonList.append(anItem(n, fileName, "default.png").__dict__)
        else:
            mp3JsonList.append(anItem(n, fileName, fileName + ext).__dict__)
            found_img = ""
        n += 1
    return mp3JsonList


class ListSoundBites:

    def __init__(self):
        pass

    def GET(self):
        web.header('Access-Control-Allow-Origin', '*')
        web.header('Content-Type', 'application/json')
        mp3JsonList = pullListing(os.listdir("mp3"), os.listdir("static/images"))
        resp = json.dumps(mp3JsonList)
        return resp


class GetSoundBite:
    def __init__(self):
        pass

    def GET(self, soundBite):
        web.header('Access-Control-Allow-Origin', '*')
        web.header('Content-Type', 'application/json')
        mp3JsonList = pullListing(os.listdir("mp3"), os.listdir("static/images"))

        for child in mp3JsonList:
            if child['id'] == int(soundBite):
                print child
                fileToPlay = child['title']
                os.system('xmms2 add "mp3/' + fileToPlay + '"')
                os.system('xmms2 play')
                os.system('xmms2 remove 1')
                resp = json.dumps(child)
                return resp


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
