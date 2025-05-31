from odoo import api, fields, models


class KitchenScreen(models.Model):
    """Kitchen Screen model for the cook"""
    _name = 'kitchen.screen'
    _description = 'Pos Kitchen Screen'
    _rec_name = 'sequence'

    def _pos_shop_id(self):
        """Domain for the Pos Shop"""
        kitchen = self.search([])
        if kitchen:
            return [('module_pos_restaurant', '=', True),
                    (
                    'id', 'not in', [rec.id for rec in kitchen.pos_config_id])]
        else:
            return [('module_pos_restaurant', '=', True)]

    sequence = fields.Char(readonly=True, default='New',
                           copy=False, tracking=True, help="Sequence of items")
    pos_config_id = fields.Many2one('pos.config', string='Allowed POS',
                                    domain=_pos_shop_id,
                                    help="Allowed POS for kitchen")
    pos_categ_ids = fields.Many2many('pos.category',
                                     string='Allowed POS Category',
                                     help="Allowed POS Category"
                                          "for the corresponding Pos")
    shop_number = fields.Integer(related='pos_config_id.id', string='Customer',
                                 help="Id of the POS")

    def kitchen_screen(self):
        """Redirect to corresponding kitchen screen for the cook"""
        return {
            'type': 'ir.actions.act_url',
            'target': 'new',
            'url': '/pos/kitchen?pos_config_id= %s' % self.pos_config_id.id,
        }

    @api.model
    def create(self, vals_list):
        """Used to create sequence in batch-compatible way"""
        # Asegurarse de que vals_list sea siempre una lista de diccionarios
        # Odoo pasa una lista por defecto, pero es una buena práctica de compatibilidad
        if isinstance(vals_list, dict):
            vals_list = [vals_list]

        # Procesar cada diccionario en la lista
        for vals in vals_list:
            if vals.get('sequence', 'New') == 'New':
                vals['sequence'] = self.env['ir.sequence'].next_by_code(
                    'kitchen.screen')
        
        # Llamar al método create original del padre (Odoo) con la lista modificada
        records = super(KitchenScreen, self).create(vals_list)
        return records