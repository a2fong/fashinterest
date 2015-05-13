from app import app,models,db
from app import app,db,manager,models
import flask.ext.restless
import json

class Fashin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    blurb = db.Column(db.Text)
    author = db.Column(db.String(120))
    thumbnail_url = db.Column(db.String(120))
    details_url = db.Column(db.String(120))

    def __repr__(self):
        return '<Fashin %r>' % (self.title)

db.create_all()

@app.route('/')
@app.route('/index')
def index():
    f = Fashin(title="title1", blurb="blurb1", author="author1", thumbnail_url="thumbnail_url1", details_url="details_url1")
    db.session.add(f)
    g = Fashin(title="title2", blurb="blurb2", author="author2", thumbnail_url="thumbnail_url2", details_url="details_url2")
    db.session.add(g)
    db.session.commit
    fashin_blueprint = manager.create_api(Fashin, methods=['GET', 'POST', 'DELETE'])
    print fashin_blueprint
    return 'success'

#
# @app.route('/api/fashin/get.json', methods=['GET'])
# def getFashins():
#     f = models.Fashin(title="title1", blurb="blurb1", author="author1", thumbnail_url="thumbnail_url1", details_url="details_url1")
#     db.session.add(f)
#     g = models.Fashin(title="title2", blurb="blurb2", author="author2", thumbnail_url="thumbnail_url2", details_url="details_url2")
#     db.session.add(g)
#     db.session.commit
#
#     fs = models.Fashin.query.all()
#
#     print fs
#     return fs
