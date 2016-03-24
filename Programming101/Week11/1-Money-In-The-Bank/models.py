from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from sqlalchemy import Column, Integer, Float, String, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()


class Client(Base):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    salt = Column(String)
    balance = Column(Float)
    message = Column(String)


class LoginAttempt(Base):
    __tablename__ = "login_attempts"
    id = Column(Integer, primary_key=True)
    attempt_status = Column(String)
    timestamp = Column(DateTime)
    client = relationship(Client, backref="login_attempts")


class BlockedUser(Base):
    __tablename__ = "blocked_users"
    id = Column(Integer, primary_key=True)
    client_id = Column(String, ForeignKey(Client.id))
    block_start = Column(DateTime)
    block_end = Column(DateTime)
    client = relationship(Client, backref="blocked_users")

engine = create_engine("sqlite:///university.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
