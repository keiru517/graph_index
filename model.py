from sqlalchemy import Column, Integer, String, Enum, ForeignKey, Boolean
import datetime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import enum

engine = create_engine('sqlite:///database.db', echo = True)

Session = sessionmaker(bind = engine)
session = Session()


Base = declarative_base()

class User(Base):
   __tablename__ = 'users'
   id = Column(Integer, primary_key=True)
   email = Column('email', String)
   password = Column('password', String)
   first_name = Column('first_name', String)
   last_name = Column('last_name', String)
   created_at = Column('created_at', String, default=datetime.datetime.utcnow)
   updated_at = Column('updated_at', String, default=datetime.datetime.utcnow)


class Project(Base):
   __tablename__ = 'projects'
   id = Column(Integer, primary_key=True)
   user_id = Column(Integer, ForeignKey('users.id'))
   created_at = Column('created_at', String, default=datetime.datetime.utcnow)
   updated_at = Column('updated_at', String, default=datetime.datetime.utcnow)


class Session(Base):
   __tablename__ = 'sessions'
   id = Column(Integer, primary_key=True)
   user_id = Column(Integer, ForeignKey('users.id'))
   created_at = Column('created_at', String, default=datetime.datetime.utcnow)
   expire_at = Column('updated_at', String, default=datetime.datetime.utcnow)

class UserSchema(Base):
   __tablename__ = 'userschemas'
   id = Column(Integer, primary_key=True)
   project_id = Column(Integer, ForeignKey('projects.id'))
   name = Column('name', String)
   created_at = Column('created_at', String, default=datetime.datetime.utcnow)
   updated_at = Column('updated_at', String, default=datetime.datetime.utcnow)

class UserSchemaTable(Base):
   __tablename__ = 'userschematables'
   id = Column(Integer, primary_key=True)
   schema_id = Column(Integer, ForeignKey('userschemas.id'))
   name = Column('name', String)
   created_at = Column('created_at', String, default=datetime.datetime.utcnow)
   updated_at = Column('updated_at', String, default=datetime.datetime.utcnow)


class UserSchemaColumn(Base):
   __tablename__ = 'userschemacolumns'
   id = Column(Integer, primary_key=True)
   table_id = Column(Integer, ForeignKey('userschematables.id'))
   name = Column('name', String)
   data_type = Column('data_type', String)
   schema_term_id = Column(Integer, ForeignKey('schemaorgterms.id'))
   created_at = Column('created_at', String, default=datetime.datetime.utcnow)
   updated_at = Column('updated_at', String, default=datetime.datetime.utcnow)

class SchemaOrgOntology(Base):
   __tablename__ = 'schemaorgontologies'
   id = Column(Integer, primary_key=True)
   version = Column('version', Integer)
   data = Column('data', String)
   created_at = Column('created_at', String, default=datetime.datetime.utcnow)
   updated_at = Column('updated_at', String, default=datetime.datetime.utcnow)

class SchemaOrgTerm(Base):
   __tablename__ = 'schemaorgterms'
   id = Column(Integer, primary_key=True)
   ontology_id = Column(Integer, ForeignKey('schemaorgontologies.id'))
   uri = Column('uri', String)
   name = Column('name', String)
   definition = Column('definition', String)
   data_type = Column('data_type', String)
   created_at = Column('created_at', String, default=datetime.datetime.utcnow)
   updated_at = Column('updated_at', String, default=datetime.datetime.utcnow)

class Mapping(Base):
   __tablename__ = 'mappings'
   id = Column(Integer, primary_key=True)
   project_id = Column(Integer, ForeignKey('projects.id'))
   created_at = Column('created_at', String, default=datetime.datetime.utcnow)
   updated_at = Column('updated_at', String, default=datetime.datetime.utcnow)

class Certainty(enum.Enum):
    high='High'
    medium='Medium'
    low='Low'
    
class MappingDetail(Base):
   __tablename__ = 'mappingdetails'
   id = Column(Integer, primary_key=True)
   mapping_id = Column(Integer, ForeignKey('mappings.id'))
   column_id = Column(Integer, ForeignKey('userschemacolumns.id'))
   schema_term_id = Column(Integer, ForeignKey('schemaorgterms.id'))
   auto_generated = Column(Boolean, nullable=False)
   curated = Column(Boolean, nullable=False)
   certainty = Column('certainty', Enum(Certainty))
   reasoning = Column('reasoning', String)
   created_at = Column('created_at', String, default=datetime.datetime.utcnow)
   updated_at = Column('updated_at', String, default=datetime.datetime.utcnow)


def init():
    Base.metadata.create_all(engine)