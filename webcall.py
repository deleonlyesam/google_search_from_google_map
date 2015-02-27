from googleMapAPI_response import GoogleMapResponse
from googleSearch_response import GoogleSearchResponse

class MainClass(object):
			
	def __init__(self, search_request): 
		self.googlemap_obj = GoogleMapResponse(search_request)
		
	def map_api_response(self):
		# Start searching values Google Mapping response 
		# 	based from user input
		for objects in self.googlemap_obj.get():
			coordinates = objects[0]
			address = objects[1]
			businesstype = objects[2]
 
			self.search_api_response(address)

	def search_api_response(self, googlesearch): 
		# start Google Search based from output from Google Map
		self.googlesearch = GoogleSearchResponse(googlesearch)
		print self.googlesearch.get()


if __name__ == '__main__':
	import argparse

	cmd = argparse.ArgumentParser()
	cmd.add_argument("--search", help="Search from Google Map")

	config_file_path = cmd.parse_args().search

	a = MainClass(cmd.parse_args().search)
	print a.map_api_response()