from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey, insert, select

Database_URL = "sqlite:///./course.db"

engine = create_engine(Database_URL, echo=True)

metadata = MetaData()

instructors = Table(
    "instructors", 
    metadata,
    Column("instructor_id", Integer, primary_key=True),
    Column("name", String, nullable=False)
)

batches = Table(
    "batches",
    metadata,
    Column("batch_id", Integer, primary_key=True),
    Column("batch_name", String, nullable=False),
    Column("instructor_id", Integer, ForeignKey("instructors.instructor_id"), nullable=False)
)

metadata.create_all(engine)

def insert_instructors(instructor_id: int, name: str):
    with engine.connect() as conn:
        query = insert(instructors).values(instructor_id=instructor_id, name=name)
        conn.execute(query)
        conn.commit()

#insert_instructors(1, "Meera")
#insert_instructors(2, "Aman")

def insert_batches(batch_id: int, batch_name: str, instructor_id: int):
    with engine.connect() as conn:
        query = insert(batches).values(batch_id=batch_id, batch_name=batch_name, instructor_id=instructor_id)
        conn.execute(query)
        conn.commit()

def get_batches_by_id(instructor_id: str):
    with engine.connect() as connetion:
        query = select(batches).where(batches.c.instructor_id == instructor_id)
        result = connetion.execute(query).fetchall()
        return result

insert_batches(1, "Backend Sprint A", 1)
insert_batches(2, "Backend Sprint B", 1)
insert_batches(3, "Backend Sprint C", 2)

print(get_batches_by_id(1))
