from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import inspect
from database_setup import Base, Restaurant, MenuItem


# Init database session
def db_init():
    engine = create_engine('sqlite:///restaurantmenu.db')
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    return session


# Get restaurants ordered alphabetically by name
def get_restaurants(session):
    all_restaurants = session.query(Restaurant).order_by(Restaurant.name)
    return all_restaurants


# Get restaurant by id
def get_restaurant(session, restaurant_id):
    return session.query(Restaurant).filter_by(id=restaurant_id).one()


# Add new restaurant
def add_restaurant(session, data):
    new_restaurant = Restaurant(name=data['name'])
    session.add(new_restaurant)
    session.commit()
    return new_restaurant


# Edit given restaurant
def edit_restaurant(session, restaurant_id, data):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    mapper = inspect(Restaurant)
    for key in data:
        for column in mapper.attrs:
            if key == column.key:
                setattr(restaurant, key, data[key])
    session.add(restaurant)
    session.commit()
    return restaurant


# Delete given restaurant
def delete_restaurant(session, restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    session.delete(restaurant)
    session.commit()
    return 1


# Get all restaurant items
def get_restaurant_items(session, restaurant):
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant.id)
    return items


# Get menu item by id
def get_menu_item(session, menu_item_id):
    return session.query(MenuItem).filter_by(id=menu_item_id).one()


# Add new menu item
def add_menu_item(session, restaurant, data):
    new_item = MenuItem(name=data['name'],
                        description=data['description'],
                        price=data['price'],
                        course=data['course'],
                        restaurant_id=restaurant.id)
    session.add(new_item)
    session.commit()
    return new_item


# Edit menu item
def edit_menu_item(session, edited_item, data):
    mapper = inspect(MenuItem)
    for key in data:
        for column in mapper.attrs:
            if key == column.key and data[key]:
                setattr(edited_item, key, data[key])
    session.add(edited_item)
    session.commit()
    return edited_item


# Delete given menu item
def delete_menu_item(session, menu_item):
    session.delete(menu_item)
    session.commit()
    return 1


def test():
    session = db_init()

    # Test get_restaurants
    restaurants = get_restaurants(session)
    print 'Restaurants loaded successfully.\n'
    for restaurant in restaurants:
        print restaurant.name
    print '--------------------'

    # Test add_restaurant
    new_restaurant = add_restaurant(session, {'name': 'Rocker\'s corner'})
    if new_restaurant:
        print new_restaurant.name + ' added successfully to the db.\n'
    print '--------------------'

    # Test edit_restaurant
    edited_restaurant = edit_restaurant(session, new_restaurant.id,
                                        {'name': 'Old rocker\'s corner'})
    if edited_restaurant:
        print edited_restaurant.name + ' edited successfully.\n'
    print '--------------------'

    # Test delete_restaurant
    restaurant_deleted = delete_restaurant(session, new_restaurant.id)
    if restaurant_deleted:
        print 'Restaurant deleted succesfully.\n'
        for restaurant in restaurants:
            print restaurant.name
    print '--------------------'
