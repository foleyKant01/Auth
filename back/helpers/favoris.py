from flask import request
from config.db import db
from model.tt import *
from flask import request, jsonify
from flask import request



def SaveFavoris():
    reponse = {}
    try:
        data = request.get_json()

        bu_name = data.get('bu_name')
        bu_city = data.get('bu_city')      
        bu_uid = data.get('bu_uid')
        user_id = data.get('user_id')
        print(user_id)
        all_favs = Favoris.query.filter_by(bu_uid=bu_uid, u_uid=user_id).first()
        if all_favs:
            rs = {
                'fav_status': all_favs.fa_uid
            }
            reponse['status'] = 'success'
            reponse['fav_infos'] = rs
        else:
            new_fav = Favoris(
                bu_name=bu_name,
                bu_city=bu_city,
                bu_uid=bu_uid,
                u_uid=user_id,
            )
            db.session.add(new_fav)
            db.session.commit()

            rs = {
                'fa_uid': new_fav.fa_uid,
                'bu_name': new_fav.bu_name,
                'bu_city': new_fav.bu_city,
                'bu_uid': new_fav.bu_uid,
                'u_uid': user_id,
                'creation_date': str(new_fav.creation_date)
            }
        reponse['status'] = 'success'
        reponse['fav_infos'] = rs

    except Exception as e:
        reponse['status'] = 'error'
        reponse['error_description'] = str(e)

    return jsonify(reponse)


def ReadAllFavorisByUser():
    reponse = {}
    try:
        user_id = request.json.get('user_id')
        all_favs = Favoris.query.filter_by(u_uid = user_id).all()
        favs_informations = []
        for favs in all_favs:
            business = Business.query.filter_by(bu_uid = favs.bu_uid).first()
            if business:
                is_favs = 1
            else:
                is_favs = 0
            favs_infos = {
                'fa_uid': favs.fa_uid,
                'bu_name': favs.bu_name,
                'bu_description': business.bu_description,
                'bu_categorie': business.bu_categorie,
                'bu_city': favs.bu_city,
                'bu_uid': favs.bu_uid,                    
                'u_uid': favs.u_uid, 
                'is_favs': is_favs,
                'creation_date': str(favs.creation_date),
            }
            favs_informations.append(favs_infos)
        reponse['status'] = 'success'
        reponse ['favs_informations'] = favs_informations
    except Exception as e:
        reponse['error_description'] = str(e)
        reponse['status'] = 'error'

    return reponse


def DeleteFavoris():

    reponse = {}
    try:
        data = request.get_json()
        bu_uid = data.get('bu_uid')
        user_id = data.get('user_id')
        delete_fav = Favoris.query.filter_by(bu_uid=bu_uid, u_uid=user_id).first()
        db.session.delete(delete_fav)
        db.session.commit()
        reponse['status'] = 'success'
        reponse['fav_infos'] = 'Fav deleted'

    except Exception as e:
        reponse['error_description'] = str(e)
        reponse['status'] = 'error'

    return reponse