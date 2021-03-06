from flask import Blueprint, render_template, redirect
import os
import psycopg2
from app.forms import AppointmentForm
from datetime import datetime

bp = Blueprint('main', __name__, '/')

CONNECTION_PARAMETERS = {
    "user": os.environ.get("DB_USER"),
    "password": os.environ.get("DB_PASS"),
    "dbname": os.environ.get("DB_NAME"),
    "host": os.environ.get("DB_HOST"),
}



@bp.route('/', methods=["POST", "GET"])
def main():
    form = AppointmentForm()
    params = {
    'name': form.name.data,
    'start_datetime': datetime.combine(form.start_date.data, form.start_time.data),
    'end_datetime': datetime.combine(form.end_date.data, form.end_time.data),
    'description': form.description.data,
    'private': form.private.data
    }
    if form.validate():
        print('am i in')
        with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
            with conn.cursor() as cursor:
                cursor.execute('''
                        INSERT INTO appointments(name, start_datetime, end_datetime, description, private)
                        VALUES (%(name)s, %(start_datetime)s, %(end_datetime)s, %(description)s, %(private)s);
                    ''',
                    params
                    # {'name': params.name,'start_datetime': params.start_datetime, 'end_datetime': params.end_datetime, 'description': params.description, 'private': params.private},
                    )
                return redirect('/')
    with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
        with conn.cursor() as cursor:
            cursor.execute('''
                SELECT id, name, start_datetime, end_datetime
                FROM appointments
                ORDER BY start_datetime
                '''
            )

            rows = cursor.fetchall()
    return render_template('main.html', rows=rows, form=form)
