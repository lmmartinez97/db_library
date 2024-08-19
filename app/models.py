from . import db  # Import the SQLAlchemy instance from __init__.py

# Import necessary components from SQLAlchemy
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

# Define the Book model
class Book(db.Model):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    author = Column(String(100), nullable=False)
    published_date = Column(Date, nullable=False)
    publisher = Column(String(100), nullable=False)
    isbn = Column(String(20), nullable=False, unique=True)
    available_copies = Column(Integer, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'
    
# Define the User model
class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)

    loans = relationship('Loan', backref='user')

    def __repr__(self):
        return f'<User {self.username}>'
    
# Define the Loan model
class Loan(db.Model):
    __tablename__ = 'loans'

    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey('books.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    loan_date = Column(Date, nullable=False)
    return_date = Column(Date, nullable=True)
    actual_return_date = Column(Date, nullable=True)

    book = relationship('Book', backref='loans')
    user = relationship('User', backref='loans')

    def __repr__(self):
        return f'<Loan {self.id}>'