from flask import request, jsonify
from config.db import db
from model.tt import *
import json
from flask import request, jsonify


def CreateStats():
    try:
        data = request.get_json()
        required_fields = ['textSearch', 'all_business_found', 'city', 'commune', 'longitude', 'latitude']
        for field in required_fields:
            if field not in data:
                return {'status': 'error', 'message': f'Le champ "{field}" est requis.'}

        all_business_json = json.dumps(data['all_business_found']) if isinstance(data['all_business_found'], list) else str(data['all_business_found'])
        new_stat = Stats(
            textSearch=data['textSearch'],
            all_business_found=all_business_json,
            city=data['city'],
            commune=data['commune'],
            longitude=data['longitude'],
            latitude=data['latitude'],
        )

        db.session.add(new_stat)
        db.session.commit()

        return {'status': 'success', 'message': 'Statistique enregistrée avec succès.'}

    except Exception as e:
        print("Erreur lors de la création des stats :", e)
        return {'status': 'error', 'message': 'Une erreur est survenue lors de l’enregistrement des stats.'}



def GetAllStats():
    try:
        # Tu peux ajouter des filtres ici, par exemple par ville
        city = request.args.get('city')
        commune = request.args.get('commune')

        query = Stats.query

        if city:
            query = query.filter(Stats.city.ilike(f'%{city}%'))

        if commune:
            query = query.filter(Stats.commune.ilike(f'%{commune}%'))

        stats = query.order_by(Stats.creation_date.desc()).all()

        result = []
        for stat in stats:
            result.append({
                'uid': stat.uid,
                'textSearch': stat.textSearch,
                'all_business_found': stat.all_business_found,
                'city': stat.city,
                'commune': stat.commune,
                'longitude': stat.longitude,
                'latitude': stat.latitude,
                'creation_date': stat.creation_date.strftime('%Y-%m-%d %H:%M:%S')
            })

        return jsonify({'status': 'success', 'data': result}), 200

    except Exception as e:
        print("Erreur récupération stats :", e)
        return jsonify({'status': 'error', 'message': 'Une erreur est survenue lors de la récupération des statistiques.'}), 500