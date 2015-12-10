from sqlalchemy import Column, ForeignKey, Integer, String, Unicode, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.mysql import TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

from datetime import datetime
from sqlalchemy.sql import func

from sqlalchemy.dialects.mysql import INTEGER

import sqlalchemy

Base = declarative_base()

DBpath = "mysql://root:oigalera8458@localhost/catolicosapp_utf8"

engine = sqlalchemy.create_engine('mysql://root:oigalera8458@localhost')

#engine.execute("CREATE DATABASE catolicosapp_utf8 CHARACTER SET utf8 COLLATE utf8_general_ci")

class User(Base):
	__tablename__ = 'user'
	id 				= Column(Integer, primary_key=True)
	name 			= Column(Unicode(250, collation='utf8_bin'), nullable=False)
	email 			= Column(Unicode(250, collation='utf8_bin'), nullable=False)
	url_picture 	= Column(Unicode(250, collation='utf8_bin'))
	phone_number 	= Column(Unicode(250, collation='utf8_bin'))
	sex 			= Column(Unicode(250, collation='utf8_bin'))
	bio 			= Column(Unicode(250, collation='utf8_bin'))
	web_page 		= Column(Unicode(250, collation='utf8_bin'))
	city 			= Column(Unicode(250, collation='utf8_bin'))
	country 		= Column(Unicode(250, collation='utf8_bin'))
	address 		= Column(Unicode(250, collation='utf8_bin'))
	old 			= Column(Unicode(250, collation='utf8_bin'))

	@property
	def serialize(self):
		"""Return object data in easily serializeable format"""
		return {
			'name'	: self.name,
			'id'	: self.id,
		}


class Following(Base):
	__tablename__ = 'following'
	id 					= Column(Integer, primary_key=True)
	user_id 			= Column(Integer,ForeignKey('user.id'))
	following_user_id 	= Column(Integer,ForeignKey('user.id'))
	current_time 		= Column(TIMESTAMP, server_default= func.now(), onupdate=func.current_timestamp())


class Post(Base):
	__tablename__ = 'post'
	id 					= Column(Integer, primary_key=True)
	user_id 			= Column(Integer,ForeignKey('user.id'))
	post_current_time 	= Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp())
	post_text 			= Column(Unicode(250, collation='utf8_bin'))
	post_url_picture 	= Column(Unicode(250, collation='utf8_bin'))
	post_url_video 		= Column(Unicode(250, collation='utf8_bin'))


class nlike(Base):
	__tablename__ = 'nlike'
	id 					= Column(Integer, primary_key=True)
	user_id 			= Column(Integer,ForeignKey('user.id'))
	post_id 			= Column(Integer,ForeignKey('post.id'))
	like_current_time 	= Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp())


class Comment(Base):
	__tablename__ = 'comment'
	id 						= Column(Integer, primary_key=True)
	user_id					= Column(Integer,ForeignKey('user.id'))
	post_id					= Column(Integer,ForeignKey('post.id'))
	comment_text            = Column(Unicode(250, collation='utf8_bin'))
	comment_current_time 	= Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp())


class Pray(Base):
	__tablename__ = 'pray'
	id 					= Column(Integer, primary_key=True)
	user_id 			= Column(Integer,ForeignKey('user.id'))
	post_id 			= Column(Integer,ForeignKey('post.id'))
	pray_current_time 	= Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp())


class Share(Base):
	__tablename__ = 'share'
	id 					= Column(Integer, primary_key=True)
	user_id 			= Column(Integer,ForeignKey('user.id'))
	post_id 			= Column(Integer,ForeignKey('post.id'))
	share_current_time 	= Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp())

engine = create_engine(DBpath)

Base.metadata.create_all(engine)


