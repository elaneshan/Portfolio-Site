import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

#add list of page data here so all pages can use
all_pages = [
        ("Home", "/"),
        ("Hobbies", "/hobbies"),
    ]
#pass it as an arg for rendering
@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"), nav_links=all_pages)
@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html', title="Hobbies", nav_links=all_pages)