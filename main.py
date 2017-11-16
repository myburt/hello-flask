from flask import Flask, request, redirect
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader= jinja2.FileSystemLoader
(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

time_form = """
    <style>
        .error{{color: red}}
    </style>
    <h1>Validate Time</h1>
    <form method="POST">
        <label>Hours (24-Hour format)
            input name="hours" type="text" value"{hours}"
        </label>
        <p class="error">{hours_error}</p>
        <label>Minutes
            input name="minutes" type="text" value"{minutes}"
        </label>
        <p class="error">{munutes_error}</p>
        <input type="submit" value="Validate"/>
    </form>
"""

@app.route("/")
def index():
    template = jinja_env.get_template('hello_form.html')
    return template.render()

@app.route("/hello", methods=['POST'])
def hello():
    first_name = request.form['first_name']
    template = jinja_env.get_template('hello_greeting.html')
    return template.render(name = first_name)

app.run()