class Car(object):
	def __init__(self, name='General', model='GM',the_type='saloon'):
		self.name=name
		self.model=model
		self.the_type=the_type
		self.speed=0
		self.num_of_doors=4
		self.num_of_wheels=4

		if (self.name == "Porshe" or self.name == "Koenigsegg"):
			self.num_of_doors = 2

		elif (self.the_type == "trailer"):
			self.num_of_wheels=8

	def is_saloon(self):
		if (self.the_type == "saloon"):
			return True
		return False	

	def drive(self,speed):
		if (speed==7):
			self.speed=77
		elif (speed == 3):
			self.speed=1000
		return self