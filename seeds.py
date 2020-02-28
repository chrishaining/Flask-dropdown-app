from app import db
from app.models import Player

# clear the database
Player.query.delete()

# create players
player1 = Player(first_name="Cantata ", last_name="Zomes")
player2 = Player(first_name="Louder", last_name="Fargo")
player3 = Player(first_name="Varius", last_name="Lant")

# add them to the database
db.session.add(player1)
db.session.add(player2)
db.session.add(player3)


# commit
db.session.commit()
players = Player.query.all()
print(players)