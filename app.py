# importo a Classe Flask do módulo flask

from flask import Flask, render_template

# Crio o abjecto app

app = Flask(__name__)

# usando 'decorators' para colegar a função a uma URL

@app.route('/')
def index():
    return render_template('index.html') # O template 

@app.route('/sobre')
def sobre():
    return render_template('index.html#sobre') # O template 

@app.route('/produtos')
def produtos():
    return render_template('index.html#produtos') # O template 

@app.route('/contato')
def contato():
    return render_template('index.html#contato') # O template 

# iniciando o servidor comm o método 'run()'
if __name__ == '__main__':
    app.run(debug=True)




