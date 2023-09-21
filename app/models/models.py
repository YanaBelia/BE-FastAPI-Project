from sqlalchemy import Column, String, Integer, Table, DateTime, Boolean, ForeignKey
from app.my_data.database import Base
from sqlalchemy.ext.declarative import declarative_base
import passlib.hash as _hash
from sqlalchemy.orm import relationship

keyword_tables = Table(
    "company_keywords",
    Base.metadata,
    Column("user_id", ForeignKey("user.id"), primary_key=True),
    Column("company_id", ForeignKey("company.id"), primary_key=True),

)


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    date = Column(DateTime)
    is_active = Column(Boolean, default=False)
    company = relationship("Company", back_populates="owner")


    invite = relationship("Invite", back_populates="user_invite")

    def verify_password(self, password: str):
        return _hash.bcrypt.verify(password, self.password)


class Company(Base):
    __tablename__ = "company"
    id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String)
    description = Column(String, index=True)
    is_visible = Column(Boolean, default=True)
    owner_email = Column(String, ForeignKey("user.email"))
    owner = relationship("User", back_populates="company")
    users = relationship("User", secondary=keyword_tables, back_populates="company")
    # user_id = Column(String, ForeignKey("user.id"))
    company_invite = relationship("Invite", back_populates="company_invite")
    users_emails = Column(String, index=True)

class Invite(Base):
    __tablename__ = 'invite'

    id = Column(Integer, primary_key=True, index=True, unique=True)
    confirm = Column(Boolean, default=False)
    company_id = Column(Integer, ForeignKey('company.id'))
    #
    user_invite = relationship("User", back_populates="invite")
    company_invite = relationship("Company", back_populates="company_invite")
    user_email = Column(String, ForeignKey('user.email'))
    user = Column(String, index=True)

