from flask import Flask, render_template, request
from flask_mail import Mail
from flask_mail import Message

app = Flask(__name__)
app.config['MAIL_SERVER']='http://mail.mailkitchen.com/'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'uriel_monsivais@hotmial.com'
app.config['MAIL_PASSWORD'] = 'monsivaismireles'
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
                  sender="contacto.sasit.red",
                  recipients=[request_c['mail']])        
        msg.body = "Nuevo correo: "+request_c['mail']
        mail.send(msg)
    except ValueError:
        print("Email error")
        print(ValueError)
    return render_template('index.html')