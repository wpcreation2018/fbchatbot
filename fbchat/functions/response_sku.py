import json

class Supplier():
	""" A parent class for reading and return values from json files that store skus key."""
	def __init__(self, sku, image, files=''):
		self.sku = sku
		self.image = image
		self.files = files
	
	def response_sku(self):
		""" Read and return descriptions of sku keys. """
		with open(self.files, 'r', encoding='utf-8') as f:
			sku_load = json.load(f)
			description = sku_load[self.sku]['description']
			return description
			
	def response_image(self):
		""" Read and return images of sku keys. """
		with open(self.files, 'r', encoding='utf-8') as f:
			img_load = json.load(f)
			images = img_load[self.image]['image']
			return images


""" Child classes for returning twinsshop.json inherited from the Supplier parent's class. The "twinsshop.json" file stores skus, image urls and a product's description."""

class TwinsShop(Supplier):
	""" Twinsshop """
	def __init__(self, sku, image):
		super().__init__(sku, image)
		self.files = 'functions/supplier/twinsshop.json'	


class ChoiShop(Supplier):
	""" Choishop """
	def __init__(self, sku, image):
		super().__init__(sku, image)
		self.files = 'functions/supplier/choishop.json'