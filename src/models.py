from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()


class User(db.Model):
    __tablename__= 'usuario'
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(
        String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)

    favorites: Mapped[list['CharactereFavorite']]= relationship(back_populates='users')
    favorites_planet: Mapped[list['PlanetFavorite']] = relationship(back_populates = 'users')
    favorite_vehicle: Mapped[list['VehicleFavorite']] = relationship(back_populates = 'users')

class Character(db.Model):
    __tablename__= 'people'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    height: Mapped[int] = mapped_column(Integer)
    gender: Mapped[str] = mapped_column(String, nullable=False)
    eyes_color: Mapped[str] = mapped_column(String(50))
    birth_day: Mapped[str] = mapped_column(String(20))
    mass: Mapped[int] = mapped_column(nullable=True)
    favorites_by: Mapped[list['CharactereFavorite']] = relationship(back_populates='characteres')
class Planet(db.Model):
    __tablename__= 'planets'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(60), nullable=False)
    climate: Mapped[str] = mapped_column(String(120), nullable=True)
    diametre: Mapped[int] = mapped_column(nullable=True)
    population: Mapped[int] = mapped_column(nullable=True)
    favorite_by: Mapped[list['PlanetFavorite']] = relationship(back_populates = 'planetas')

class Vehicle(db.Model):
    __tablename__= 'vehicles'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), nullable=True)
    model: Mapped[str] = mapped_column(String(120))
    passengers: Mapped[int] = mapped_column(nullable=False)
    favorite_by: Mapped[list['VehicleFavorite']] = relationship(back_populates = 'vehiculo')

class Starship(db.Model):
    __tablename__ = 'starships'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    model: Mapped[str] = mapped_column(String(120))
    passengers: Mapped[int] = mapped_column(nullable=False)
    length: Mapped[int] = mapped_column(nullable=False)

class CharactereFavorite(db.Model):
    __tablename__ = 'charactere_favorite'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int]= mapped_column(ForeignKey('usuario.id'))
    users: Mapped['User'] = relationship(back_populates='favorites')

    character_id:Mapped[int] = mapped_column(ForeignKey('people.id'))
    characteres: Mapped['Character'] = relationship(back_populates='favorites_by')

class PlanetFavorite(db.Model):
    __tablename__ = 'planet_favorite'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('usuario.id'))
    users: Mapped['User'] = relationship(back_populates = 'favorites_planet')

    planet_id: Mapped[int] = mapped_column(ForeignKey('planets.id'))
    planetas: Mapped['Planet'] = relationship(back_populates = 'favorite_by')

class VehicleFavorite(db.Model):
    __tablename__ = 'vehicle_favorite'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id:Mapped[int] = mapped_column(ForeignKey('usuario.id'))
    users: Mapped['User'] = relationship(back_populates = 'favorite_vehicle')

    vehicle_id: Mapped[int] = mapped_column(ForeignKey('vehicles.id'))
    vehiculo: Mapped['Vehicle'] = relationship(back_populates = 'favorite_by')

class StarshipFavorite(db.Model):
    __tablename__ = 'starship_favorite'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id:Mapped[int] = mapped_column(ForeignKey('usuario.id'))

    starship_id: Mapped[int] = mapped_column(ForeignKey('starships.id'))
       



def serialize(self):
    return {
        "id": self.id,
        "email": self.email,
            # do not serialize the password, its a security breach
        }
