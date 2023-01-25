import sqlalchemy as sa
from sqlalchemy.dialects import mysql
import os
from app import db, app
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin 
from flask import url_for

class Doctors(db.Model):
    __tablename__ = 'doctors'
    id_doctor = db.Column(db.Integer, primary_key=True)
    fio = db.Column(db.String(100), nullable=False)
    work_time = db.Column(db.String(100), nullable=False)
    specialisation = db.Column(db.String(100), nullable=False)
    def __repr__(self):
        return '<Doctor.FIO %r>' % self.fio 

class Records(db.Model, UserMixin):
    __tablename__ = 'records'
    id = db.Column(db.Integer, primary_key=True)
    telephone = db.Column(db.String(16), nullable=False)
    code_sms = db.Column(db.String(8), nullable=False)
    id_doctor = db.Column(db.Integer, db.ForeignKey("doctors.id_doctor"), nullable=False)
    time_record = db.Column(db.String(8), nullable=False)

    doctor = db.relationship('Doctors')

    def __repr__(self):
        return '<Record.Telephone %r>' % self.telephone