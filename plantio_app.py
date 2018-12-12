from flask import Flask, render_template, request, redirect
from icalendar import Calendar, Event
from datetime import datetime
from pytz import UTC

app = Flask('MyApp')

#app's plant catalogue
class Plant(object):

  def __init__(self,name,date):
    self.name=name
    self.plant_date=date

def make_plant(name,plant_date):
  plant=Plant(name,plant_date)
  return plant

rose=make_plant("rose",datetime(2018,12,05,0,0,0,tzinfo=UTC))
fig=make_plant("fig",datetime(2018,12,06,0,0,0,tzinfo=UTC))
aloe=make_plant("aloe",datetime(2018,12,07,0,0,0,tzinfo=UTC))
sunflower=make_plant("sunflower",datetime(2018,12,07,0,0,0,tzinfo=UTC))

plants_list=[]
plants_list.append(rose)
plants_list.append(fig)
plants_list.append(aloe)
plants_list.append(sunflower)

user_plants=[]
#user_calendar=ics.icalendar.Calendar()

#get info from user
@app.route('/',methods=['POST', 'GET'])
def index():
   return render_template('choose_plant.html')


@app.route('/plant_cal',methods=['POST', 'GET'])
def plant_cal():
    input_plants = request.form.getlist('plants')
    #compare user plants to app's plant catalogue
    cal = Calendar()
    cal.add('prodid', '-//My calendar product//mxm.dk//')
    cal.add('version', '2.0')

    for plant in plants_list:
        if (plant.name) in input_plants:
            event = Event()
            event.add('summary', plant.name)
            event.add('dtstart', plant.plant_date)
            event.add('dtend', plant.plant_date)
            cal.add_component(event)
    f = open('your_plant_calendar.ics', 'wb')
    f.write(cal.to_ical())
    f.close()
    print cal.to_ical()
    return render_template('plant_cal.html',user_plants=user_plants)

app.run(debug=True)
