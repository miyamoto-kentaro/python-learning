import sqlalchemy
import sqlalchemy.ext.declarative
import sqlalchemy.orm

engine = sqlalchemy.create_engine('sqlite:///test_sqlite')
# if we want to see sql method
# engine = sqlalchemy.create_engine('sqlite:///:memory:',echo=True)



Base = sqlalchemy.ext.declarative.declarative_base()

class Person(Base):
    __tablename__ = 'person'
    id = sqlalchemy.Column(
        sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String(14))

Base.metadata.create_all(engine)

SessionClass = sqlalchemy.orm.sessionmaker(engine)
session = SessionClass()

'''
Create method:
'''
p1 = Person(name='Mike')
session.add(p1)
p2 = Person(name='Nancy')
session.add(p2)
p3 = Person(name='Jun')
session.add(p3)
session.commit()

'''
Edit method:
'''
p4 = session.query(Person).filter_by(name='Mike').first()
p4.name = 'Michel'
session.commit()

'''
Delete method:
'''
p5 = session.query(Person).filter_by(name='Nancy').first()
session.delete(p5)
session.commit()

'''
Get method:
'''
persons = session.query(Person).all()
for person in persons:
    print(person.id,person.name)


