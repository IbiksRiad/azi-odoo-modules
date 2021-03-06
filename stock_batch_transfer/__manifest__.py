# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP Module
#    
#    Copyright (C) 2014 Asphalt Zipper, Inc.
#    Author Matt Taylor

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
    "name": "stock_batch_transfer",
    "version": "10.0.0.1",
    "summary": "Stock Batch Transfer",
    "category": "Inventory Control",
    "author": "Matt Taylor",
    "website": "http://www.asphaltzipper.com",
    'description': """
Validate a batch of internal transfers
=========================================

* Automatically set done quantity same as required quantity
* Only allow Internal Transfer type.
* Only allow Available pickings.
* Only allow totally incomplete picking lines.
* Skip transfers requiring serial numbers.
* Skip transfers requiring quality checks.
    """,
    "depends": ['product', 'stock'],
    'data': [
        'views/stock_picking_views.xml',
    ],
    "installable": True,
    "auto_install": False,
}
