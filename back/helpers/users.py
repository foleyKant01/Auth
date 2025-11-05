from flask_jwt_extended import create_access_token
from datetime import timedelta
from flask import request, jsonify
from config.db import db
from model.tt import *
import bcrypt
from flask import request, jsonify
import bcrypt
import random
import string

   
def CreateUser():

    reponse = {}
    try:
        email = (request.json.get('email'))
        password = (request.json.get('password'))
        motpreferer = (request.json.get('motpreferer'))
        role = (request.json.get('role'))
        confirmpassword = (request.json.get('confirmpassword'))
        if not str(confirmpassword) == str(password):
            return "Mot de passe non conforme"
        
        new_user = User()
        new_user.email = email
        new_user.motpreferer = motpreferer
        new_user.role = role
        new_user.password = password
        
        db.session.add(new_user)
        db.session.commit()

        rs = {}
        rs['uid'] = new_user.uid
        rs['email'] = email
        rs['role'] = role
        rs['creation_date'] = str(new_user.creation_date)


        reponse['status'] = 'success'
        reponse['user_infos'] = rs

    except Exception as e:
        reponse['error_description'] = str(e)
        reponse['status'] = 'error'

    return reponse



def ReadAllUser():
    response = {}
    try:
        users = User.query.filter_by(role='user').all()

        if users:
            user_informations = [
                {
                    'uid': user.uid,
                    'email': user.email,
                    'role': user.role,
                    'creation_date': str(user.creation_date)
                } 
                for user in users
            ]
            response['status'] = 'success'
            response['users'] = user_informations
        else:
            response['status'] = 'erreur'
            response['motif'] = 'aucun utilisateur trouvé'

    except Exception as e:
        response['status'] = 'error'
        response['error_description'] = str(e)

    return response




def ReadSingleUser():

    reponse = {}
    try:
        uid = request.json.get('uid')
        single_user = User.query.filter_by(uid = uid).first_or_404()
        user_infos = {
            'uid': single_user.uid,
            'email': single_user.email,
            'role': single_user.role,
            'creation_date': str(single_user.creation_date),                    
        }
        reponse['status'] = 'success'
        reponse['user'] = user_infos

    except Exception as e:
        reponse['error_description'] = str(e)
        reponse['status'] = 'error'

    return reponse



def UpdateUser  ():

    reponse = {}
    try:
        uid = request.json.get('uid')
        update_user = User.query.filter_by(uid = uid).first_or_404()

        update_user.username = request.json.get('username', update_user.username)            
        update_user.mobile = request.json.get('mobile', update_user.mobile)
        update_user.address = request.json.get('address', update_user.address)
        update_user.email = request.json.get('email', update_user.email)

        db.session.add(update_user)
        db.session.commit()

        reponse['status'] = 'Succes'
        reponse['user'] = update_user


    except Exception as e:
        reponse['error_description'] = str(e)
        reponse['status'] = 'error'

    return reponse


def DeleteUser():

    reponse = {}
    try:
        uid = request.json.get('uid')
        deleteuser = User.query.filter_by(uid=uid).first_or_404()

        db.session.delete(deleteuser)
        db.session.commit()
        reponse['status'] = 'success'

    except Exception as e:
        reponse['error_description'] = str(e)
        reponse['status'] = 'error'

    return reponse



def LoginUser():
    reponse = {}

    try:
        email = request.json.get('email')
        password = request.json.get('password')

        login_user = User.query.filter_by(email=email).first()

        if login_user.password == password:
            rs = {}
            rs['uid'] = login_user.uid
            rs['email'] = login_user.email
            rs['role'] = login_user.role
            rs['creation_date'] = str(login_user.creation_date)

            reponse['status'] = 'success'
            reponse['message'] = 'Login successful'
            reponse['user_infos'] = rs

        else:
            reponse['status'] = 'error'
            reponse['message'] = 'Invalid username or password'

    except Exception as e:
        reponse['status'] = 'error'
        reponse['message'] = str(e)

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
        single_user = User.query.filter_by(email=email).first()
        if not single_user:
            response['status'] = 'error'
            response['message'] = "Aucun utilisateur trouver avec cet email."
            return response
        # temp_password = generate_temp_password()
        # hashed_password = bcrypt.hashpw(temp_password.encode('utf-8'), bcrypt.gensalt())

        single_user.password = hashed_password
        db.session.commit()

        try:
            send_mailer_pincode(single_user.email, temp_password)

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
        motpreferer = request.json.get('motpreferer')
        newpassword = request.json.get('newpassword')
        confirmpassword = request.json.get('confirmpassword')
        
        if newpassword != confirmpassword:
            response['status'] = 'error'
            response['message'] = "Les mots de passe ne correspondent pas."
            return response
        single_user = User.query.filter_by(email=email).first()
        
        if not single_user:
            response['status'] = 'error'
            response['message'] = "Aucun utilisateur avec cet email."
            return response
        
        if single_user.motpreferer == motpreferer:
            single_user.password = newpassword
            db.session.commit()
            response['status'] = 'success'
            response['message'] = 'Mot de passe reinitialise avec succes.'
            
        else:
            response['status'] = 'error'
            response['message'] = 'Code temporaire invalide'

    except Exception as e:
        response['status'] = 'error'
        response['message'] = str(e)

    return response