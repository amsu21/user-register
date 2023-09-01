# GRAB DB
from db import db

class UserModel(db.Model):
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    
    def __init__(self, email, password):
        self.email = email
        self.password = password
        
    # FIND BY EMAIL
    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()
    
    # FIND BY ID
    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()
    
    # PASSWORD CONFIRMATION
    @classmethod
    def password_conf(cls, conf_passwd, password):
        return password == conf_passwd
    
    # EMAIL CONFIRMATION
    @classmethod
    def email_conf(cls, conf_email, email):
        return email == conf_email
    
    # GET ALL
    @classmethod
    def get_all(cls):
        return cls.query.all()
    
    # SAVE TO DB
    def db_save(self):
        db.session.add(self)
        db.session.commit()
        
    # DELETE FROM DB
    def db_delete(self):
        db.session.delete(self)
        db.session.commit()
        
    def json(self):
        return {
            'id' : self.id,
            'email' : self.email
        }