from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os.path

app = Flask(__name__)
app.secret_key = 'lslsknljnjdjjdljgndl'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/your-url', methods=['GET', 'POST'])
def your_url():
    urls = {}
    if os.path.exists('urls.json'):
        with open('urls.json') as url_file:
            urls = json.load(url_file)
    if request.form['code'] in urls:
        flash('That shortname has already taken. Please select another one.')
        return redirect(url_for('home'))


    urls[request.form['code']] = {'url': request.form['url']}
    with open('urls.json', 'w') as url_file:
        json.dump(urls, url_file)

    if request.method == 'POST':
        return render_template('your_url.html', code=request.form['code'])
    else: 
        return redirect(url_for('home'))