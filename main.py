from flask import Flask, app, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/stock')
def stock():
    return render_template('stockstats.html')




if __name__ == '__main__':
    app.run(debug=True)
