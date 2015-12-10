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

x1 = 550000
x2 = 600000

print "Faixa do Cadastramento : entre: " + str(x1) + " e " + str(x2)  

for x in range(x1, x2):
    myuser = User(name = "user" + str(x),
                email = "mymail" + str(x) + "@udacity.com",
                url_picture = "https://pbs.twimg.com/" + str(x) + "profile_images.png",
                phone_number = "1298861188" + str(x), 
                sex = "Masculino",         
                bio = "Im a Elder, One Engeneer that loves doing things that challeng my capacities. Im 28 years old and my home is SJC",         
                web_page = "https://www.ysh" + str(x) + ".com",   
                city = "São José dos Campos - SP",
                country = "Brasil",
                address = "Rua monte das Oliveiras n:" + str(x),     
                old = "28")
    session.add(myuser)
    #print "add user number" + str(x)

session.commit()


print "added menu items!"