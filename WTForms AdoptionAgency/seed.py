""" Seed file to make sample data for our database """

from models import Pet, db
from app import app




# Create all tables 

db.drop_all()
db.create_all()





billy = Pet( name = 'Billy the Goat', species = 'C. hircus', age = 12, picture_url = 'https://i.etsystatic.com/7051074/r/il/584986/2035634265/il_fullxfull.2035634265_p32x.jpg', notes = 'Loves long walks on the beach', avaliable = True )

tyrone = Pet ( name = 'Tyrone the Tyrannosaurus', species = 'T. imperator', age = 8, picture_url = 'https://www.hollywoodreporter.com/wp-content/uploads/2015/04/mcdjupa_ec032_h.jpg', notes = 'Loves to eat goats and flashing lights but hates cars', avaliable = True )

cleo = Pet( name = 'Cleo the Chameleon', species = 'Panther Chameleon', age = 21, picture_url = 'https://i0.wp.com/tortoisesworld.com/wp-content/uploads/2021/08/WhatsApp-Image-2021-08-20-at-6.44.38-AM-1.jpeg?fit=1080%2C1080&ssl=1', notes = 'I enjoy changing colors and climing things', avaliable = True )

jasmine = Pet( name = 'Jasmine the Giraffe', species = 'Northern Giraffe', age = 14, picture_url = 'https://www.pbs.org/wnet/nature/files/2020/07/giraffe.png', notes = 'I enjoy eating fruit and grass while spending some time near the shady trees', avaliable = True )

bobby = Pet( name = 'Bobby the Bulldog', species = 'C. familiaris', age = 2, picture_url = 'https://cdn.britannica.com/08/234208-050-C9A21C4C/English-bulldog-dog.jpg', notes = 'I enjoy being the goodest boy and obviously some tasty treats',  avaliable = True )





db.session.add(billy)
db.session.add(tyrone)
db.session.add(cleo)
db.session.add(jasmine)
db.session.add(bobby)

db.session.commit()



