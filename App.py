from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = "Secret Key"
 

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/crud'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
db = SQLAlchemy(app)

class Data(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))
    product = db.Column(db.String(100))
    color = db.Column(db.String(100))
    size = db.Column(db.String(100))
    price = db.Column(db.String(100))


 
    def __init__(self , name, email, phone , product , color , size , price  ):
 
        self.name = name
        self.email = email
        self.phone = phone
        self.product = product
        self.color = color
        self.size = size
        self.price = price



@app.route('/')
def index():
    all_data = Data.query.all()
    return render_template("index.html", products = all_data)


@app.route('/insert' , methods = ['POST'])
def insert():

    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        product = request.form['product']
        color = request.form['color']
        size = request.form.get('size')
        price = request.form.get('price')

        my_data = Data(name, email, phone, product, color, size, price)
        db.session.add(my_data)
        db.session.commit()

        flash("Employee Updated Successfully")

        return redirect(url_for('index'))


@app.route('/update', methods = ['GET', 'POST'])
def update():

    if request.method == 'POST':
        my_data = Data.query.get(request.form.get('id'))
 
        my_data.name = request.form['name']
        my_data.email = request.form['email']
        my_data.phone = request.form['phone']
        my_data.product = request.form['product']
        my_data.color = request.form['color']
        my_data.size = request.form['size']
        my_data.price = request.form['price']
 
        db.session.commit()
        flash("Product Updated Successfully")
 
        return redirect(url_for('index'))

@app.route('/delete/<id>/', methods = ['GET', 'POST'])
def delete(id):
    my_data = Data.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Product Deleted successfully") 

    return redirect(url_for('index'))       


if __name__ == "__main__":
    app.run(debug=True)