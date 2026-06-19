import json
import os
import auxTools

class CMService:
    def __init__(self, path = '\\carData.json'):
        self.path = os.getcwd() + path # 주소
        self.data = {}

        if not os.path.exists(self.path):
            self.save('w+')
        if not isinstance(self.data, dict):
            self.save()

        self.load()
                
    def register(self, method='input', **kwargs):

        if method == 'input':
            carNum = input('차량번호를 입력하세요: ')
            carModel = input('차량모델을 입력하세요: ')
            carYear = input('차량연식을 입력하세요: ')

            carNum = auxTools.removeSpace(carNum)

            self.carToData(carNum, carModel, carYear)

        elif method == 'params':
            carNum = kwargs.get('carNum')
            carModel = kwargs.get('carModel')
            carYear = kwargs.get('carYear')
            return self.carToData(carNum, carModel, carYear)

    def check(self, method='input'):
        if method == 'input':
            carNum = input('조회할 차량번호를 입력하세요: ')
            carNum = auxTools.removeSpace(carNum)

            if carNum in self.data:
                auxTools.printWithLine(f'차량번호: {carNum}\n' \
                                    f'차량모델: {self.data[carNum][0]}\n' \
                                    f'차량연식: {self.data[carNum][1]}')
                
            else:
                auxTools.printWithLine('잘못된 차량 정보입니다.', '처음으로 돌아갑니다.')
        
        elif method == 'dict':
            pass

    def modify(self, method='input', **kwargs):
        if method == 'input':
            carNum = input('수정할 차량번호를 입력하세요: ')
            carNum = auxTools.removeSpace(carNum)

            if carNum in self.data:
                carModel = input('차량모델을 입력하세요: ')
                carYear = input('차량연식을 입력하세요: ')
                self.carToData(carNum, carModel, carYear, message='수정이 완료되었습니다.')

        elif method == 'params':
            carNum = kwargs.get('carNum')
            carModel = kwargs.get('carModel')
            carYear = kwargs.get('carYear')
            return self.carToData(carNum, carModel, carYear, message='수정이 완료되었습니다.')

    def delete(self, method='input', **kwargs):
        if method == 'input':
            carNum = input('삭제할 차량번호를 입력하세요: ')
            carNum = auxTools.removeSpace(carNum)

            if carNum in self.data:
                del self.data[carNum]
                auxTools.printWithLine('삭제가 완료되었습니다.', '처음으로 돌아갑니다.')
                self.save()
            else:
                auxTools.printWithLine('잘못된 차량 정보입니다.', '처음으로 돌아갑니다.')

        elif method == 'params':
            carNum = kwargs.get('carNum')
            if carNum in self.data:
                del self.data[carNum]
                self.save()
                return True, '삭제가 완료되었습니다.'
            return False, '잘못된 차량 정보입니다.'

    def carToData(self, carNum, carModel, carYear, message='등록이 완료되었습니다.'):
        if (len(carNum) == 8 and auxTools.isValidText(carNum[3]) and \
            auxTools.convertibleToInt(carNum[4:8]) and auxTools.convertibleToInt(carNum[0:3])) and \
            (len(carModel) >= 1 and auxTools.isValidText(carModel)) and \
            (auxTools.convertibleToInt(carYear) and len(carYear) == 4):
            self.data[carNum] = [carModel, carYear]
            auxTools.printWithLine(message, '처음으로 돌아갑니다.')
            self.save()
            return True, message

        else :
            auxTools.printWithLine('잘못된 차량 정보입니다.', '처음으로 돌아갑니다.')
            return False, '잘못된 차량 정보입니다.'

    def save(self, type_='r+'):
        with open(self.path, type_) as json_file:
            json.dump(self.data, json_file)
            
    def load(self, type_='r+'):
        with open(self.path, type_) as json_file:
            self.data = json.load(json_file)

if __name__ == '__main__':
    ser = CMService()
