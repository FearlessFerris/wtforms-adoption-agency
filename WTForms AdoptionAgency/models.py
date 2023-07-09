from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()




class Pet(db.Model):
    """ Adopt Pet """


    __tablename__ = 'pets'


    id = db.Column( db.Integer, primary_key = True )
    name = db.Column ( db.Text, nullable = False )      
    species = db.Column ( db.Text, nullable = False )
    age = db.Column( db.Integer )                           # Defaults to nullable is True no need to declare so
    picture_url = db.Column ( db.Text )
    notes = db.Column( db.Text )
    avaliable = db.Column ( db.Boolean, nullable = False, default = True )


    def __init__ ( self, name, species, age,  picture_url, notes, avaliable ):
        self.name = name
        self.species = species
        self.age = age
        self.picture_url = picture_url
        self.notes = notes 
        self.avaliable = avaliable 



    def hello_there( self ):
        return f' Hello friend, my name is {self.name} and I cannot wait to get to know you!!!'
    


def connect_db(app):
    """ Connect to this database in the main Flask app.py """

    db.app = app
    db.init_app(app)






    

    
