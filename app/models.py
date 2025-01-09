from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.orm import relationship
from app.database import Base, engine
from datetime import datetime

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

## 회사 관리
# company
class Company(Base):
    __tabelname__ = "companies"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True) # 회사명
    branch_name = Column(String) # 지점명
    department_name = Column(String) # 부서명
    address = Column(String) # 주소지
    main_phone = Column(String) # 대표번호
    fax_number = Column(String) # FAX 번호
    representative_name = Column(String) # 대표자명
    contact_person = Column(String) # 담당자명
    contact_phone = Column(String) # 담당자연락처

    contracts = relationship("Contract", back_populates="company") # 회사와 계약 1:다

# contact 계약
class contact(Base):
    __tablename__ = "contacts"

Base.metadata.create_all(bind=engine)
