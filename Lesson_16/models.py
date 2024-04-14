from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Создать питоновский файл models.py . Создать таблицу Users определив поля( id: первичный ключ, first_name,last_name:строки длинной в 50 символов, age: целое число).
# Создать “движок” для подключения SQLite и создать таблицу через Base.metadata.create_all(engine)

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    age = Column(Integer)


engine = create_engine('sqlite:///users.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

user_1 = User(first_name='John', last_name='Doe', age=30)
user_2 = User(first_name='Jane', last_name='Smith', age=25)
user_3 = User(first_name='Alice', last_name='Brown', age=35)
user_4 = User(first_name='Bob', last_name='Johnson', age=40)
user_5 = User(first_name='Emily', last_name='Davis', age=27)

session.add_all([user_1, user_2, user_3, user_4, user_5])
session.commit()

# Вывести первых 3 пользователей отсортированных по убыванию возраста
users = session.query(User).order_by(User.age.desc()).limit(3).all()
for user in users:
    print(user.first_name, user.last_name, user.age)

# Вывести пользователей с именем "John"
john_users = session.query(User).filter(User.first_name == 'John').all()
for user in john_users:
    print(user.first_name, user.last_name, user.age)
