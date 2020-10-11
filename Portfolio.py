from flask import Flask, render_template, send_from_directory, url_for, request, redirect
import csv
# GitHub password: b4be5a780439e87c6799a3162ed4def56698f916
# Terminal:
# go to the desig path
# git clone (copy&paste Git clone ssh or https)
# git cd portfolio
# git add .
# git commit -m"message"
# git push origin master
# PythonAnywhere:
# Console -> bash: git clone ()
    # cd portfolio\ project
    # mkvirtualenv --python=/usr/bin/python{version number} my-virtualenv{ or name}
    # pip3 install flask
    # workon my-virtualenv
    # cd portfolio\ project
    # pip3 install -r requirements.txt
# check up on 10/11/2020
app = Flask(__name__)
print(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


# @app.route('/index.html')
# def main_page(username=None, post_id=None):
#     return render_template('index.html')
# print(url_for('static', filename='favicon.ico'))

# @app.route('/about.html')
# def hello_thighs():
#     return render_template('about.html')
#
# @app.route('/works.html')
# def works():
#     return render_template('works.html')
# @a.pp.route('/work.html')
# def work():
#     return render_template('work.html')
# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')
@app.route('/<string:page_name>')  # lines 11-27 can be replaced with this
def html_page(page_name):
    return render_template(page_name)
    # error = None
    # if request.method == 'POST':
    #     if valid_login(request.form['username'], request.form['password']):
    #         return log_the_user_in(request.form['username'])
    #     else:
    #         error = 'Invalid username/password'
    #         # the code below is executed if the request method
    #         # was GET or the credentials were invalid
    #         return render_template('login.html', error=error)
    #         return 'Form has been submitted'


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email}, {subject}, {message}')


def write_to_csv(data):
    with open("database.csv", newline='', mode="a") as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=",", quotechar="'", quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            print(data)
            return redirect('/contactreply.html')

        except:
            return 'Could not be uploaded to the database'
    else:
        return 'Something went wrong. Try again.'
# @app.route('/upload', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         f = request.files['the_file']
#         f.save('/var/www/uploads/uploaded_file.txt')


# @app.route('/favicon1.ico')
# def favicon():
#     return 'here\'s the icon'

# @app.add_url_rule('/favicon1.ico', redirect_to=url_for('static', filename='favicon1.ico'))


# 'python3 -m venv {name of the server; ex. web server}' to make a venv
# to activate the venv, '. {name}/bin/activate'
# use 'python3 -m flask run' if 'flask run' does not work
