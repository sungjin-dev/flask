from flask import Flask, render_template, request
from blueprints.bank.routes import bank_bp


app = Flask(__name__)

app.secret_key = 'saujfhksdhfkjaskldjsakl'

session['signinedMemberId'] = 'user123'

app.register_blueprint(bank_bp)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

     

                      

                                            