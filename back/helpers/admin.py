from flask_jwt_extended import create_access_token, get_jwt_identity
from datetime import timedelta
from flask import request
from helpers.send_mail import send_mailer_pincode
from config.db import db
from model.tt import *
import bcrypt
import random
import string


def CreateAdmin():
    response = {}

    try:
        ad_password = "foley123"
        hashed_password = bcrypt.hashpw(ad_password.encode('utf-8'), bcrypt.gensalt())
        
        new_admin = Admin()
        new_admin.ad_fullname = "Kraye Roland Landry"
        new_admin.ad_username = "foleykant"
        new_admin.ad_mobile = "0702653594"
        new_admin.ad_email = "krayediego@gmail.com"
        new_admin.ad_password = hashed_password
        
        db.session.add(new_admin)
        db.session.commit()

        response['status'] = 'Succes'

    except Exception as e:
        response['error_description'] = str(e)
        response['status'] = 'error'

    return response


def ReadAllAdmin():

    reponse = {}
    try:
        all_admin = Admin.query.all()
        if all_admin:
            admin_informations = []
            for admin in all_admin:
                admin_infos = {
                    'ad_uid': admin.ad_uid,
                    'ad_fullname': admin.ad_fullname,
                    'ad_username': admin.ad_username,
                    'ad_mobile': admin.ad_mobile,                    
                    'ad_email': admin.ad_email, 
                    'ad_password': admin.ad_password,
                }
                admin_informations.append(admin_infos)
            reponse['status'] = 'success'
            reponse ['admins'] = admin_informations
        else:
            reponse['status'] = 'erreur'
            reponse['motif'] = 'aucun'

    except Exception as e:
        reponse['error_description'] = str(e)
        reponse['status'] = 'error'

    return reponse



def LoginAdmin():
    reponse = {}

    try:
        identifiant = request.json.get('identifiant')
        password = request.json.get('ad_password')
        login_admin = Admin.query.filter((Admin.ad_email == identifiant) | (Admin.ad_username == identifiant)).first()

        if login_admin and bcrypt.checkpw(password.encode('utf-8'), login_admin.ad_password.encode('utf-8')):
            expires = timedelta(hours=1)
            access_token = create_access_token(identity=identifiant)
            rs = {}
            rs['ad_uid'] = login_admin.ad_uid
            rs['ad_fullname'] = login_admin.ad_fullname
            rs['ad_username'] = login_admin.ad_username
            rs['ad_mobile'] = login_admin.ad_mobile
            rs['ad_email'] = login_admin.ad_email

            reponse['status'] = 'success'
            reponse['message'] = 'Login successful'
            reponse['admin_infos'] = rs
            reponse['access_token'] = access_token

        else:
            reponse['status'] = 'error'
            reponse['message'] = 'Invalid username or password'

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
            response['error_description'] = 'Adresse email manquante.'
            return response
        admin = Admin.query.filter_by(ad_email=email).first()
        if not admin:
            response['status'] = 'error'
            response['error_description'] = "Aucun administrateur avec cet email."
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
            response['error_description'] = str(e)

    except Exception as e:
        response['status'] = 'error'
        response['error_description'] = str(e)

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



def UpdateAdmin():

    reponse = {}
    try:
        uid = request.json.get('ad_uid')
        update_admin = Admin.query.filter_by(ad_uid = uid).first()

        if update_admin:
            update_admin.ad_fullname = request.json.get('ad_fullname', update_admin.ad_fullname)
            update_admin.ad_username = request.json.get('ad_username', update_admin.ad_username)            
            update_admin.ad_mobile = request.json.get('ad_mobile', update_admin.ad_mobile)
            update_admin.ad_email = request.json.get('ad_email', update_admin.ad_email)
            db.session.add(update_admin)
            db.session.commit()

            admin_infos = {
                'ad_fullname': update_admin.ad_fullname,
                'ad_username': update_admin.ad_username,
                'ad_mobile': update_admin.ad_mobile,
                'ad_email': update_admin.ad_email,
            }
            reponse['status'] = 'success'
            reponse['admin_infos'] = admin_infos
        else:
            reponse['status'] = 'Admin not found'

    except Exception as e:
        reponse['error_description'] = str(e)
        reponse['status'] = 'error'

    return reponse

    