import hashlib
from database.database import get_db
import config
from flask import redirect, url_for, render_template
import forms


class UserService():

    @staticmethod
    def verify(login, password):
        db = get_db()
        hashed_password = hashlib.sha256(password.encode('utf-8'))
        user = db.execute('''
            SELECT *
            FROM users 
            WHERE login_name = ? AND login_password = ?''', [login, hashed_password.hexdigest()]).fetchone()
        if user:
            return user
        else:
            return None

    @staticmethod
    def getAllEmployees():
        db = get_db()
        user = db.execute(''' 
            SELECT *
            FROM users
            WHERE position != "Customer"
        ''').fetchall()
        return user

    @staticmethod
    def getAllCustomers():
        db = get_db()
        user = db.execute(''' 
            SELECT *
            FROM users
            WHERE position = "Customer"
        ''').fetchall()
        return user

    @staticmethod
    def getUserById(login_name):
        db = get_db()
        user = db.execute(''' 
            SELECT *
            FROM users
            WHERE login_name = ?
        ''', [login_name]).fetchone()
        return user

    @staticmethod
    def updateUser(login, new_email, new_first_name, new_password):
        db = get_db()
        user = db.execute(''' 
                UPDATE users
                SET first_name = ?, email = ?, login_password = ?
                where login_name = ?
            ''', [new_first_name, new_email, new_password, login]).fetchone()
        db.commit()
        return user

    @staticmethod
    def insertNewUser(new_position, new_first_name, new_last_name, new_phone_number, new_email, new_hourly_wage,
                      new_login_name, new_password, new_company_id, new_active):
        db = get_db()
        hashed_password = hashlib.sha256(new_password.encode('utf-8'))
        db.execute('''INSERT INTO users (position, first_name, last_name, phone_number, email, hourly_wage, login_name, login_password, company_company_id, active) 
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                   [new_position, new_first_name, new_last_name, new_phone_number, new_email, new_hourly_wage,
                    new_login_name, hashed_password.hexdigest(), new_company_id, new_active]
                   )
        db.commit()

    @staticmethod
    def updateUserActivity(login, activenew):
        db = get_db()
        user = db.execute(''' 
                 UPDATE users
                 SET active = not ?
                 where login_name = ?
             ''', [activenew, login]).fetchone()
        db.commit()