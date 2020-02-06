#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlalchemy as sa

from .base import Base


class InvoiceItem(Base):
    __tablename__ = 'invoice_items'

    invoice_line_id = sa.Column('InvoiceLineId', sa.Integer, primary_key=True)
    invoice_id = sa.Column(
        'InvoiceId',
        sa.ForeignKey('invoices.InvoiceId'),
        nullable=False,
        index=True
    )
    track_id = sa.Column(
        'TrackId',
        sa.ForeignKey('tracks.TrackId'),
        nullable=False,
        index=True
    )
    unit_price = sa.Column('UnitPrice', sa.Numeric(10, 2), nullable=False)
    quantity = sa.Column('Quantity', sa.Integer, nullable=False)

    invoice = sa.orm.relationship('Invoice')
    track = sa.orm.relationship('Track')
