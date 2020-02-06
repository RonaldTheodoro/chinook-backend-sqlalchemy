#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlalchemy as sa

from .base import Base


class Genre(Base):
    __tablename__ = 'genres'

    genre_id = sa.Column('GenreId', sa.Integer, primary_key=True)
    name = sa.Column('Name', sa.NVARCHAR(120))
