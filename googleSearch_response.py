from processing_request import GetResponse, convert_to_url

class GoogleSearchResponse(object):

	def __init__(self, search_item): 
		self.search_item = search_item
		self.response_obj = GetResponse("Search", 
								self.search_item)
		self.start()

	def start(self):
		# Google Search for items passed here
		self.search_item = self.response_obj.process_get()

		print self.search_item

	def get(self):
		# scrapy here
		return self.search_item
		