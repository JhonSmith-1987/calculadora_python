from flask import Flask, render_template, redirect, url_for, request

from models.Operations import Operation

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('calculadora.html')


@app.route('/operation', methods=['POST'])
def operation():
    if request.method == 'POST':
        value_one = int(request.form['value_one'])
        operation = request.form['operation']
        value_two = int(request.form['value_two'])
        if operation == 'suma':
            value = Operation.suma(value_one, value_two)
            result = f'{value_one} + {value_two} = {value}'
            return render_template('result.html', result=result)
        elif operation == 'resta':
            value = Operation.resta(value_one, value_two)
            result = f'{value_one} - {value_two} = {value}'
            return render_template('result.html', result=result)
        elif operation == 'multiplicacion':
            value = Operation.multiplicar(value_one, value_two)
            result = f'{value_one} * {value_two} = {value}'
            return render_template('result.html', result=result)
        else:
            value = Operation.dividir(value_one, value_two)
            result = f'{value_one} / {value_two} = {value}'
            return render_template('result.html', result=result)


@app.route('/result')
def result():
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
