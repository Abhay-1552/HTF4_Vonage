from flask import Flask, render_template, request
from sms_api_voyage import API

app = Flask(__name__, template_folder='template')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit_form', methods=['GET', 'POST'])
def submit_form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        data = API()
        data.send_sms(name, email, message)
        print(f"Name: {name}, Email: {email}, Message: {message}")

        return render_template('index.html')
    return '', 204


if __name__ == "__main__":
    app.run(debug=True)
