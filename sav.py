# -*- coding: utf-8 -*-
##############################################################################
# v2.0
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
from openerp.addons.base_status.base_stage import base_stage
import binascii 
from openerp.addons.crm import crm 
from openerp.osv import fields, osv 
import time 
from openerp import tools 
from openerp.tools.translate import _ 
from openerp.tools import html2plaintext 
from bzrlib.errors import ReadOnlyError

class sav(osv.osv):
    _inherit = 'crm.claim'
    
    
    def create(self, cr, user, vals, context=None):
        if ('n_reclamation' not in vals) or (vals.get('n_reclamation')=='/'):
            vals['n_reclamation'] = self.pool.get('ir.sequence').get(cr, user, 'crm.claim')
        return super(sav, self).create(cr, user, vals, context)
    

    _columns = {
        'n_reclamation': fields.char('N reclamation'),
        'company_id1': fields.many2one('res.company', 'Societe Client'),
        'partner_id1': fields.many2one('res.partner', 'Client'),
        'email_from1': fields.char('Email client', size=128, help="Destination email for email gateway."),
		'partner_phone1': fields.char('Phone client', size=32),
        'street01': fields.char('Address client', size=128),
        'city1': fields.char('Ville client', size=128),
		'company_id2': fields.many2one('res.company', 'Societe Distributeur'),
        'partner_id2': fields.many2one('res.partner', 'Distributeur'),
        'email_from2': fields.char('Email Distributeur', size=128, help="Destination email for email gateway."),
		'partner_phone2': fields.char('Phone Distributeur', size=32),
		'company_id3': fields.many2one('res.company', 'Societe Revendeur'),
        'partner_id3': fields.many2one('res.partner', 'Revendeur'),
        'email_from3': fields.char('Email Revendeur', size=128, help="Destination email for email gateway."),
		'partner_phone3': fields.char('Phone Revendeur', size=32),
		'produit': fields.many2one('product.product', 'Prouduit'),
		'Modele': fields.char('Model Produit', size=64),
		'date_achat': fields.datetime('Date Achat'),
		'Desc': fields.text('description pane '),   
        'Marque' : fields.many2one('product.marque', 'Marque'),
		'Serial': fields.char('N de serie', size=64),
		'File_upload': fields.binary ("Bonne d'achat"),
        'product_ids': fields.many2many('product.product','product_equipment_rel','product_id','equipment_id','Piece of change'),
	}

    _defaults = {
        'n_reclamation': lambda self, cr, uid, context: '/',   
        
	}
    
    
    
    def onchange_partner_id1(self,cr,uid,ids,part,context={}):
        data = {}
        if part:
            data_sav_model = self.pool.get('res.partner').read(cr,uid,part,['phone','street','city'])
            if data_sav_model:
                data ['partner_phone1'] = data_sav_model['phone']
                data ['street01'] = data_sav_model['street']
                data ['city1'] = data_sav_model['city']
        return {'value' : data }
    
	
    def onchange_partner_id2(self,cr,uid,ids,part,context={}):
        data = {}
        if part:
            data_sav_model = self.pool.get('res.partner').read(cr,uid,part,['email','phone'])
            if data_sav_model:
                data ['email_from2'] = data_sav_model['email']
                data ['partner_phone2'] = data_sav_model['phone']
        return {'value' : data }
		
    
    def onchange_partner3(self,cr,uid,ids,part,context={}):
        data = {}
        if part:
            data_sav_model = self.pool.get('res.partner').read(cr,uid,part,['email','phone'])
            if data_sav_model:
                data ['email_from3'] = data_sav_model['email']
                data ['partner_phone3'] = data_sav_model['phone']
        return {'value' : data }
    

class res_partner1(osv.osv):
    _inherit = 'res.partner'
    _columns = {
        'claims_ids': fields.one2many('crm.claim', 'partner_id1', 'Claims'),
    }
class res_partner2(osv.osv):
    _inherit = 'res.partner'
    _columns = {
        'claims_ids': fields.one2many('crm.claim', 'partner_id2', 'Claims'),
    }
class res_partner3(osv.osv):
    _inherit = 'res.partner'
    _columns = {
        'claims_ids': fields.one2many('crm.claim', 'partner_id3', 'Claims'),
    }
sav()
