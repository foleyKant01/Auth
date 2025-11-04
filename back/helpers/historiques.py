from flask import request
from config.db import db
from model.tt import *
from flask import request


def SaveHistorique():

    reponse = {}
    try:
        textSearch = (request.json.get('textSearch'))
        bu_uid = (request.json.get('bu_uid'))
        u_uid = (request.json.get('u_uid'))
        
        new_historiques = Historiques()
        new_historiques.textSearch = textSearch
        new_historiques.bu_uid = bu_uid
        new_historiques.u_uid = u_uid
        
        db.session.add(new_historiques)
        db.session.commit()

        rs = {}
        rs['h_uid'] = new_historiques.h_uid
        rs['textSearch'] = new_historiques.textSearch
        rs['bu_uid'] = new_historiques.bu_uid
        rs['u_uid'] = new_historiques.u_uid
        rs['visited_at'] = str(new_historiques.visited_at)

        reponse['status'] = 'success'
        reponse['histo_infos'] = rs

    except Exception as e:
        reponse['error_description'] = str(e)
        reponse['status'] = 'error'

    return reponse


def ReadAllHistoriqueByUser():
    reponse = {}
    try:
        user_id = request.json.get('user_id')
        all_histo = Historiques.query.filter_by(u_uid=user_id).all()
        if all_histo:
            print('histo found')
            histo_informations = []
            for histo in all_histo:
                single_business = Business.query.filter_by(bu_uid=histo.bu_uid).first()
                if single_business:
                    histo_infos = {
                        'h_uid': histo.h_uid,
                        'textSearch': histo.textSearch,
                        'bu_uid': single_business.bu_uid,
                        'bu_name': single_business.bu_name,
                        'bu_description': single_business.bu_description[:150]+"..." if len(single_business.bu_description) > 150 else single_business.bu_description,
                        'u_uid': histo.u_uid,
                        'visited_at': str(histo.visited_at),
                    }
                    histo_informations.append(histo_infos)  # Ajout seulement si complet
            reponse['status'] = 'success'
            reponse['histo_informations'] = histo_informations
        else:
            reponse['status'] = 'erreur'
            reponse['motif'] = 'aucun'
    except Exception as e:
        reponse['error_description'] = str(e)
        reponse['status'] = 'error'

    return reponse


def DeleteHistoriques():
    reponse = {}
    try:
        h_uid = request.json.get('h_uid')
        delete_histo = Historiques.query.filter_by(h_uid=h_uid).first()
        
        if delete_histo is None:
            reponse['status'] = 'error'
            reponse['error_description'] = f"Aucun historique trouvé avec h_uid = {h_uid}"
            return reponse
        
        db.session.delete(delete_histo)
        db.session.commit()
        reponse['status'] = 'success'

    except Exception as e:
        reponse['error_description'] = str(e)
        reponse['status'] = 'error'

    return reponse
