import random
import string
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from datetime import timedelta
from flask import request, jsonify
from helpers.send_mail import send_mailer_pincode
from config.db import db
from model.tt import *
import bcrypt



def CreateTeller():
    rseponse = {}

    try:
        data = request.json
        t_fullname = data.get('t_fullname', '').strip().title()
        t_username = data.get('t_username', '')
        t_mobile = data.get('t_mobile', '')
        t_address = data.get('t_address', '').strip().title()
        t_email = data.get('t_email', '')
        t_password = data.get('t_password', '')
        t_city = data.get('t_city', '').strip().title()

        if not all([t_fullname, t_username, t_mobile, t_address, t_email, t_password, t_city]):
            raise ValueError("All fields are required")
        
        if not t_mobile.isdigit() or len(t_mobile) != 10:
            raise ValueError("Mobile number must contain exactly 10 digits and no other characters")

        if '@' not in t_email:
            raise ValueError("Invalid email address")

        existing_teller = Teller.query.filter((Teller.t_username == t_username) | (Teller.t_email == t_email)).first()
        if existing_teller:
            raise ValueError("Username or email already exists")
        
        new_teller = Teller()
        new_teller.t_fullname = t_fullname
        new_teller.t_username = t_username
        new_teller.t_mobile = t_mobile
        new_teller.t_address = t_address
        new_teller.t_email = t_email
        new_teller.t_password = t_password
        new_teller.t_city = t_city
        new_teller.t_status = 'Active'
        
        db.session.add(new_teller)
        db.session.commit()

        rs = {}
        rs['t_fullname'] = t_fullname
        rs['t_username'] = t_username
        rs['t_mobile'] = t_mobile
        rs['t_address'] = t_address
        rs['t_email'] = t_email
        rs['t_city'] = t_city
        rs['t_status'] = new_teller.t_status
        rs['t_uid'] = new_teller.t_uid

        rseponse['status'] = 'success'
        rseponse['teller_infos'] = rs

    except Exception as e:
        rseponse['status'] = 'error'
        rseponse['error_description'] = str(e)

    return rseponse



def ReadAllTeller():
    reponse = {}

    try:
        all_user = Teller.query.all()
        if all_user:
            teller_informations = []

            for teller in all_user:
                teller_infos = {
                    't_fullname': teller.t_fullname,
                    't_username': teller.t_username,
                    't_mobile': teller.t_mobile,
                    't_address': teller.t_address,
                    't_email': teller.t_email,
                    't_city': teller.t_city,                    
                    't_status': teller.t_status,                    
                    't_uid': teller.t_uid, 
                }
                teller_informations.append(teller_infos)

            reponse['status'] = 'success'
            reponse ['teller'] = teller_informations
        else:
            reponse['status'] = 'erreur'
            reponse['motif'] = 'aucun'

    except Exception as e:
        reponse['error_description'] = str(e)
        reponse['status'] = 'error'

    return reponse



def ReadSingleTeller():

    reponse = {}
    try:
        uid = request.json.get('t_uid')
        single_teller = Teller.query.filter_by(t_uid = uid).first()

        if single_teller:
            teller_infos = {
                't_fullname': single_teller.t_fullname,
                't_username': single_teller.t_username,
                't_mobile': single_teller.t_mobile,
                't_address': single_teller.t_address,
                't_email': single_teller.t_email,
                't_city': single_teller.t_city,                    
                't_status': single_teller.t_status,                    
                't_uid': single_teller.t_uid, 
            }
            reponse['status'] = 'success'
            reponse['teller'] = teller_infos
        else:
            reponse['status'] = 'erreur'
            reponse['motif'] = 'aucun'

    except Exception as e:
        reponse['error_description'] = str(e)
        reponse['status'] = 'error'

    return reponse



def UpdateTeller  ():

    reponse = {}
    try:
        uid = request.json.get('t_uid')
        update_teller = Teller.query.filter_by(t_uid = uid).first()

        if update_teller:
            update_teller.t_fullname = request.json.get('t_fullname', update_teller.t_fullname)
            update_teller.t_username = request.json.get('t_username', update_teller.t_username)            
            update_teller.t_mobile = request.json.get('t_mobile', update_teller.t_mobile)
            update_teller.t_address = request.json.get('t_address', update_teller.t_address)
            update_teller.t_email = request.json.get('t_email', update_teller.t_email)
            update_teller.t_city = request.json.get('t_city', update_teller.t_city)

            db.session.add(update_teller)
            db.session.commit()

            teller_infos = {
                't_fullname': update_teller.t_fullname,
                't_username': update_teller.t_username,
                't_mobile': update_teller.t_mobile,
                't_address': update_teller.t_address,
                't_email': update_teller.t_email,
                't_city': update_teller.t_city,                    
                't_status': update_teller.t_status,                    
                't_uid': update_teller.t_uid, 
            }

            reponse['status'] = 'success'
            reponse['teller_infos'] = teller_infos
        else:
            reponse['status'] = 'Teller not found'

    except Exception as e:
        reponse['error_description'] = str(e)
        reponse['status'] = 'error'

    return reponse


