from flask import Flask


app = Flask(__name__)

# Задание 1: Простые маршруты
@app.route("/hello")
def hello():
    return 'hello, world!'

@app.route('/info')
def info():
    return 'this is an informational page'

# Задание 2: Динамические маршруты
@app.route('/calc/<num1>/<num2>')
def find_sum(num1, num2):
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        return "error: please enter numeric values ​​(integer or floating point)"
    return f'the sum of {num1} and {num2} is {num1 + num2}'

# Задание 3. Создайте маршрут /reverse/, который переворачивает текст
@app.route('/reverse/<text>')
def reverse(text):
    if len(text.strip()) > 0:
        return text[::-1]
    raise TypeError('please enter at least one character')

# Задание 4. Реализуйте маршрут /user//
@app.route('/user/<name>/<int:age>')
def greet_user(name, age):
    if age > 0 and age < 120:
        return f'hello, {name}. you are {age} yo. cooooool!!!!!!!!'
    return 'please enter the correct age'


if __name__ == "__main__":
    app.run(debug=True)