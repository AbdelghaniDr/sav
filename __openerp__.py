# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': "SAV",
    'version': "1.0",
    'author': "Ait-Mlouk addi /INFOSIT R&B",
    'category': 'Customer Relationship Management',
    'description': """

Manage Customer Claims.
=======================
This application allows you to track your customers/suppliers claims and grievances.

It is fully integrated with the email gateway so that you can create
automatically new claims based on incoming emails.
    """,
    'depends': ['base','crm_claim','product'],
    'data': [ 
             'security/sav_security.xml',
             'sav.xml',
             'sav_sequence.xml',
             ],
    'demo': [],
    'installable': True,
    
    
    
}
