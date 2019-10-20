from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Document(Base):

    __tablename__ = 'documents'

    name = Column(String, primary_key=True)
    content = Column(String)
