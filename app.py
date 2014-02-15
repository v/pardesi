from flask import Flask, render_template

app = Flask(__name__, static_folder='assets', static_url_path='/assets')

@app.route('/')
def home():
    return render_template('index.html')

app.run(debug=True)
