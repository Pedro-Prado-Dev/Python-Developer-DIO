import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, inspect, select, func
from sqlalchemy.orm import declarative_base, relationship, Session

Base = declarative_base()


class User(Base):
    __tablename__ = 'user_account'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    full_name = Column(String)

    addresses = relationship(
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

with Session(engine) as session:
    pedro = User(
        name='Pedro',
        full_name='Pedro Henrique do Prado',
        addresses=[Address(email_address='pedroppaiva1@hotmail.com')]
    )
    mel = User(
        name='Melyssa',
        full_name='Melyssa Caroline',
        addresses=[Address(email_address='melyssacaroline@hotmail.com'),
                Address(email_address='melyssacaroline@gmail.com')]
    )
    carlos = User(
        name='Carlos',
        full_name='Carlos Paiva'
    )

    session.add_all([pedro, mel, carlos])

    session.commit()

print("Recuperando usúarios a partir de condições de filtragem")
stmt = select(User).where(User.name.in_(['Pedro','Melyssa']))
for result in session.scalars(stmt):
    print(result)

print("\nRecuperando os endereços de e-mail de Melyssa")
stmt_address = select(Address).where(Address.user_id.in_([2]))
for result in session.scalars(stmt_address):
    print(result)

print("\nRecuperando infos de maneira ordenada")
stmt_order_by = select(User).order_by(User.full_name.desc())
for result in session.scalars(stmt_order_by):
    print(result)

print("\nRecuperando infos com join SCALARS")
stmt_join = select(User.full_name, Address.email_address).join_from(Address, User)
for result in session.scalars(stmt_join):
    print(result)

print("\nExecutando statement a partir da connection")
connection = engine.connect()
results = connection.execute(stmt_join).fetchall()
for result in results:
    print(result)

print("\nTotal de registros de User")
stmt_count = select(func.count('*')).select_from(User)
for result in session.scalars(stmt_count):
    print(result)