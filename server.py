# In the command prompt, input - python3 -m venv webDevelopment
# In the command prompt, input - webDevelopment\Scripts\activate.bat
# In the command prompt, input - set FLASK_APP = server.py
# In the command prompt, input - set FLASK_ENV = development
## In the command prompt, input - flask run

from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('welcome.html')

@app.route('/welcome.html')
def my_home2():
    return render_template('welcome.html')

@app.route('/index.html')
def my_home3():
    return render_template('welcome.html')

@app.route('/home.html')
def my_home4():
    return render_template('welcome.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f"\n{email}, {subject},{message}")

def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong'

