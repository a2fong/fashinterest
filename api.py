#!flask/bin/python
from flask import Flask, render_template
from flask_restful import reqparse, Api, Resource, fields, marshal_with
from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__, static_folder="static")
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
        self.blurb = blurb
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
        for x in range(0, 60):
            title = "title"
            title += str(x)
            blurb = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
            author = "author"
            author += str(x)
            thumb = "http://dzasv7x7a867v.cloudfront.net/product_photos/20073051/98)_60S_5D9FE_7D_5DQ_AE_607YHVN7V_original.jpg"
            details = "api/fashin?limit=1&page="
            details += str(x+1)
            f = FashinDao(title=title, blurb=blurb, author=author, thumbnail_url=thumb, details_url=details)
            session.add(f)

        session.commit()

        args = parser.parse_args()

        if args['limit'] is None:
            limit = 20
        else:
            limit = args['limit']

        if args['page'] is None:
            page = 1
        else:
            page = args['page']

        offset = (page-1) * limit

        q = session.query(FashinDao)
        fashins = q.offset(offset).limit(limit).all()
        return fashins

api.add_resource(Fashin, '/api/fashin')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=False)
