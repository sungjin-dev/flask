from flask import Flask, render_template, request, redirect, url_for, flash
from carManageService import CMService
import os

app = Flask(__name__)
app.secret_key = 'car_manage_secret'
service = CMService()

@app.route('/')
def index():
    return render_template('index.html', cars=service.data)

@app.route('/register', methods=['POST'])
def register():
    carNum = request.form.get('carNum')
    carModel = request.form.get('carModel')
    carYear = request.form.get('carYear')
    
    # 이미 존재하는 차량이면 수정, 아니면 등록 메시지 처리
    is_edit = carNum in service.data
    msg = '수정되었습니다.' if is_edit else '등록이 완료되었습니다.'
    
    success, message = service.carToData(carNum, carModel, carYear, message=msg)
    flash(message, 'success' if success else 'danger')
    return redirect(url_for('index'))

@app.route('/delete/<carNum>')
def delete(carNum):
    success, message = service.delete(method='params', carNum=carNum)
    flash(message, 'success' if success else 'danger')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)