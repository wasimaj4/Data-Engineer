class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def __repr__(self):
    return self.name + ' menu available from ' + str(self.start_time) + ' - ' + str(self.end_time)
  def calculate_bill(self, purchased_items):
    total_price = 0
    for item in purchased_items:
      if item in self.items:
        total_price += self.items[item]
    return total_price
class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
  def __repr__(self):
    return self.address
  def available_menus(self, time):
    available_menu = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
         available_menu.append(menu)
    return available_menu
      
class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

brunch_items = {  
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}
brunch_menu = Menu('Brunch', brunch_items, 1100, 1600)

early_bird_items = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}
early_bird_menu = Menu('Early bird', early_bird_items, 1500, 1800)

dinner_items = {
  'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}
dinner_menu = Menu('Dinner', dinner_items, 1700, 2300)

kids_itmes = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}

kids_menu = Menu('Kids', kids_itmes, 1100, 2100)
#print(kids_menu)

print(brunch_menu.calculate_bill(['pancakes', 'home fries', 'coffee']))
print(early_bird_menu.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))
menus = [brunch_menu, early_bird_menu, dinner_menu, kids_menu]
flagship_store = Franchise("1232 West End Road", menus)
new_installment = Franchise("12 East Mulberry Street", menus)

#print(flagship_store)

print(flagship_store.available_menus(1200))
print(flagship_store.available_menus(1700))
basta = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

arepas_items = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}
arepas_menu = Menu('Take a Arepa', arepas_items, 1000, 2000)

arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])

arepas = Business("Take a Arepa", [arepas_place])
print(arepas.franchises[0].menus[0])
