from flask import Flask, render_template
from routes import init_app

app = Flask(__name__)

# Initialize the blueprints
init_app(app)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
