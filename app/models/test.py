from app.application import db

class Test(db.Document):
	name = db.StringField()
	age = db.IntField()

	def to_dict(self):
		dict_object = {}
		for key,value in self._fields.items():
			dict_object[key] = getattr(self, key)
		dict_object['id'] = str(dict_object['id'])
		return dict_object