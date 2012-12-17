#!/usr/bin/python

import twitter
import random
import imp
import os

class randomtweet:

	def __init__(self):
		self.loadconfig()
		self.apilogin()

        def loadconfig(self):
                self.config = imp.load_source('rng_config', self.filepath('config.py'))

	def filepath(self,file):
		filename = os.path.join(os.path.dirname(os.path.abspath(__file__)),file)
		return filename

	def getline(self):
		try:
			f = open(self.filepath('randomtweet.txt'))
		except IOError:
			print "The tweet datafile could not be opened"
			return

	        try:
        	        fcount = open(self.filepath('count.txt'),'r')
	        except IOError:
			lasttweet = -1
		else:
			lasttweet = int(fcount.read())
			fcount.close


		lines = f.read().splitlines()
	
		while True:
			linenum = random.randrange(0,len(lines))
			if linenum == lasttweet: continue		
			break
		fcount = open(self.filepath('count.txt'),'w')
		fcount.write(str(linenum))
		f.close
		fcount.close
		return lines[linenum]

	def apilogin(self):
		self.api = twitter.Api(self.config.consumer_key, self.config.consumer_secret, self.config.access_token_key, self.config.access_token_secret)

	def sendtweet(self):

		try:
        		status = self.api.PostUpdate(self.getline())
		except twitter.TwitterError as e:
        		print "Error: Unable to send tweet - " + e.message
		else:
		        print "Tweet sent"


if __name__ == '__main__':
	
	rt = randomtweet()

	rt.sendtweet()
