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
    def enroll(self):
        if self.is_rewards_member:
            print("User already a member.")
            return False
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
            return True
    def spend_points(self, amount):
        if self.gold_card_points >= amount:
            self.gold_card_points -= amount
        else:
            print('Insufficient Points.')

anthony = User('Anthony','Greenwell','ant@email', 28)
anthony.enroll()

kaitlin = User('Kaitlin','Brooks','kait@email', 25)
kristine = User('Kristine', 'Greenwell', 'kris@email', 69)

anthony.spend_points(50)
kaitlin.enroll()
kaitlin.spend_points(80)

anthony.display_info()
kaitlin.display_info()
kristine.display_info()

anthony.enroll()
kristine.spend_points(40)