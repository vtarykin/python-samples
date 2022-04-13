class MoneyBox:
     def __init__(self, capacity):
         self.capacity = capacity
         coins = 0
         check = 0
         self.coins = coins
         self.check = check

     def can_add(self, v):
         self.check = self.coins
         self.check += v
         if self.check < self.capacity:
             return True
         else:
             return False

     def add(self,v):
         if self.can_add(v)==True:
             self.coins += v
         print(self.coins)

a = MoneyBox(100)
a.add(26)
a.add(23)
a.add(30)
a.coins