def UpdateStatusTeller  ():

    reponse = {}
    try:
        uid = request.json.get('t_uid')
        update_teller = Teller.query.filter_by(t_uid = uid).first()

        if update_teller:
            update_teller.t_status = request.json.get('t_status', update_teller.t_status)

            db.session.add(update_teller)
            db.session.commit()

            reponse['status'] = 'Succes'
            reponse['teller'] = update_teller
        else:
            reponse['status'] = 'Teller not found'

    except Exception as e:
        reponse['error_description'] = str(e)
        reponse['status'] = 'error'

    return reponse


def DeleteTeller():

    reponse = {}
    try:
        uid = request.json.get('t_uid')
        delete_teller = Teller.query.filter_by(t_uid=uid).first()
        if delete_teller:
            db.session.delete(delete_teller)
            db.session.commit()
            reponse['status'] = 'success'
        else:
            reponse['status'] = 'error'
            reponse['motif'] = 'Teller not found'

    except Exception as e:
        reponse['error_description'] = str(e)
        reponse['status'] = 'error'

    return reponse




def LoginTeller():
    reponse = {}

    try:
        identifiant = request.json.get('identifiant')
        password = request.json.get('t_password')
        login_teller = Teller.query.filter((Teller.t_email == identifiant) | (Teller.t_username == identifiant)).first()

        if login_teller:
            if password == login_teller.t_password:
                expires = timedelta(hours=1)
                access_token = create_access_token(identity=identifiant)
                rs = {}
                rs['t_uid'] = login_teller.t_uid
                rs['t_fullname'] = login_teller.t_fullname
                rs['t_username'] = login_teller.t_username
                rs['t_mobile'] = login_teller.t_mobile
                rs['t_address'] = login_teller.t_address
                rs['t_email'] = login_teller.t_email
                rs['t_password'] = login_teller.t_password
                rs['t_city'] = login_teller.t_city
                rs['t_status'] = login_teller.t_status

                reponse['status'] = 'success'
                reponse['message'] = 'Login successful'
                reponse['teller_infos'] = rs
                reponse['access_token'] = access_token

            else:
                reponse['status'] = 'error'
                reponse['message'] = 'Invalid password'

        else:
            reponse['status'] = 'error'
            reponse['message'] = 'Invalid identifiant'

    except Exception as e:
        reponse['error_description'] = str(e)
        reponse['status'] = 'error'

    return reponse




def generate_temp_password(length=8):
    digits = string.digits  # '0123456789'
    return ''.join(random.choice(digits) for _ in range(length))


def ForgotPassword():
    response = {}
    try:
        email = request.json.get('email')
        if not email:
            response['status'] = 'error'
            response['message'] = 'Adresse email manquante.'
            return response
        admin = Admin.query.filter_by(ad_email=email).first()
        if not admin:
            response['status'] = 'error'
            response['message'] = "Aucun administrateur avec cet email."
            return response
        temp_password = generate_temp_password()
        hashed_password = bcrypt.hashpw(temp_password.encode('utf-8'), bcrypt.gensalt())

        admin.ad_password = hashed_password
        db.session.commit()

        try:
            send_mailer_pincode(admin.ad_email, temp_password)

            response['status'] = 'success'
            response['message'] = 'Envoi du code de réinitialisation réussit'
            response['email'] = email 

        except Exception as e:
            response['status'] = 'error'
            response['message'] = str(e)

    except Exception as e:
        response['status'] = 'error'
        response['message'] = str(e)

    return response


def SaveNewPassword():
    response = {}
    try:
        email = request.json.get('email')
        temp_password = request.json.get('temp_password')
        new_password = request.json.get('new_password')
        admin = Admin.query.filter_by(ad_email=email).first()
        if not admin:
            response['status'] = 'error'
            response['error_description'] = "Aucun administrateur avec cet email."
            return response
        if admin and bcrypt.checkpw(temp_password.encode('utf-8'), admin.ad_password.encode('utf-8')):
            hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
            admin.ad_password = hashed_password
            db.session.commit()
            response['status'] = 'success'
            response['message'] = 'Mot de passe réinitialisé avec succès.'
        else:
            response['status'] = 'error'
            response['message'] = 'Invalid temp_password'

    except Exception as e:
        response['error_description'] = str(e)
        response['status'] = 'error'

    return response