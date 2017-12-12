from flask import Flask, url_for, render_template, request, redirect, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem
app = Flask(__name__)

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

#Fake Restaurants
restaurant = {'name': 'The CRUDdy Crab', 'id': '1'}

restaurants = [{'name': 'The CRUDdy Crab', 'id': '1'}, 
               {'name':'Blue Burgers', 'id':'2'},
               {'name':'Taco Hut', 'id':'3'}]

#Fake Menu Items
items = [{'name':'Cheese Pizza', 'description':'made with fresh cheese', 'price':'$5.99',
          'course' :'Entree', 'id':'1'}, 
         {'name':'Chocolate Cake','description':'made with Dutch Chocolate', 'price':'$3.99',
          'course':'Dessert','id':'2'},
         {'name':'Caesar Salad', 'description':'with fresh organic vegetables','price':'$5.99', 
          'course':'Entree','id':'3'},
         {'name':'Iced Tea', 'description':'with lemon','price':'$.99', 
          'course':'Beverage','id':'4'},
         {'name':'Spinach Dip', 'description':'creamy dip with fresh spinach','price':'$1.99', 
          'course':'Appetizer','id':'5'}]
item = {'name':'Cheese Pizza','description':'made with fresh cheese','price':'$5.99',
        'course' :'Entree'}

# Show all restaurants
@app.route('/')
@app.route('/restaurants/')
def showRestaurants():
    return render_template('restaurants.html', restaurants = restaurants)

@app.route('/restaurant/new/', methods=['GET', 'POST'])
def newRestaurant():
    return render_template('newRestaurant.html')

@app.route('/restaurant/<int:restaurant_id>/edit/', methods=['GET', 'POST'])
def editRestaurant(restaurant_id):
    return render_template('editRestaurant.html', restaurant = editedRestaurant)

@app.route('/restaurant/<int:restaurant_id>/delete/', methods=['GET', 'POST'])
def deleteRestaurant(restaurant_id):
    return render_template('deleteRestaurant', restaurant = restaurantToDelete)

@app.route('/restaurant/<int:restaurant_id>/')
@app.route('/restaurant/<int:restaurant_id>/menu/')
def showMenu(restaurant_id):
    return render_template('menu.html', restaurant = restaurant, items = items)

@app.route('/restaurant/<int:restaurant_id>/menu/new/', methods=['GET', 'POST'])
def newMenuItem(restaurant_id):
    return render_template('newMenuItem.html', restaurant_id = restaurant_id)

@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit/', methods=['GET', 'POST'])
def editMenuItem(restaurant_id, menu_id):
    return render_template('editMenuItem.html', restaurant_id = restaurant_id, item = editeditem)

@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete/', methods=['GET', 'POST'])
def deleteMenuItem(restaurant_id, menu_id):
    return render_template('deleteMenuitem.html', item = itemToDelete)

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host = '0.0.0.0', port= 5000)














