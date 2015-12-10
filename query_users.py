#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import User, Base, Following, Post, nlike, Comment, Pray, Share

DBpath = "mysql://root:oigalera8458@localhost/catolicosapp_utf8"

print DBpath

####### Nao esquecer de mudar a senha do data base aqui.
engine = create_engine(DBpath)
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

print "######## Ok Lets Go!!!!!!!"

session = DBSession()

x1 = 550000
x2 = 600000

Debug = False

print "Faixa do Query: entre: " + str(x1) + " e " + str(x2)  

# O maior query que consegui foi de 60000 registros
users = session.query(User).filter(User.id > x1, User.id < x2)

if Debug == True:
    for user in users:
        print user.id
        print user.name
        print user.email
        print user.url_picture
        print user.phone_number
        print user.sex
        print user.bio
        print user.web_page
        print user.city
        print user.country 
        print user.address
        print user.old
        print user.current_time
        print "\n"

print "Number of Query"

print users.count()

print "End of Query Puppies"

print "added menu items!"