from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index1.html')

history = []

@app.route('/', methods=['POST'])
def calc():

    try:
        op = request.form['text']
        past(op)
        print(history)
        x, y, z = op.split()
        x = float(x)
        z = float(z)
        if y == '+':
            plus = (x+z)
            plus = str(plus)
            return "Ответ: "+plus
        elif y == '-':
            minus = (x-z)
            minus = str(minus)
            return "Ответ: "+minus
        elif y == '*':
            mul = (x*z)
            mul = str(mul)
            return "Ответ: "+mul
        elif y == '/':
            div = (x/z)
            div = str(div)
            return "Ответ: "+div
    except:
        return "Произошла ошибка"

def past(exp):
    history.append(exp)

@app.route('/hist1')
def hist():
    return render_template("hist1.html", history=history)

if __name__ == "__main__":
    app.run(debug=True)