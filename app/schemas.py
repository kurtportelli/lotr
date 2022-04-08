from pydantic import BaseModel


class ChapterBase(BaseModel):
    ext_id: str
    name: str


class ChapterCreate(ChapterBase):
    pass


class Chapter(ChapterBase):
    id: int
    book_id: int

    class Config:
        orm_mode = True


class BookBase(BaseModel):
    ext_id: str
    name: str


class BookCreate(BookBase):
    pass


class Book(BookBase):
    id: int
    chapters: list[Chapter] = []

    class Config:
        orm_mode = True


class QuoteBase(BaseModel):
    ext_id: str
    dialog: str


class QuoteCreate(QuoteBase):
    pass


class Quote(QuoteBase):
    id: int
    movie_id: int
    character_id: int

    class Config:
        orm_mode = True


class MovieBase(BaseModel):
    ext_id: str
    name: str
    runtime_in_minutes: int
    budget_in_millions: int
    box_office_revenue_in_millions: int
    academy_award_nominations: int
    academy_award_wins: int
    rotten_tomatoes_score: int


class MovieCreate(MovieBase):
    pass


class Movie(MovieBase):
    id: int
    quotes: list[Quote] = []

    class Config:
        orm_mode = True


class CharacterBase(BaseModel):
    ext_id: str
    height: int
    race: str
    gender: str
    birth: str
    spouse: str
    death: str
    realm: str
    hair: str
    name: str
    wiki_url: str


class CharacterCreate(CharacterBase):
    pass


class Character(CharacterBase):
    id: int
    quotes: list[Quote] = []

    class Config:
        orm_mode = True
