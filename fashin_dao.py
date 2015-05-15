from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base

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

engine = create_engine('sqlite://', echo=True)
Base.metadata.create_all(engine)