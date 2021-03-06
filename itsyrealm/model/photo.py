from flask import escape
from itsyrealm.model.main import db

class Photo(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.Text, nullable=True)
	description = db.Column(db.Text, nullable=True)
	full_url = db.Column(db.Text, nullable=True)
	thumb_url = db.Column(db.Text, nullable=True)

	def serialize(self):
		return {
			'id': self.id,
			'title': self.title,
			'description': self.description
		}
