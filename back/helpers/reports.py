from model.tt import *
from flask import request, jsonify
from datetime import datetime
from collections import defaultdict
from datetime import datetime


def ReportsTeller():
    response = {}
    try:
        t_uid = request.json.get('t_uid')
        if not t_uid:
            return {'status': 'error', 'message': 't_uid manquant'}

        single_user = Teller.query.filter_by(t_uid=t_uid).first()
        if not single_user:
            return {'status': 'error', 'message': 'Teller non trouvé'}

        all_business = Business.query.filter_by(t_uid=t_uid).all()
        all_favoris = Favoris.query.all()
        all_historiques = Historiques.query.all()
        all_publicites_active = Advertisement.query.filter_by(t_uid=t_uid, ad_status=True).all()

        if not all_historiques:
            return {'status': 'error', 'message': 'Historiques manquant'}

        all_vue_this_month = []
        all_business_favoris = []
        vue_counter = defaultdict(int)
        favoris_counter = defaultdict(int)
        bu_info = {}

        for business in all_business:
            bu_uid = business.bu_uid
            bu_info[bu_uid] = {
                'bu_name': business.bu_name,
                'bu_city': business.bu_city,
            }

            # Compter les favoris
            favoris_count = len([f for f in all_favoris if f.bu_uid == bu_uid])
            favoris_counter[bu_uid] = favoris_count

            if favoris_count > 0:
                all_business_favoris.append({
                    'bu_name': business.bu_name,
                    'bu_city': business.bu_city,
                    'bu_uid': bu_uid,
                })

            vues_this_month = [
                h for h in all_historiques
                if h.bu_uid == bu_uid
                and h.visited_at.month == datetime.now().month
                and h.visited_at.year == datetime.now().year
            ]
            if vues_this_month:
                for h in vues_this_month:
                    all_vue_this_month.append({
                        'h_uid': h.h_uid,
                        'textSearch': h.textSearch,
                        'bu_uid': h.bu_uid,
                        'u_uid': h.u_uid,
                        'visited_at': str(h.visited_at)
                    })
                    vue_counter[bu_uid] += 1

        top_entities = sorted(vue_counter.items(), key=lambda x: x[1], reverse=True)[:5]
        most_visited_entities = []

        for bu_uid, vue_count in top_entities:
            most_visited_entities.append({
                'bu_uid': bu_uid,
                'bu_name': bu_info[bu_uid]['bu_name'],
                'vues': vue_count,
                'favoris': favoris_counter.get(bu_uid, 0)
            })

        response['status'] = 'success'
        response['all_business'] = len(all_business)
        response['all_business_favoris'] = len(all_business_favoris)
        response['all_vue_this_month'] = len(all_vue_this_month)
        response['all_publicites_active'] = len(all_publicites_active)
        response['most_visited_entities'] = most_visited_entities

    except Exception as e:
        response['status'] = 'error'
        response['error_description'] = str(e)

    return response

