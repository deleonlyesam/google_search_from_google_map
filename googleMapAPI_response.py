import json

from processing_request import GetResponse

class GoogleMapResponse(object):
	
	def __init__(self, search_item):
		self.uri = GetResponse("Map", search_item).process_get() 
		
	def get(self):
		content_to_dict = json.loads(self.uri)
		for results in content_to_dict["results"]:
			if content_to_dict["status"] != "OK": return
			yield self.set_variables(results)
		
	def set_variables(self, dataitems):
		"""
			This function iterates through the response given by
			google map api and fetch values based from necessary
			parameters needed by client namely(
				address, location: (latitude, longitude), 
				type)
		"""
		itemlist = []
		ctr = 0
		if isinstance(dataitems, dict):
			for k,v in dataitems.iteritems():
				if k in ["formatted_address", "types"] and ctr == 0:
					itemlist.extend([str(dataitems["formatted_address"])]) 
					itemlist.extend([str(dataitems["types"])])
					ctr += 1
				if k == "geometry":
					itemlist.extend([(k1,v1) for k1,v1 in v.items() if k1 =="location"])				
		return itemlist
