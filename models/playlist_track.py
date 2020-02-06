#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlalchemy as sa

from .base import metadata


PlaylistTrack = sa.Table(
    'playlist_track',
    metadata,
    sa.Column(
        'PlaylistId',
        sa.ForeignKey('playlists.PlaylistId'),
        primary_key=True,
        nullable=False
    ),
    sa.Column(
        'TrackId',
        sa.ForeignKey('tracks.TrackId'),
        primary_key=True,
        nullable=False,
        index=True
    )
)
