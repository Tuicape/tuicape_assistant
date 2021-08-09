#           base func   using template (html), template (css)
from flask import Flask, render_template, url_for
from flask import request

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import os

#create server
app = Flask(__name__)

#create folder template, default "templates"
#template of styles (js and css files, png ect.) - folder 'static'
#template inheritance
#to create template using structure {% block name_block %}{% endblock %}
#to inheritance all use structure {% extends 'base.html' %}
#to inheritance block use {% block title %}some data{% endblock %}

#create decorator
#if you go to this page
@app.route("/")
@app.route("/home")
def index():
    #show on main window
    #in defaul directory open page index.html
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/download", methods=['GET', 'POST'])
def download():
    return render_template("download.html")

@app.route('/download_button()')
def download_button():
    count = str(int(open('downloads.txt').read())+1)
    open('downloads.txt', 'w', encoding='utf-8').write(count)
    open(os.getcwd() + '\\templates\\download_final.html', 'w', encoding='utf-8').write('''{% extends 'base.html' %}

{% block title %}
Скачать Tuicape assistant
{% endblock %}

{% block body %}
<br>
<section class="download padding site">
    <h2 id="adownload" >Всё готово к скачиванию!</h2>
    <div>
        <br><p>Скачиваний:''' + count + '''</p><br>
        <a href="#" download="setup.exe" title="Скачать" class="download_box3"><img src="{{ url_for('static', filename='css/download.gif') }}" alt="Скачать" height=300, width=250></a>
    </div>
</section>
{% endblock %}
''')
    return render_template("download_final.html")

@app.route("/help")
def help():
    return render_template("help.html")

@app.route("/support")
def support():
    return render_template("support.html")

@app.errorhandler(404)
def page_not_find(e):
    return render_template("page_not_found.html")

#if file started
if __name__ == "__main__":
    #stat server
    #errors sended on site  free hosting
    app.run(host='192.168.0.104', port=5000, debug=True)