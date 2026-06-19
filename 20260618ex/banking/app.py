from flask import Flask, render_template, request
from blueprints.member.routes import bank_bp

app = Flask(__name__)

app.secret_key = 'saujfhksdhfkjaskldjsakl'

app.register_blueprint(bank_bp)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

     

                      

                                            