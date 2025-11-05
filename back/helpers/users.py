from config.db import db
from model.tt import *
from flask import request
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