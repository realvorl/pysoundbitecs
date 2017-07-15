# Minimal Sound Board Client - Server

###Allows you to play back soundbites over the network on your raspberry or any other computer with Network and Sound capabilities that can also run Python.

### For the server part:

> http://bit.ly/python-rest

This web service, once started, will parse:  `sound_bites.js` and use it as a source for serving information bout the resource that is being played back.

To be able to run the python script, you must ensure that the file is executable:

    chmod +x rest.py

After that you run it using:

	./rest.py
	
The actual MP3's are played using xmms2, here is how to install and read about it:

>  sudo apt install xmms2 
>  man xmms2

### For the client part:
