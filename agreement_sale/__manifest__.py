# © 2017 Akretion (Alexis de Lattre <alexis.delattre@akretion.com>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Agreement Sale",
    "summary": "Agreement on sales",
    "version": "20.0.1.0.0",
    "category": "Contract",
    "author": "Akretion, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/agreement",
    "license": "AGPL-3",
    "depends": ["sale_management", "agreement"],
    "data": [
        "views/agreement_view.xml",
        "views/sale_order.xml",
        "security/ir.access.csv",
    ],
    "development_status": "Beta",
    "maintainers": ["alexis-via", "bealdav"],
    "installable": True,
}
