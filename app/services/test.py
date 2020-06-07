from app.models.test import Test


class TestServices():
	def __init__(self):
		pass
		
	def add_test(self, name, age):
		test = Test(name=name, age=age)
		test.save()

		return test.to_dict()
