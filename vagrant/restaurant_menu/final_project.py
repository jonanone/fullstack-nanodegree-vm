from flask import Flask
app = Flask(__name__)


@app.route('/')
@app.route('/restaurants/')
def restaurants():
    return 'Show all the restaurants'


@app.route('/restaurant/<int:restaurant_id>/')
@app.route('/restaurant/<int:restaurant_id>/menu/')
def restaurantMenu(restaurant_id):
    return 'This should show restaurant %s menu items' % restaurant_id


@app.route('/restaurant/new')
def newRestaurant():
    return 'This should show new restaurant form'


@app.route('/restaurant/<int:restaurant_id>/edit')
def editRestaurant(restaurant_id):
    return 'This should show edit restaurant %s form' % restaurant_id


@app.route('/restaurant/<int:restaurant_id>/delete')
def deleteRestaurant(restaurant_id):
    return 'This should show delete restaurant %s form' % restaurant_id


@app.route('/restaurant/<int:restaurant_id>/menu/item/new')
def newMenuItem(restaurant_id):
    return 'This should show new menu item form for restaurant %s' % restaurant_id


@app.route('/restaurant/<int:restaurant_id>/menu/item/<int:item_id>/edit')
def editMenuItem(restaurant_id, item_id):
    return 'This should show edit menu item form for item %s' % item_id


@app.route('/restaurant/<int:restaurant_id>/menu/item/<int:item_id>/delete')
def deleteMenuItem(restaurant_id, item_id):
    return 'This should show delete menu item form for item %s' % item_id

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
