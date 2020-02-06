#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlalchemy as sa

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

import decouple


Base = declarative_base()

metadata = Base.metadata

DATABASE_URL = decouple.config('DATABASE_URL')


def get_session():
    return scoped_session(sessionmaker(bind=get_db_engine()))


def get_db_engine():
    return sa.create_engine(DATABASE_URL)


session = get_session()
