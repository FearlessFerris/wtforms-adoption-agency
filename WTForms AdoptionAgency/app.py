from flask import Flask, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPets




app = Flask(__name__)
app.config['SECRET_KEY'] = 'imasecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt_db'    # Location of the database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False     # Set this to false or will enable tracking of object modifications and display errors



app.app_context().push()
connect_db(app)
db.create_all()




# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False      # Having this line uncommented will stop the debug toolbar from showing redirects which can help when debugging
toolbar = DebugToolbarExtension(app)






@app.route('/')
def homepage():
    """ Routes to the website homepage """


    pets = Pet.query.all()

    return render_template( 'pets-homepage.html', pets = pets )






@app.route('/pets/<int:pets_id>')
def pet_details(pets_id):
    """ Routes to display pets details page """

    pets = Pet.query.get_or_404(pets_id)

    return render_template( 'pets-details.html', pets = pets )






@app.route('/add', methods = ['GET', 'POST'])
def add_pets():
    """ Routes to the add a pet form """

    
    form = AddPetForm()

    if form.validate_on_submit():   # This line of code is doing two different things: Is this a post request? Is this token valid?
        data = {k: v for k, v in form.data.items() if k != 'csrf_token'}
        new_pet = Pet(**data)
        # new_pet = Pet( name = form.name.data, species = form.species.data, age = form.age.data, picture_url = form.picture_url.data, notes = form.notes.data, avaliable = form.avaliable.data)

        db.session.add(new_pet)
        db.session.commit()
        flash(f'{new_pet.name} was added!')
        return redirect('/')
    
    else: 
        return render_template( 'add-pet-form.html', form = form )      # form is a python object that represents a form 






@app.route('/pets/<int:pets_id>/edit', methods = ['GET', 'POST'])
def edit_pet(pets_id):
    """ Routes to an edit form / upon successful submit will redirect to details page """

    pets = Pet.query.get_or_404(pets_id)
    form = EditPets( obj = pets )

    if form.validate_on_submit():
        pets.notes = form.notes.data
        pets.avaliable = form.avaliable.data
        pets.picture_url = form.picture_url.data
        db.session.commit()

        flash(f'{pets.name} profile has been updated' )

        return redirect('/')
    
    else:

        return render_template('pet-edit-form.html', pets = pets, form = form )
    





@app.route('/delete/<int:pets_id>', methods = ['POST'])
def delete_pet(pets_id):
    """ Routes a post request to delete a pet """

    pets = Pet.query.get_or_404(pets_id)

    db.session.delete(pets)
    db.session.commit()

    return redirect('/')


















