import os
from flask import Flask, render_template, abort, send_from_directory, render_template, request
from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import current_user

app = Flask(__name__)
application = app

app.config.from_pyfile('config.py')


convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=convention)
db = SQLAlchemy(app, metadata=metadata)
migrate = Migrate(app, db)

from auth import bp as auth_bp, init_login_manager

app.register_blueprint(auth_bp)

init_login_manager(app)

from models import Doctors, Records

@app.route('/')
def index():
    doctors = Doctors.query.all()
    records = None
    if current_user.is_authenticated:
        records = Records.query.all()
        for record in records:
            record.id_doctor = record.doctor.fio
    return render_template('index.html', doctors=doctors, records=records)




