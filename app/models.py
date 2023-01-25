import sqlalchemy as sa
from sqlalchemy.dialects import mysql
import os
from app import db, app
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin 
from flask import url_for

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(100), nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    middle_name = db.Column(db.String(100), nullable=False)
    login = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), unique=True, nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @property
    def full_name(self):
        return ' '.join([self.last_name, self.first_name, self.middle_name or ''])

    def __repr__(self):
        return '<User %r>' % self.login

class Doctors(db.Model):
    __tablename__ = 'doctors'
    id_doctor = db.Column(db.Integer, primary_key=True)
    fio = db.Column(db.String(100), nullable=False)
    work_time = db.Column(db.String(100), nullable=False)
    specialisation = db.Column(db.String(100), nullable=False)
    def __repr__(self):
        return '<Doctor.FIO %r>' % self.fio 

class Records(db.Model):
    __tablename__ = 'records'
    id_record = db.Column(db.Integer, primary_key=True)
    telephone = db.Column(db.String(8), nullable=False)
    code_sms = db.Column(db.String(8), nullable=False)
    id_doctor = db.Column(db.Integer, db.ForeignKey("doctors.id_doctor"), nullable=False)
    time_record = db.Column(db.String(8), nullable=False)
    def __repr__(self):
        return '<Record.Telephone %r>' % self.telephone