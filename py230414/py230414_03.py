class AP:
    def __init__(self, brand):
        self.brand=brand

    def takeoff(self):
        print("비행기가 결항입니다")
    
    def land(self):
        print("비행기가 착륙합니다")
     
AP1 = AP("대한항공")

if __name__=="__name__":
    print("항공사는 ", AP1.brand, "입니다")
    AP1.takeoff()
    AP1.land()