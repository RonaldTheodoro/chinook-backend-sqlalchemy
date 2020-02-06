#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlalchemy as sa

from .base import Base


class Customer(Base):
    __tablename__ = 'customers'

    customer_id = sa.Column('CustomerId', sa.Integer, primary_key=True)
    first_name = sa.Column('FirstName', sa.NVARCHAR(40), nullable=False)
    last_name = sa.Column('LastName', sa.NVARCHAR(20), nullable=False)
    company = sa.Column('Company', sa.NVARCHAR(80))
    address = sa.Column('Address', sa.NVARCHAR(70))
    city = sa.Column('City', sa.NVARCHAR(40))
    state = sa.Column('State', sa.NVARCHAR(40))
    country = sa.Column('Country', sa.NVARCHAR(40))
    postal_code = sa.Column('PostalCode', sa.NVARCHAR(10))
    phone = sa.Column('Phone', sa.NVARCHAR(24))
    fax = sa.Column('Fax', sa.NVARCHAR(24))
    email = sa.Column('Email', sa.NVARCHAR(60), nullable=False)
    support_rep_id = sa.Column(
        'SupportRepId',
        sa.ForeignKey('employees.EmployeeId'),
        index=True
    )

    employee = sa.orm.relationship('Employee')
