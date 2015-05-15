from flask_restful import reqparse, Resource, fields, marshal_with
from sqlalchemy.orm import Session
from fashin_dao import engine, FashinDao

session = Session(engine)

resource_fields = {
    'title':   fields.String,
    'blurb':    fields.String,
    'author':   fields.String,
    'thumbnail_url':    fields.String,
    'details_url':   fields.String
}

parser = reqparse.RequestParser()
parser.add_argument('page', type=int)
parser.add_argument('limit', type=int)

class Fashin(Resource):

    @marshal_with(resource_fields)
    def get(self):
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

    def post(self):
        q = session.query(FashinDao)
        fashins = q.all()
        if not fashins:
            for x in range(0, 105):
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
        return "{success: true}";