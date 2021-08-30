from flask import render_template
from app import app

from app.models.forms import LoginForm

@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html',
                           form=form)

@app.route("/base")
def base():
    return render_template('base.html')








@app.route("/test")
@app.route("/test/<name>")
def test(name=None):
    if name:
        return "Ola, %s!" %name
    else:
        return "Olá, usuário!"

@app.route("/test_2/<int:id>", methods=['GET'])   #limita a página somente ao método GET do HTTP
def test_2(id):
    print(type(id))                               #this two values will be print in the termminal
    print(id)                                     
    return ""                                     #the route must always return something, even if it is void 


@app.route("/test_3")
def test_3():
    return """
    
    <html>
    <head>
        <title>Teste 3</title>
    </head>
    <body>
        <h1>Teste 3, funcionando apenas com html!</h1>
    </body>
    </html>
    
    """


@app.route("/example", defaults={"user":None})
@app.route("/example/<user>")
def example(user):
    return render_template('example.html',
                           user=user
                           )