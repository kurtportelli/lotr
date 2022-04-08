from sqlalchemy.orm import Session

from . import models, schemas


def get_book(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()


def get_book_by_ext_id(db: Session, ext_id: int):
    return db.query(models.Book).filter(models.Book.ext_id == ext_id).first()


def get_book_by_name(db: Session, name: int):
    return db.query(models.Book).filter(models.Book.name == name).first()


def get_books(db: Session):
    return db.query(models.Book).all()


def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def get_movie(db: Session, movie_id: int):
    return db.query(models.Movie).filter(models.Movie.id == movie_id).first()


def get_movie_by_ext_id(db: Session, ext_id: int):
    return db.query(models.Movie).filter(models.Movie.ext_id == ext_id).first()


def get_movie_by_name(db: Session, name: int):
    return db.query(models.Movie).filter(models.Movie.name == name).first()


def get_movies(db: Session):
    return db.query(models.Movie).all()


def create_movie(db: Session, movie: schemas.MovieCreate):
    db_movie = models.Movie(**movie.dict())
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie


def get_character(db: Session, character_id: int):
    return db.query(models.Character).filter(models.Character.id == character_id).first()


def get_character_by_ext_id(db: Session, ext_id: int):
    return db.query(models.Character).filter(models.Character.ext_id == ext_id).first()


def get_characters(db: Session):
    return db.query(models.Character).all()


def create_character(db: Session, character: schemas.CharacterCreate):
    db_character = models.Character(**character.dict())
    db.add(db_character)
    db.commit()
    db.refresh(db_character)
    return db_character


def get_quote(db: Session, quote_id: int):
    return db.query(models.Quote).filter(models.Quote.id == quote_id).first()


def get_quote_by_ext_id(db: Session, ext_id: int):
    return db.query(models.Quote).filter(models.Quote.ext_id == ext_id).first()


def get_quote_by_movie_id(db: Session, movie_id: int):
    return db.query(models.Quote).filter(models.Quote.movie_id == movie_id).first()


def get_quote_by_character_id(db: Session, character_id: int):
    return db.query(models.Quote).filter(models.Quote.character_id == character_id).first()


def get_quotes(db: Session):
    return db.query(models.Quote).all()


def create_quote(db: Session, quote: schemas.QuoteCreate, movie_id: int, character_id: int):
    db_quote = models.Quote(**quote.dict(), movie_id=movie_id, character_id=character_id)
    db.add(db_quote)
    db.commit()
    db.refresh(db_quote)
    return db_quote


def get_chapter(db: Session, chapter_id: int):
    return db.query(models.Chapter).filter(models.Chapter.id == chapter_id).first()


def get_chapter_by_ext_id(db: Session, ext_id: int):
    return db.query(models.Chapter).filter(models.Chapter.ext_id == ext_id).first()


def get_chapter_by_name(db: Session, name: int):
    return db.query(models.Chapter).filter(models.Chapter.name == name).first()


def get_chapter_by_book_id(db: Session, book_id: int):
    return db.query(models.Chapter).filter(models.Chapter.book_id == book_id).first()


def get_chapters(db: Session):
    return db.query(models.Chapter).all()


def create_chapter(db: Session, chapter: schemas.ChapterCreate, book_id: int):
    db_chapter = models.Chapter(**chapter.dict(), book_id=book_id)
    db.add(db_chapter)
    db.commit()
    db.refresh(db_chapter)
    return db_chapter
