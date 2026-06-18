from flask import Flask, render_template, request
from blueprints.member.routes import member_bp

app = Flask(__name__)

app.secret_key = 'saujfhksdhfkjaskldjsakl'
# 쿠키 위변조 방지 

app.register_blueprint(member_bp)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

# python -m venv (폴더명)    
 
# keydown                                                                                          