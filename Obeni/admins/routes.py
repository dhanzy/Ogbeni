from flask import Blueprint, render_template
from flask_admin.contrib.sqla import ModelView

from Obeni import admin, db
from Obeni.model import Customer, Product, ProductAdminView, OrderView, Order


admins = Blueprint('admins', __name__)


admin.add_view(ModelView(Customer, db.session, menu_icon_type='fa', menu_icon_value='users'))
admin.add_view(ProductAdminView(Product, db.session, menu_icon_type='fa', menu_icon_value='box'))
# admin.add_view(OrderView())
