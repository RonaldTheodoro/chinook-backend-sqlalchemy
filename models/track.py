#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlalchemy as sa

from .base import Base


class Track(Base):
    __tablename__ = 'tracks'

    track_id = sa.Column('TrackId', sa.Integer, primary_key=True)
    name = sa.Column('Name', sa.NVARCHAR(200), nullable=False)
    album_id = sa.Column('AlbumId', sa.ForeignKey('albums.AlbumId'), index=True)
    media_type_id = sa.Column(
        'MediaTypeId',
        sa.ForeignKey('media_types.MediaTypeId'),
        nullable=False,
        index=True
    )
    genre_id = sa.Column('GenreId', sa.ForeignKey('genres.GenreId'), index=True)
    composer = sa.Column('Composer', sa.NVARCHAR(220))
    milliseconds = sa.Column('Milliseconds', sa.Integer, nullable=False)
    bytes_size = sa.Column('Bytes', sa.Integer)
    unit_price = sa.Column('UnitPrice', sa.Numeric(10, 2), nullable=False)

    album = sa.orm.relationship('Album')
    genre = sa.orm.relationship('Genre')
    media_type = sa.orm.relationship('MediaType')
