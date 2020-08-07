from flask import Flask, render_template, request
from flask_mail import Mail
from flask_mail import Message
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



app = Flask(__name__)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'monsivaisuriel28@gmail.com'
app.config['MAIL_PASSWORD'] = 'hpqgwjliswijqrwb'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost:3306/db_sait'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signin')
def signin():
    return render_template('signin.html')

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/contact', methods=['POST'])
def contact():
    request_c = request.form
    try:
        msg = Message("New request",
                  sender="monsivaisuriel28@gmail.com",
                  recipients=["uriel.monsivais@sait.red"])
        mailBody = """ 
        Hola, nuevo correo de {0}.

        Datos:

            Nombre: {1}
            Telefono: {2}
            Numéro de empleados: {3}
            Servicios de interes: {4} 
        
        """.format(request_c['mail'],request_c['name'],request_c['phone'],request_c['employees'],request_c['services'])
        msg.body = mailBody
        mail.send(msg)
    except ValueError:
        print("Email error")
        print(ValueError)
    return render_template('index.html')

class Company(db.Model):
    __tablename__ = 'companies'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    admin = db.Column(db.String(100), nullable=False)
    users = db.Column(db.String(256), nullable=False)
    creation = db.Column(db.String(256), nullable=False)
    image = db.Column(db.String(256), nullable=False)

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit();
