import requests

class SDCar:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.left = 0
        self.right = 0
    def getStatus(self):
        return "SDCar: " + self.ip + ":" + str(self.port)
    def getMotorStatus(self):
        return {"left": self.left, "right":  self.right}
    def setLeftMotor(self, value):
        req = requests.get("http://" + self.ip + ":" + str(self.port) + "/left/set/" + str(value))
        self.left = req.json()["value"]
        if req.json()["success"] == True:
            return True
        else:
            return False
    def setRightMotor(self, value):
        req = requests.get("http://" + self.ip + ":" + str(self.port) + "/right/set/" + str(value))
        self.right = req.json()["value"]
        if req.json()["success"] == True:
            return True
        else:
            return False
    def brake(self):
        req = requests.get("http://" + self.ip + ":" + str(self.port) + "/all/brake")
        if req.json()["success"] == True:
            return True
        else:
            return False
    def forward(self, value):
        req = requests.get("http://" + self.ip + ":" + str(self.port) + "/all/forward/" + str(value))
        if req.json()["success"] == True:
            return True
        else:
            return False
