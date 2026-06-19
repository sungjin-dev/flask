from flask import Flask, render_template
app = Flask(__name__)

#http://127.0.0.1:5000/
@app.route('/')
def home():
    # return "This page is HOME."
    
    str = 'abcd'
    return render_template('index.html', return_data = str)

#http://127.0.0.1:5000/users
@app.route('/users/')
def users():
    user_list = ['gildong', 'chanho', 'saeri']
    return render_template('users.html', users = user_list)

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')