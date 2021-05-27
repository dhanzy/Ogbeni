

from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_user, logout_user


from Obeni.forms import ShippingForm, LoginForm

main = Blueprint('main', __name__)



@main.route('/admin/logout/')
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@main.route('/admin/login/', methods=['POST','GET'])
def login():
    form = LoginForm()
    return render_template('admin/login.html', form=form)

@main.route('/checkout/')
def checkout():
    form = ShippingForm()
    return render_template('checkout.html', form=form)


@main.route('/cart/')
def cart():
    return render_template('cart.html')


@main.route('/product/')
def product():
    return render_template('product.html')

@main.route('/collection/')
def collection():
    return render_template('collection.html')

@main.route('/women/')
def women():
    return render_template('collection.html')


@main.route('/men/')
def men():
    return render_template('collection.html')

@main.route('/')
def index():
    return render_template('index.html')