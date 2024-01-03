# ADAS_CAR
# 1. 거리 유지 2. 차선 유지 3. 차선 변경

class Car:
    def __init__(self):
        self.velocity = 0
        self.accelerate = 0
        self.handle = 0
        self.relativeVelocity = 0
        
    # 엑셀
    def accelerator(self):
        self.accelerate += 1
    
    # 브레이크
    def breaker(self):
        if self.velocity > 1:
            self.accelerate -= 1
        else:
            self.velocity = 0
        
    def updateVelocity(self):
        self.velocity += self.accelerate

    def objectDetection(self):
        pass
    
    # 차선 유지
    def keepLane(self):
        angle = self.getLaneAngle()
        if angle == 0: # 차선과 차량이 평행하면 핸들을 중앙에 위치함
            self.handle = 0
        elif angle > 0: # 차선이 오른쪽으로 치우치면 오른쪽으로 회전함
            self.handle += 1
        else:  # 차선이 왼쪽으로 치우치면 왼쪽으로 회전함
            self.handle -= 1
        
    # 거리 유지
    def keepDistance(self):
        if self.relativeVelocity > 0: # 상대 속도가 0보다 크면 엑셀러레이터를 밟는다.
            self.accelerator()
        elif self.relativeVelocity < 0: # 상대 속도가 0보다 작으면 브레이크를 밟는다.
            self.breaker()
        self.updateVelocity()
 
    
        
    def isThereCarFront(self):
        while self.isThereObject():
            obj, location = self.objectDetection()
            if obj == 'Car' and location == 'Front':
                return True
        return False
        
    def isThereObject(self):
        pass
        
    #RANSAC 알고리즘 -> 차선 인식 -> 차와 차선의 각도 구하기
    def getLaneAngle(self):
        pass

    #라이다로부터 거리 재기     
    def getDistance(self):
        pass 

    def objectDetection(self):
        return obj, location


        
car = Car()
        
while(True):
    if car.isThereCarFront():
        car.getDistance()
        car.keepDistance() # 거리 유지
    else:
        pass
    car.keepLane() # 차선 유지