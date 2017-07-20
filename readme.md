# Minimal Sound Board Client - Server



### Allows you to play back soundbites over the network on your raspberry or any other computer with Network and Sound capabilities that can also run Python.

### For the server part:

	http://bit.ly/python-rest

in case you missed it, you will need `web.py`

    sudo apt install python-pip
    pip install web.py

This web service, once started, will list the content of the `/mp3` folder and transform the filenames into a JSon Array together with the associated images from the `/images` folder.

The Code is setup to display any `.mp3` file as a tile that is represented in `final product.png`

The necessary fields are modeled in this class:

    class anItem:
    	def __init__(self, id, title, img):
    		self.id = id
    		self.title = title
    		self.img = img

To be able to run the python script, you must ensure that the file is executable:

    chmod +x rest.py

After that you run it using:

	./rest.py

The actual MP3's are played using `xmms2`, here is how you can install it:

	sudo apt install xmms2
	man xmms2

### For the client part:

we are going to use REACT.JS with BABEL-CORE and jQuery:

	<script src="https://unpkg.com/react@15/dist/react.js"></script>
	<script src="https://unpkg.com/react-dom@15/dist/react-dom.js"></script>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/babel-core/5.8.34/browser.js"></script>
	<script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>

If all went well you will be able to access / play the mp3's by opening your browser and visiting this adress: 

[http://localhost:8080](URL)

Adding mp3's to `/mp3` folder will add new buttons:

    mp3/images/I'm Mr. Meeseeks, look at me!.mp3

Adding an image with the same name as the mp3 to wich it belongs, will display it on the button instead of the fallback image:

    server/images/I'm Mr. Meeseeks, look at me!.mp3.jpg




