from datetime import datetime
import os



from sqlalchemy import Column, String, Integer, Binary, Table, ForeignKey, Binary, Boolean, DateTime, Unicode, VARCHAR, FLOAT
from flask_admin import form, expose
from flask_admin.contrib.sqla import ModelView

from Obeni import db



file_path = os.path.join(os.path.dirname(__file__), 'static/images/files')



class User(db.Model):
    id = db.Column(Integer, primary_key=True)
    firstname = db.Column(String(30))
    lastname = db.Column(String(30))
    email = db.Column(String(30), unique=True, nullable=False)
    phone = db.Column(Integer())
    profile_image = db.Column(Unicode(150), default='team-4-800x800.jpg')
    password = db.Column(String(255))

    
    def __repr__(self):
        return "<User %r>" % str(self.email)        


class Category(db.Model):
    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(30), unique=True)
    description = db.Column(String())
    created_at = db.Column(DateTime(), default=datetime.now())
    product_id = db.Column(Integer(), db.ForeignKey('product.id'))

    def __repr__(self):
        return "<Category: {}>".format(self.name)


class Customer(db.Model):
    id = db.Column(Integer, primary_key=True)
    order_id = db.relationship('Order', backref='customer', lazy='dynamic')
    firstname = db.Column(String(30))
    lastname = db.Column(String(30))
    email = db.Column(String(30), unique=True)
    phone = db.Column(Integer())
    address = db.Column(String())
    city = db.Column(String())
    location = db.Column(String())
    last_login_ip = db.Column(String())
    current_login_ip = db.Column(String())
    created = db.Column(DateTime(), default=datetime.now())
    
    def __str__(self):
        return self.email



class Product(db.Model):
    id = db.Column(Integer, primary_key=True)
    category_id = db.relationship('Category', backref='category', lazy='dynamic')
    orderitem_id = db.relationship('Orderitem', backref='product', lazy='dynamic')
    name = db.Column(String(80), nullable=False)
    price = db.Column(Integer(), nullable=False)
    image = db.Column(Unicode(150), nullable=False)
    digital = db.Column(Boolean(), default=False)
    added_date = db.Column(DateTime(), default=datetime.now())
    category = db.Column(String(20))
    total = db.Column(Integer, nullable=False)
    description = db.Column(String(250), default='Crafted with superior quality and tailored for a more specific fit')
    
    @property
    def imageUrl(self):
        if not self.image:
            url = ''
            url = form.thumbgen_filename(self.image)
        else:
            return url

    @property
    def get_price(self):
        if not self.price:
            return None
        else:
            return "{:,.0f}".format(self.price)


    def __repr__(self):
        return "<Product %r>" % str(self.name)




class Order(db.Model):
    id = db.Column(Integer(), primary_key=True)
    orderitem_id = db.relationship('Orderitem', backref='order', lazy='dynamic')
    customer_id = db.Column(Integer(), db.ForeignKey('customer.id'))
    total = db.Column(Integer())
    created_at = db.Column(DateTime(), nullable=False, default=datetime.now())
    

    def __repr__(self):
        return "<Order %r>" % str(self.id)


class Orderitem(db.Model):
    id = db.Column(Integer, primary_key=True)
    order_id = db.Column(String(), db.ForeignKey('order.id'))
    products = db.Column(String(200), db.ForeignKey('product.name'))
    quantity = db.Column(Integer())
    date_ordered = db.Column(DateTime(), default=datetime.now())
    size = db.Column(String(5))



    @property
    def get_total(self):
        total = self.quantity * self.product.price
        return total

    @property
    def get_style_total(self):
        return "{:,.1f}".format(self.get_total)

    def __repr__(self):
        return "<Orderitem %r>" % str(self.id)

############# VIEWS ################



class OrderView(ModelView):
    @expose('/list/')
    def list_view(self):
        return self.render('list_order.html')


class AdminView(ModelView):
    # def is_accessible(self):
    #     if not current_user.is_authenticated or not current_user.has_role('admin'):
    #         return False
    #     if current_user.has_role('admin'):
    #         return True
    #     if current_user.has_role('admin'):
    #         return True
        

    #     return False

    # def _handle_view(self, name, **kwargs):
    #     if not self.is_accessible():
    #         if current_user.is_authenticated:
    #             abort(403)
    #         else:
    #             return redirect('/admin/')


    can_export = True
    edit_modal = True
    create_modal = True
    details_modal = True


class ProductAdminView(AdminView):
    def _list_thumbnail(view, context, model, name):
        if not model.image:
            return "Not Found"
        return Markup('<img src="%s">' % url_for('static', filename='Images/files/' + form.thumbgen_filename(model.image)))

        
        
    can_export = False
    can_delete = True
    can_edit = True
    column_formatters = {'image': _list_thumbnail}
    form_extra_fields = {'image': form.ImageUploadField('Image', base_path=file_path, thumbnail_size=(100,100,True)), 'category': form.Select2Field(choices=[('tshirt','Tshirt'),('hoodie','Hoodie')])}