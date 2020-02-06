#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlalchemy as sa

from .base import Base


class Employee(Base):
    __tablename__ = 'employees'

    employee_id = sa.Column('EmployeeId', sa.Integer, primary_key=True)
    last_name = sa.Column('LastName', sa.NVARCHAR(20), nullable=False)
    first_name = sa.Column('FirstName', sa.NVARCHAR(20), nullable=False)
    title = sa.Column('Title', sa.NVARCHAR(30))
    reports_to = sa.Column(
        'ReportsTo',
        sa.ForeignKey('employees.EmployeeId'),
        index=True
    )
    birth_date = sa.Column('BirthDate', sa.DateTime)
    hire_date = sa.Column('HireDate', sa.DateTime)
    address = sa.Column('Address', sa.NVARCHAR(70))
    city = sa.Column('City', sa.NVARCHAR(40))
    state = sa.Column('State', sa.NVARCHAR(40))
    country = sa.Column('Country', sa.NVARCHAR(40))
    postal_code = sa.Column('PostalCode', sa.NVARCHAR(10))
    phone = sa.Column('Phone', sa.NVARCHAR(24))
    fax = sa.Column('Fax', sa.NVARCHAR(24))
    email = sa.Column('Email', sa.NVARCHAR(60))

    parent = sa.orm.relationship('Employee', remote_side=[employee_id])
