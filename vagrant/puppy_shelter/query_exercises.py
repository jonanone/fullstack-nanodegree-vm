from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import timedelta
from database_setup import Base, Shelter, Puppy

engine = create_engine('sqlite:///puppies.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)

session = DBSession()

all_puppies_by_name = session.query(Puppy).order_by(Puppy.name)
print 'Puppies ordered by name'
for puppy in all_puppies_by_name:
    print puppy.name
print '\n'

six_months_ago = timedelta(days=-180)

all_puppies_less_than_6_months = session.query(Puppy).filter(
    Puppy.date_of_birth >= six_months_ago).order_by(-Puppy.date_of_birth)
print 'Younger than 6 months puppies ordered by the youngest first'
for puppy in all_puppies_less_than_6_months:
    print puppy.name + ' - ' + puppy.date_of_birth.strftime("%d/%m/%y")
print '\n'

all_puppies_by_ascending_weight = session.query(Puppy).order_by(Puppy.weight)
print 'Puppies ordered by ascending weight'
for puppy in all_puppies_by_ascending_weight:
    print puppy.name + ' - ' + "%.2f" % round(puppy.weight, 2) + 'Kg'
print '\n'

all_shelters = session.query(Shelter).order_by(Shelter.name)
puppies_by_shelter = {}
for shelter in all_shelters:
    puppies_for_shelter = session.query(Puppy).filter_by(
        shelter=shelter).order_by(Puppy.name)
    puppies_by_shelter[shelter] = puppies_for_shelter

for shelter in puppies_by_shelter:
    print 'Shelter: ' + shelter.name
    print '----------------------------------'
    for puppy in puppies_by_shelter[shelter]:
        print puppy.name
    print '\n'
