class Aircraft():
    def __init__(self, base_damage, max_ammo, aircraft_type):
        self.current_ammo = 0
        self.base_damage = base_damage
        self.max_ammo = max_ammo
        self.aircraft_type = aircraft_type
        self.damage = self.base_damage * self.current_ammo

    def fight(self):
        self.damage_done = self.damage
        self.current_ammo = 0
        return self.damage_done

    def refill(self, ammo_input):
        self.ammo_input = ammo_input
        if ammo_input < self.max_ammo:
            self.current_ammo += ammo_input
            self.damage = self.base_damage * self.current_ammo
            return 0
        else:
            self.current_ammo = self.max_ammo
            self.damage = self.base_damage * self.current_ammo
            return ammo_input - self.max_ammo

    def get_type(self):
        return self.aircraft_type

    def get_status(self):
        return str(self.aircraft_type) + " " + str(self.current_ammo) + " " + str(self.base_damage) + " " + str(self.damage)

class F16(Aircraft):
    def __init__(self):
        super().__init__(max_ammo = 8, base_damage = 30, aircraft_type = "F16")

class F35(Aircraft):
    def __init__(self):
        super().__init__(max_ammo = 12, base_damage = 50, aircraft_type = "F35")

class Carrier():
    def __init__(self, current_carrier_ammo, health_point):
        self.current_carrier_ammo = current_carrier_ammo
        self.aircraft_list = []
        self.health_point = health_point

    def add_aircraft(self, aircraft_type):
        if aircraft_type == "f16":
            self.aircraft_list.append(F16())
        elif aircraft_type == "f35":
            self.aircraft_list.append(F35())

    def fill_aircraft(self):
        for aircraft in self.aircraft_list:
            if aircraft.get_type() == "F35":
                self.current_carrier_ammo = aircraft.refill(self.current_carrier_ammo)
        for aircraft in self.aircraft_list:
            self.current_carrier_ammo = aircraft.refill(self.current_carrier_ammo)

    def carrier_fight(self, enemy_carrier):
        for aircraft in self.aircraft_list:
            enemy_carrier.health_point -= aircraft.fight()




f16 = F16()
f35 =  F35()

carrier = Carrier(25, 0)
u_boat = Carrier(20, 1000)
print(f16.base_damage)
print(f35.max_ammo)
print(f16.get_type())
print(f16.refill(10))
print(f16.get_status())
carrier.add_aircraft("f16")
carrier.add_aircraft("f35")
carrier.add_aircraft("f16")
carrier.add_aircraft("f35")

print(carrier.aircraft_list[0].get_type())
print(carrier.aircraft_list[2].get_type())
print(carrier.aircraft_list[0].current_ammo)

carrier.fill_aircraft()
print(carrier.aircraft_list[0].current_ammo)
print(carrier.aircraft_list[1].current_ammo)
print(carrier.aircraft_list[2].current_ammo)
print(carrier.aircraft_list[3].current_ammo)

carrier.carrier_fight(u_boat)
print(u_boat.health_point)
