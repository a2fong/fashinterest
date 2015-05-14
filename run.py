#!flask/bin/python
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource, fields, marshal_with
from sqlalchemy import Table, MetaData, orm, Column, String, Integer, create_engine
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)
api = Api(app)

Base = declarative_base()

class FashinDao(Base):
    __tablename__ = 'FashinDao'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    blurb = Column(String)
    author = Column(String)
    thumbnail_url = Column(String)
    details_url = Column(String)

    def __init__(self, title, blurb, author, thumbnail_url, details_url):
        self.title = title
        self.blub = blurb
        self.author = author
        self.thumbnail_url = thumbnail_url
        self.details_url = details_url

    def __repr__(self):
        return '<Fashin %r>' % (self.title)

parser = reqparse.RequestParser()
parser.add_argument('page', type=int)
parser.add_argument('limit', type=int)

resource_fields = {
    'title':   fields.String,
    'blurb':    fields.String,
    'author':   fields.String,
    'thumbnail_url':    fields.String,
    'details_url':   fields.String
}

class Fashin(Resource):
    @marshal_with(resource_fields)
    def get(self):
        engine = create_engine('sqlite://', echo=True)
        Base.metadata.create_all(engine)

        session = Session(engine)
        f = FashinDao(title="title1", blurb="blurb1", author="author1", thumbnail_url="thumbnail_url1", details_url="details_url1")
        session.add(f)
        session.commit()
        g = FashinDao(title="title2", blurb="blurb2", author="author2", thumbnail_url="thumbnail_url2", details_url="details_url2")
        session.add(g)
        session.commit()

        args = parser.parse_args()
        if args['limit'] is None:
            limit = 20
        else:
            limit = args['limit']

        print limit

        if args['page'] is None:
            page = 1
        else:
            page = args['page']

        offset = (page-1) * limit

        print "offset"
        print offset

        q = session.query(FashinDao)
        fashins = q.offset(offset).limit(limit).all()
        return fashins

api.add_resource(Fashin, '/api/fashin')

if __name__ == '__main__':
    app.run(debug=True)
