from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/your-url', methods=['GET', 'POST'])
def your_url():
    urls = {}
    urls[request.form['code']] = {'url': request.form['url']}
    with open('urls.json', 'w') as url_file:
        json.dump(urls, url_file)

    if request.method == 'POST':
        return render_template('your_url.html', code=request.form['code'])
    else: 
        return redirect(url_for('home'))