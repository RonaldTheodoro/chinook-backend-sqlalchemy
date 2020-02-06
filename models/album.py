#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlalchemy as sa

from .base import Base


class Album(Base):
    __tablename__ = 'albums'

    album_id = sa.Column('AlbumId', sa.Integer, primary_key=True)
    title = sa.Column('Title', sa.NVARCHAR(160), nullable=False)
    artist_id = sa.Column(
        'ArtistId',
        sa.ForeignKey('artists.ArtistId'),
        nullable=False,
        index=True
    )

    artist = sa.orm.relationship('Artist')
