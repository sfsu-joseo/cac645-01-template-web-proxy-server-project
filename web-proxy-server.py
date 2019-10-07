from flask import Flask
from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)


@app.route('/')
def home():
   return render_template('home.html')

@app.route('/proxy-settings')
def proxy_settings():
    return render_template('proxy-settings.html')

if __name__ == '__main__':
    app.run()
