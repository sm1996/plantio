import datetime

class Plant(object):

  def __init__(self,name,date):
    self.name=name
    self.plant_date=date

def make_plant(name,plant_date):
  plant=Plant(name,plant_date)
  return plant

rose=make_plant("Rose",datetime.datetime(2018,12,05))
grass=make_plant("Grass",datetime.datetime(2018,12,06))

plants_list=[]
plants_list.append(rose)
plants_list.append(grass)

for plant in plants_list:
    print "{} planted on {}".format(plant.name, str(plant.plant_date))

search = raw_input ("Enter the name of a plant you own")

plant_found = False
for plant in plants_list:
    if str(search) == str(plant.name):
        print plant.plant_date
        plant_found = True

if plant_found==False:
    print "Plant not found"

search_v2 = raw_input ("Enter the names of all the plants you own, separated by commas")
search_list=search_v2.split(",")

print_plant=0
for plant in plants_list:
    if plant.name in search_list:
        print plant.plant_date
        print_plant=print_plant+1

count_plant=len(search_list)
if count_plant!=print_plant:
    print "Not all plants found"
