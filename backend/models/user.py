from sqlalchemy import Column, Integer, String
from backend.db.session import Base 

class User(Base):
    __tablename__ = "user_info"
    
    id = Column(Integer, primary_key=True) 
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String, nullable=False)

    def __repr__(self):
        return f"<User(username='{self.username}', email='{self.email}')>"