from sqlalchemy import create_engine
from config import Config

engine = create_engine(Config.DATABASE_URI)