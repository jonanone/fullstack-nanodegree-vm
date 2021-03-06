from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import func
from database_setup import Base, Shelter, Puppy
from database_setup import PuppyProfile, Adoption, Adopter
from random import randint
import datetime
import random


engine = create_engine('sqlite:///puppies.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()


# Add Shelters
shelter1 = Shelter(
    name="Oakland Animal Services",
    address="1101 29th Ave",
    city="Oakland",
    state="California",
    zipCode="94601",
    maximum_capacity=50,
    current_occupancy=0,
    website="oaklandanimalservices.org")
session.add(shelter1)

shelter2 = Shelter(
    name="San Francisco SPCA Mission Adoption Center",
    address="250 Florida St",
    city="San Francisco",
    state="California",
    zipCode="94103",
    maximum_capacity=50,
    current_occupancy=0,
    website="sfspca.org")
session.add(shelter2)

shelter3 = Shelter(
    name="Wonder Dog Rescue",
    address="2926 16th Street",
    city="San Francisco",
    state="California",
    zipCode="94103",
    maximum_capacity=20,
    current_occupancy=0,
    website="http://wonderdogrescue.org")
session.add(shelter3)

shelter4 = Shelter(
    name="Humane Society of Alameda",
    address="PO Box 1571",
    city="Alameda",
    state="California",
    zipCode="94501",
    maximum_capacity=3,
    current_occupancy=0,
    website="hsalameda.org")
session.add(shelter4)

shelter5 = Shelter(
    name="Palo Alto Humane Society",
    address="1149 Chestnut St.",
    city="Menlo Park",
    state="California",
    zipCode="94025",
    maximum_capacity=10,
    current_occupancy=0,
    website="paloaltohumane.org")
session.add(shelter5)

print 'Shelters created'

# Add Puppies

male_names = ["Bailey", "Max", "Charlie", "Buddy", "Rocky", "Jake", "Jack",
              "Toby", "Cody", "Buster", "Duke", "Cooper", "Riley", "Harley",
              "Bear", "Tucker", "Murphy", "Lucky", "Oliver", "Sam", "Oscar",
              "Teddy", "Winston", "Sammy", "Rusty", "Shadow", "Gizmo",
              "Bentley", "Zeus", "Jackson", "Baxter", "Bandit", "Gus",
              "Samson", "Milo", "Rudy", "Louie", "Hunter", "Casey",
              "Rocco", "Sparky", "Joey", "Bruno", "Beau", "Dakota",
              "Maximus", "Romeo", "Boomer", "Luke", "Henry"]

female_names = ['Bella', 'Lucy', 'Molly', 'Daisy', 'Maggie', 'Sophie', 'Sadie',
                'Chloe', 'Bailey', 'Lola', 'Zoe', 'Abby', 'Ginger', 'Roxy',
                'Gracie', 'Coco', 'Sasha', 'Lily', 'Angel', 'Princess', 'Emma',
                'Annie', 'Rosie', 'Ruby', 'Lady', 'Missy', 'Lilly', 'Mia',
                'Katie', 'Zoey', 'Madison', 'Stella', 'Penny', 'Belle',
                'Casey', 'Samantha', 'Holly', 'Lexi', 'Lulu', 'Brandy',
                'Jasmine', 'Shelby', 'Sandy', 'Roxie', 'Pepper', 'Heidi',
                'Luna', 'Dixie', 'Honey', 'Dakota']


adopter_names = ['John', 'Andrew', 'Angela',
                 'Steve', 'Peter', 'Rose', 'Sandra']

adopter_last_names = ['Stevenson', 'Hamill', 'Ford', 'Connor']

puppy_images = [
            "http://pixabay.com/get/da0c8c7e4aa09ba3a353/1433170694/dog-785193_1280.jpg?direct",
            "http://pixabay.com/get/6540c0052781e8d21783/1433170742/dog-280332_1280.jpg?direct",
            "http://pixabay.com/get/8f62ce526ed56cd16e57/1433170768/pug-690566_1280.jpg?direct",
            "http://pixabay.com/get/be6ebb661e44f929e04e/1433170798/pet-423398_1280.jpg?direct",
            "http://pixabay.com/static/uploads/photo/2010/12/13/10/20/beagle-puppy-2681_640.jpg",
            "http://pixabay.com/get/4b1799cb4e3f03684b69/1433170894/dog-589002_1280.jpg?direct",
            "http://pixabay.com/get/3157a0395f9959b7a000/1433170921/puppy-384647_1280.jpg?direct",
            "http://pixabay.com/get/2a11ff73f38324166ac6/1433170950/puppy-742620_1280.jpg?direct",
            "http://pixabay.com/get/7dcd78e779f8110ca876/1433170979/dog-710013_1280.jpg?direct",
            "http://pixabay.com/get/31d494632fa1c64a7225/1433171005/dog-668940_1280.jpg?direct"
            ]

descriptions = [
            'This is a wonderful puppy, with great hair and very agile.',
            'This puppy is adorable, eats like a dinosaur and is like having your best friend in mini-size.']


special_needs = 'This puppy has a very beatiful hair and needs to be brushed twice a week.'


# This method will make a random age for each puppy between 0-18
# months(approx.) old from the day the algorithm was run.
def CreateRandomAge():
    today = datetime.date.today()
    days_old = randint(0, 540)
    birthday = today - datetime.timedelta(days=days_old)
    return birthday


# This method will create a random weight between 1.0-40.0
# pounds (or whatever unit of measure you prefer)
def CreateRandomWeight():
    return random.uniform(1.0, 40.0)


# This method will create a random special needs text or none
def CreateRandomSpecialNeeds():
    num = randint(0, 1)
    if num:
        return special_needs
    else:
        return None


# This methos gets a random adopter
def GetRandomAdopter():
    random_adopter = session.query(Adopter).order_by(func.random()).first()
    return random_adopter


def check_puppy_into_random_shelter(puppy):
    random_shelter = session.query(Shelter).filter_by(id=randint(1, 5)).first()
    if random_shelter.current_occupancy == random_shelter.maximum_capacity:
        print 'We tried to check ' + puppy.name + ' into '\
              + random_shelter.name
        print 'but it is at full capacity.'
        print 'Please, select another shelter to check in ' + puppy.name
        print 'Shelters: '
        shelters = session.query(Shelter).filter(
            Shelter.id != random_shelter.id).order_by(Shelter.id)
        shelter_ids = []
        for shelter in shelters:
            if shelter.current_occupancy < shelter.maximum_capacity:
                print str(shelter.id) + '.- ' + shelter.name + ' - ' + \
                      str(shelter.current_occupancy) + '/' + \
                      str(shelter.maximum_capacity)
                shelter_ids.append(shelter.id)
        answer = int(raw_input('Select the shelter number: '))
        while (answer not in shelter_ids):
            answer = int(raw_input('That is not a valid selection.\n \
                                Please, select another shelter: '))
        for shelter in shelters:
            if answer == shelter.id:
                puppy.shelter_id = shelter.id
                puppy.shelter = shelter
                session.add(puppy)
                shelter.current_occupancy += 1
                session.add(shelter)
                print 'Congrats! ' + puppy.name + ' has been checked into '\
                      + shelter.name
    else:
        puppy.shelter_id = random_shelter.id
        puppy.shelter = random_shelter
        session.add(puppy)
        random_shelter.current_occupancy += 1
        session.add(random_shelter)


for i, x in enumerate(male_names):
    new_puppy = Puppy(
        name=x,
        gender="male",
        date_of_birth=CreateRandomAge(),
        weight=CreateRandomWeight())
    session.add(new_puppy)
    new_puppy_profile = PuppyProfile(picture_url=random.choice(puppy_images),
                                     description=random.choice(descriptions),
                                     special_needs=CreateRandomSpecialNeeds(),
                                     puppy=new_puppy)
    session.add(new_puppy_profile)
    check_puppy_into_random_shelter(new_puppy)
    session.commit()

for i, x in enumerate(female_names):
    new_puppy = Puppy(
        name=x,
        gender="female",
        date_of_birth=CreateRandomAge(),
        weight=CreateRandomWeight())
    session.add(new_puppy)
    new_puppy_profile = PuppyProfile(picture_url=random.choice(puppy_images),
                                     description=random.choice(descriptions),
                                     special_needs=CreateRandomSpecialNeeds(),
                                     puppy=new_puppy)
    session.add(new_puppy_profile)
    check_puppy_into_random_shelter(new_puppy)
    session.commit()

for i, x in enumerate(adopter_names):
    new_adopter = Adopter(
        name=x,
        last_name=random.choice(adopter_last_names))
    session.add(new_adopter)
    session.commit()


adopted_puppies = session.query(Puppy)[:10]
for puppy in adopted_puppies:
    adopter = GetRandomAdopter()
    new_adoption = Adoption(date=CreateRandomAge(),
                            puppy=puppy,
                            adopter=adopter)
    puppy.adopters.append(new_adoption)
    new_adoption.adopter.puppies.append(new_adoption)
    session.add(new_adoption)
    session.commit()
