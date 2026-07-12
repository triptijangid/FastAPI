from database import engine
from sqlalchemy import insert, select, update, delete
from db_tables import users, posts

def insert_user(input_name: str, input_email: str, input_address: str):
    with engine.connect() as connection:
        query = insert(users).values(name=input_name, email = input_email, address = input_address)
        connection.execute(query)
        connection.commit()

def insert_post(input_user_id: int, input_content: str):
    with engine.connect() as connection:
        query = insert(posts).values(user_id=input_user_id, content = input_content)
        connection.execute(query)
        connection.commit()

def get_user_by_id(input_user_id: str):
    with engine.connect() as connetion:
        query = select(users).where(users.c.id == input_user_id)
        result = connetion.execute(query).first()
        return result
    
def get_all_users():
    with engine.connect() as conn:
        # select * from users
        query = select(users)
        result = conn.execute(query).fetchall()
        return result
    
def get_post_by_user_id(input_user_id: int):
    with engine.connect() as conn:
        # select * from users where id = input_user_id
        query = select(posts).where(posts.c.user_id == input_user_id)
        result = conn.execute(query).fetchall()
        return result
    
def update_user_name(input_user_id: int, new_name: str):
    with engine.connect() as conn:
        # update users set name = new_name where user_id = input_user_id
        query = update(users).where(users.c.id == input_user_id).values(name=new_name)
        conn.execute(query)
        conn.commit()

def delete_user_by_id(input_user_id: int):
    with engine.connect() as conn:
        # delete from users where user_id = input_user_id
        query = delete(users).where(users.c.id == input_user_id)
        conn.execute(query)
        conn.commit()