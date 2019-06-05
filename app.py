from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method =='GET':
        return render_template('login.html')
    else:
        name = request.form.get('name')
        username = request.form.get('username')
        password = request.form.get('password')

        if username == password:
            return render_template('welcome.html', name = name)
        else:
            return 'Invalid credentials! Please try again.'


@app.route('/welcome')
def welcome():
    return render_template('welcome.html')


if __name__ == '__main__':
    app.run(use_reloader = True, debug= True)
