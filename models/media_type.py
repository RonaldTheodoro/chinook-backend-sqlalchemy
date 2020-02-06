#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlalchemy as sa

from .base import Base


class MediaType(Base):
    __tablename__ = 'media_types'

    media_type_id = sa.Column('MediaTypeId', sa.Integer, primary_key=True)
    name = sa.Column('Name', sa.NVARCHAR(120))
