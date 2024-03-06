from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('calculadora.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    operation = request.form['operation']

    if operation == 'add':
        result = num1 + num2
        operator = '+'
    elif operation == 'subtract':
        result = num1 - num2
        operator = '-'
    elif operation == 'multiply':
        result = num1 * num2
        operator = '*'
    elif operation == 'divide':
        if num2 != 0:
            result = num1 / num2
            operator = '/'
        else:
            return "No se puede dividir entre cero!"
    else:
        return "Invalid operation"

    return render_template('resultado.html', num1=num1, num2=num2, operator=operator, result=result)

if __name__ == '__main__':
    app.run(debug=True)
