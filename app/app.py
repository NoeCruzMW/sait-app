from flask import Flask, render_template, request
from flask_mail import Mail
from flask_mail import Message

app = Flask(__name__)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'monsivaisuriel28@gmail.com'
app.config['MAIL_PASSWORD'] = 'hpqgwjliswijqrwb'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


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