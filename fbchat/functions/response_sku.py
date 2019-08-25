import json

class Supplier():
	def __init__(self, sku, image, files=''):
		self.sku = sku
		self.image = image
		self.files = files
	
	def response_sku(self):
		with open(self.files, 'r', encoding='utf-8') as f:
			sku_load = json.load(f)
			description = sku_load[self.sku]['description']
			return description
			
	def response_image(self):
		with open(self.files, 'r', encoding='utf-8') as f:
			img_load = json.load(f)
			images = img_load[self.image]['image']
			return images


class TwinsShop(Supplier):
	def __init__(self, sku, image):
		super().__init__(sku, image)
		self.files = 'functions/supplier/twinsshop.json'	


class ChoiShop(Supplier):
	def __init__(self, sku, image):
		super().__init__(sku, image)
		self.files = 'functions/supplier/choishop.json'