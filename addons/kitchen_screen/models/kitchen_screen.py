from odoo import api, fields, models

class KitchenScreen(models.Model):
    _name = 'kitchen.screen'
    _description = 'Pos Kitchen Screen'
    _rec_name = 'sequence'

    def _pos_shop_id(self):
        existing_pos_ids = self.search([]).mapped('pos_config_id').ids
        return [('module_pos_restaurant', '=', True), ('id', 'not in', existing_pos_ids)]

    sequence = fields.Char(
        readonly=True, 
        default='New', 
        copy=False, 
        tracking=True, 
        help="Secuencia de Órdenes"
    )
    
    pos_config_id = fields.Many2one(
        'pos.config',
        string='Punto de Venta Permitido',
        domain=_pos_shop_id, # <--- ¡Añadir esta línea!
        required=True # Considera hacerlo requerido si cada pantalla de cocina debe tener un POS asociado.
    )
    pos_categ_ids = fields.Many2many(
        'pos.category', 
        string='Categorías Permitidas',
        help="Categorías de productos visibles en esta cocina"
    )
    shop_number = fields.Integer(
        related='pos_config_id.id', 
        string='ID del POS',
        store=True,
        help="ID numúrico del punto de venta"
    )

    def kitchen_screen(self):
        return {
            'type': 'ir.actions.act_url',
            'target': 'new',
            'url': f'/pos/kitchen?pos_config_id={self.pos_config_id.id}',
        }

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('sequence', 'New') == 'New':
                vals['sequence'] = self.env['ir.sequence'].next_by_code('kitchen.screen') or 'New'
        return super().create(vals_list)
