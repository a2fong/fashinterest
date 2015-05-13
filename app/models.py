from app import app,db,manager

# class Fashin(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(120))
#     blurb = db.Column(db.Text)
#     author = db.Column(db.String(120))
#     thumbnail_url = db.Column(db.String(120))
#     details_url = db.Column(db.String(120))
#
#     def __repr__(self):
#         return '<Fashin %r>' % (self.title)
#
# db.create_all()

# fashin_blueprint = manager.create_api(Fashin, methods=['GET', 'POST', 'DELETE'])
# print fashin_blueprint
