from flask import Flask, render_template

app = Flask(__name__)

# Home Page ka raasta
@app.route('/')
def index():
    return render_template('index.html')

# Admission Page ka raasta
@app.route('/admission')
def admission():
    return render_template('admission.html')

if __name__ == '__main__':
    app.run(debug=True)
  
