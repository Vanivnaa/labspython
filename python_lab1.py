class Water_pump:
    producing_country = "Польща"
    def __init__(self, power_consumption, brand, efficiency):
        self.power_consumption = power_consumption
        self.brand = brand
        self.efficiency = efficiency

    def __del__(self):
        return

    def __str__(self):
        return "\tСпоживана потужність:{} Вт\n \tМарка виробника: {}\n \tOб’єм води, котру прокачує насос за годину: {} л".format(self.power_consumption, self.brand, self.efficiency) 


    @staticmethod
    def getcountry():
        return Water_pump.producing_country


if __name__ == "__main__":
    water_pulm_1 = Water_pump(4000, "Leo", 9600)
    print(" Водяний насос №1 :\n", water_pulm_1.__str__())

    water_pulm_2 = Water_pump(1200, "Lex", 13000)
    print(" Водяний насос №2 :\n", water_pulm_2.__str__())

    water_pulm_3 = Water_pump(1100, "Forwater", 3600 )
    print(" Водяний насос №3 :\n", water_pulm_3.__str__())

    print("\n КРАЇНА ВИРОБНИКІВ: ", Water_pump.getcountry())
