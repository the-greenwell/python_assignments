class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
    def display_info(self):
        dict = vars(self)
        for key in dict:
            print(f"{key}: {dict[key]}")
        return self
    def enroll(self):
        if self.is_rewards_member:
            print("User already a member.")
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
        return self
    def spend_points(self, amount):
        if self.gold_card_points >= amount:
            self.gold_card_points -= amount
        else:
            print('Insufficient Points.')
        return self

anthony = User('Anthony','Greenwell','ant@email', 28)
anthony.enroll().spend_points(50).display_info()

kaitlin = User('Kaitlin','Brooks','kait@email', 25)
kristine = User('Kristine', 'Greenwell', 'kris@email', 69)

anthony.spend_points(50)
kaitlin.enroll().spend_points(80).display_info()
kristine.display_info().spend_points(40)