from flask import Blueprint, render_template
import json
import os

# Load pet data from JSON file
base_dir = os.path.dirname(os.path.abspath(__file__))
pets_file = os.path.join(base_dir, 'pets.json')

with open(pets_file) as f:
    pets = json.load(f)

bp = Blueprint('pet', __name__, url_prefix="/pets")

@bp.route('/')
def index():
    return render_template('pets/index.html', pets=pets)

@bp.route('/<int:id>')
def show(id):
    pet = next((pet for pet in pets if pet['pet_id'] == id), None)
    if pet is None:
        return "Pet not found", 404
    return render_template('pets/show.html', pet=pet)


# from flask import ( Blueprint, render_template ) 
# import json 

# pets = json.load(open('pets.json'))

# bp = Blueprint('pet', __name__, url_prefix="/pets")

# @bp.route('/')
# def index(): 
#     return render_template('pets/index.html', pets=pets)

# @bp.route('/<int:id>')
# def show(id): 
#     pet = pets[id - 1]
#     return render_template('pets/show.html', pet=pet)