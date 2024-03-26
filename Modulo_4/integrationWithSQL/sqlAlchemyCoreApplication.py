from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey, text

engine = create_engine('sqlite:///:memory')

metadata = MetaData()
user = Table(
    'user',
    metadata,
    Column('user_id', Integer, primary_key=True),
    Column('user_name', String(40), nullable=False),
    Column('email_address', String(60)),
    Column('nickname', String(50), nullable=False)
)

user_prefs = Table(
    'user_prefs',
    metadata,
    Column('pref_id', Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey('user.user_id'), nullable=False),
    Column('pref_name', String(40), nullable=False),
    Column('pref_value', String(100))
)


for table in metadata.sorted_tables:
    print(table)

#metadata.create_all(engine)

metadata_bd = MetaData()
financials_table = Table(
    'financials',
    metadata_bd,
    Column('id', Integer, primary_key=True),
    Column('value', String(100), nullable=False)
)

print('Infos da tabela financials')
print(financials_table.primary_key)
print(financials_table.constraints)


sql = text('selct * from user')
result = engine.execute(text)
