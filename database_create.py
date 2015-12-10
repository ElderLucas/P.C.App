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

engine.execute("CREATE DATABASE catolicosapp_utf8 CHARACTER SET utf8 COLLATE utf8_general_ci")