class Monkey(object):
	def __init__ (self, intelligence, skin, sound, speed):
		self.IQ = intelligence
		self.skinColor = skin
		self.sound = sound
		self.speed = speed

	def running(monkey):
		print "This monkey is running at %s" %(monkey.speed)
		return None

	def __str__(self):
		return "This %s monkey's IQ is %d, and it cries %s" %(self.skinColor, self.IQ, self.sound)


newMon = Monkey(181, "red", "ookeyey", "5mi/h")
print newMon