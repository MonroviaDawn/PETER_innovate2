
class Hero():
    def __init__(self, hero_name, gov_name, district, rank):
        self.name = hero_name
        self.secret_identity = gov_name
        self.powers = []
        self.district = district
        self.rank = rank

    def set_powers(self, power):
        self.powers.append(power)
    def get_powers(self):
        return self.powers      

