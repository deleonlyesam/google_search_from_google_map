import requests
import urllib


def convert_to_url(search_from, search_item):
	google_map_uri = "https://maps.googleapis.com/maps/api/geocode/json?"
	google_search_uri = "https://www.google.com.ph/?gws_rd=ssl#"	

	if search_from.upper() in "MAP":
		url_query = {'address': search_item}
		url =  google_map_uri
	else: 
		url_query = {'q': search_item}
		url = google_search_uri

	return "%s%s" % (url, urllib.urlencode(url_query))
		
class GetResponse(object):

	def __init__(self, search_from, search_item):
		self.search_from = search_from
		self.search_item = search_item
	
	def process_get(self):
		try:
			uri = convert_to_url(self.search_from, self.search_item)	
			google_response = requests.get(uri)
			return google_response.content

		except Exception, err:
			return err

	def process_post(self, uri):
		pass
