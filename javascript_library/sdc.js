// THIS VERSION IS MADE FOR A WEB BROWSER

class SDCar {
    constructor(ip, port) {
        this.ip = ip;
        this.port = port;
        this.left = 0
        this.right = 0
    }
    getStatus() {
        return "SDCar: " + this.ip + ":" + this.port
    }
    getMotorStatus() {
        return {"left": self.left, "right":  self.right}
    }
    setLeftMotor(speed) {
        fetch("http://" + this.ip + ":" + this.port + "/left/set/" + speed)
        .then(response => response.json())
        .then(data => {
            if (data.success == true) {
                this.left = speed
                return true
            } else {
                return false
            }
        })
    }
    setRightMotor(speed) {
        fetch("http://" + this.ip + ":" + this.port + "/right/set/" + speed)
        .then(response => response.json())
        .then(data => {
            if (data.success == true) {
                this.right = speed
                return true
            } else {
                return false
            }
        })
    }
    brake() {
        fetch("http://" + this.ip + ":" + this.port + "/all/brake")
        .then(response => response.json())
        .then(data => {
            if (data.success == true) {
                this.right = 0
                this.left = 0
                return true
            } else {
                return false
            }
        })
    }
    forward(speed) {
        fetch("http://" + this.ip + ":" + this.port + "/all/forward/" + speed)
        .then(response => response.json())
        .then(data => {
            if (data.success == true) {
                this.right = -speed
                this.left = speed
                return true
            } else {
                return false
            }
        })
    }
}