#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlalchemy as sa

from .base import Base


class Invoice(Base):
    __tablename__ = 'invoices'

    invoice_id = sa.Column('InvoiceId', sa.Integer, primary_key=True)
    customer_id = sa.Column(
        'CustomerId',
        sa.ForeignKey('customers.CustomerId'),
        nullable=False,
        index=True
    )
    invoice_date = sa.Column('InvoiceDate', sa.DateTime, nullable=False)
    billing_address = sa.Column('BillingAddress', sa.NVARCHAR(70))
    billing_city = sa.Column('BillingCity', sa.NVARCHAR(40))
    billing_state = sa.Column('BillingState', sa.NVARCHAR(40))
    billing_country = sa.Column('BillingCountry', sa.NVARCHAR(40))
    billing_postal_code = sa.Column('BillingPostalCode', sa.NVARCHAR(10))
    total = sa.Column('Total', sa.Numeric(10, 2), nullable=False)

    customer = sa.orm.relationship('Customer')
