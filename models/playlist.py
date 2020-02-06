#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlalchemy as sa

from .base import Base


class Playlist(Base):
    __tablename__ = 'playlists'

    playlist_id = sa.Column('PlaylistId', sa.Integer, primary_key=True)
    name = sa.Column('Name', sa.NVARCHAR(120))

    tracks = sa.orm.relationship('Track', secondary='playlist_track')
