from sqlalchemy import create_engine
Database_URL = "sqlite:///./mysqlite.db"

engine = create_engine(Database_URL, echo=True)
