""" Forms for the adopt app """


from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Length, NumberRange, URL, Optional



class AddPetForm(FlaskForm):
    """ Form for adding new pets """

    name = StringField( 'Pet Name', validators = [InputRequired()] )
    species = SelectField( 'Species ', choices = ['C. hircus', 'T. imperator', 'Panther Chameleon', 'Northern Giraffe', 'C. familiaris'] )
    picture_url = StringField('Picture URL', validators = [Optional(), URL()] )
    age = IntegerField( 'Age', validators = [Optional(), NumberRange(min = 0, max = 30)] )
    notes = TextAreaField( 'Notes', validators = [Optional(), Length(min = 1)] )
    avaliable = BooleanField( 'Avaliable' )



class EditPets(FlaskForm):
    """ Edit pet form """

    picture_url = StringField( 'Picture URL', validators = [Optional(), URL()])
    notes = StringField( 'Notes', validators = [Optional(), Length(min = 1)] )
    avaliable = BooleanField( 'Avaliable' )



