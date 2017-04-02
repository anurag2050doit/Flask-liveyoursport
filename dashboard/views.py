from liveyoursport import app, db
from flask import render_template, redirect, url_for, session, request
from user.decorator import login_required
from dashboard.models import Orders
from dashboard.forms import OrderForm
from datetime import datetime
@app.route('/', methods=('GET','POST'))
@app.route('/index/<int:page>', methods=('GET','POST'))
@login_required
def index(page=1):
    sort = session.get('sort')
    orders = Orders.query.order_by(Orders.order_date.desc()).paginate(page, app.config['POSTS_PER_PAGE'], False)
    if(sort=="order_status"):
        orders = Orders.query.order_by(Orders.order_status.desc()).paginate(page, app.config['POSTS_PER_PAGE'], False)
    elif(sort=="cost_price"):
        orders = Orders.query.order_by(Orders.cost_price.desc()).paginate(page, app.config['POSTS_PER_PAGE'], False)
    elif(sort=="order_date"):
        orders = Orders.query.order_by(Orders.cost_price.desc()).paginate(page, app.config['POSTS_PER_PAGE'], False)
    if request.method == "POST":
        sort = request.form.get('sort')
        session['sort'] = sort
        print sort
        return redirect (url_for('index'))
    return render_template('dashboard/index.html', orders=orders, sort=sort)

@app.route('/add', methods=('GET', 'POST'))
@login_required
def add():
    form = OrderForm()
    error = None
    if form.validate_on_submit():
        order = Orders(
            form.order_id.data,
            form.product_name.data,
            form.order_status.data,
            form.product_url.data,
            float(form.cost_price.data)*66,
            datetime.utcnow()
        )

        db.session.add(order)
        db.session.commit()
        try:
            db.session.commit()
        except:
            error = "There is some error in saving data"
        return redirect(url_for('index'))
    return render_template('dashboard/add.html', form=form, error=error)
