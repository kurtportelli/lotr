from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    ext_id = Column(String, unique=True, index=True)
    name = Column(String, unique=True, index=True)

    chapters = relationship("Chapter", back_populates="book")


class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    ext_id = Column(String, unique=True, index=True)
    name = Column(String, unique=True, index=True)
    runtime_in_minutes = Column(Integer, default=0)
    budget_in_millions = Column(Integer, default=0)
    box_office_revenue_in_millions = Column(Integer, default=0)
    academy_award_nominations = Column(Integer, default=0)
    academy_award_wins = Column(Integer, default=0)
    rotten_tomatoes_score = Column(Integer, default=0)

    quotes = relationship("Quote", back_populates="movie")


class Character(Base):
    __tablename__ = "characters"

    id = Column(Integer, primary_key=True, index=True)
    ext_id = Column(String, unique=True, index=True)
    height = Column(Integer, default=0)
    race = Column(String, default="")
    gender = Column(String, default="")
    birth = Column(String, default="")
    spouse = Column(String, default="")
    death = Column(String, default="")
    realm = Column(String, default="")
    hair = Column(String, default="")
    name = Column(String, default="")  # there are 7 instances of 2 characters with same name
    wiki_url = Column(String, default="")

    quotes = relationship("Quote", back_populates="character")


class Quote(Base):
    __tablename__ = "quotes"

    id = Column(Integer, primary_key=True, index=True)
    ext_id = Column(String, unique=True, index=True)
    dialog = Column(String, default="")
    movie_id = Column(Integer, ForeignKey("movies.id"))
    character_id = Column(Integer, ForeignKey("characters.id"))

    movie = relationship("Movie", back_populates="quotes")
    character = relationship("Character", back_populates="quotes")



class Chapter(Base):
    __tablename__ = "chapters"

    id = Column(Integer, primary_key=True, index=True)
    ext_id = Column(String, unique=True, index=True)
    chapter_name = Column(String, unique=True, index=True)
    book_id = Column(Integer, ForeignKey("books.id"))

    book = relationship("Book", back_populates="chapters")
