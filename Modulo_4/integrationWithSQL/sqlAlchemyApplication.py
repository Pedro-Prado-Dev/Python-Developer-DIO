import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, inspect
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class User(Base):
    __tablename__ = 'user_account'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    full_name = Column(String)

    address = relationship(
        'Address', back_populates='user', cascade='all, delete-orphan'
    )

    def __repr__(self):
        return f'User (id={self.id}, name={self.name}, full_name={self.full_name})'


class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True, autoincrement=True)
    email_address = Column(String(50), unique=True, nullable=False)
    user_id = Column(Integer, ForeignKey('user_account.id'), nullable=False)

    user = relationship(
        'User', back_populates='addresses'
    )

    def __repr__(self):
        return f'Address (id={self.id}, email={self.email_address})'


engine = create_engine("sqlite://")

Base.metadata.create_all(engine)

inspetor_engine = inspect(engine)

