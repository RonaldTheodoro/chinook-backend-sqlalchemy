#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlalchemy as sa

from .base import Base


class Artist(Base):
    __tablename__ = 'artists'

    artist_id = sa.Column('ArtistId', sa.Integer, primary_key=True)
    name = sa.Column('Name', sa.NVARCHAR(120))
