from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey
from sqlalchemy import insert, select, update, delete

DATABASE_URL = "sqlite:///./platform.db"
engine = create_engine(DATABASE_URL, echo=True)
metadata = MetaData()

# TODO: Define the authors table with id, name, email columns
authors = Table(
    "authors",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(100), nullable=False),
    Column("email", String(100), nullable=False, unique=True)
)
# TODO: Define the articles table with id, title, author_id (ForeignKey with ondelete="CASCADE")
articles = Table(
    "articles",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(200), nullable=False),
    Column("author_id", Integer, ForeignKey("authors.id", ondelete="CASCADE"), nullable=False,
    )
)

#def create_all_tables():
    # TODO: call metadata.create_all(engine)
    #metadata.create_all(engine)

def insert_author(name: str, email: str):
    # TODO: build insert query, execute, commit
    with engine.connect() as conn:
        query = insert(authors).values(name=name, email=email)
        conn.execute(query)
        conn.commit()

def insert_article(author_id: int, title: str):
    with engine.connect() as conn:
        query = insert(articles).values(author_id=author_id, title=title)
        conn.execute(query)
        conn.commit()

def get_articles_by_author(author_id: int):
    with engine.connect() as conn:
        query = select(articles).where(articles.c.author_id == author_id)
        result = conn.execute(query).fetchall()
        return result
    
def update_author_email(author_id: int, new_email: str):
    with engine.connect() as conn:
        query = update(authors).where(authors.c.id == author_id).values(email=new_email)
        conn.execute(query)
        conn.commit()

def delete_author(author_id: int):
    with engine.connect() as conn:
        query = delete(authors).where(authors.c.id == author_id)
        conn.execute(query)
        conn.commit()

if __name__ == "__main__":
    
    #create_all_tables()

    
    insert_author("Alice Chen", "alice@platform.com")
    insert_author("Bob Sharma", "bob@platform.com")
    insert_article(1, "Intro to ORMs")
    insert_article(1, "SQLAlchemy Deep Dive")
    insert_article(2, "Database Design Patterns")

    print(get_articles_by_author(1))

    update_author_email(2, "bob.sharma@platform.com")
    delete_author(2)