import os
from flask import jsonify, request
import uuid
from config.db import db
from config.constant import *
from model.tt import Business, Favoris
from werkzeug.utils import secure_filename


from flask import request, jsonify, current_app as app
from sqlalchemy import or_
import re
import unicodedata
import math
from flask import Flask
import requests
# from config.constant import OVERPASS_URL, NOMINATIM_UA, OPENAI_API_KEY, OPENAI_MODEL




if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def upload_file():
    if request.method == 'PATCH' or request.method == 'POST':
        print('is post')
        if 'bu_picture' not in request.files:
            return None  # Champ de fichier manquant
        file = request.files['bu_picture']
        print(file.filename)
        if file.filename == '':
            return None  # Nom de fichier vide
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)  # Nettoyer le nom de fichier
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            return filename


def CreateBusiness():
    
    response = {}   
    try:
        new_business = Business()
        new_business.bu_categorie = request.form.get('categorie')
        new_business.bu_type = request.form.get('type')
        new_business.bu_name = request.form.get('name')
        new_business.bu_description = request.form.get('description')
        new_business.bu_city = request.form.get('city')
        new_business.bu_website = request.form.get('website')
        new_business.bu_address = request.form.get('address')
        new_business.phone = request.form.get('phone')
        new_business.t_uid = request.form.get('t_uid')
        new_business.bu_status = 'Active'
        latitude = request.form.get('latitude')
        longitude = request.form.get('longitude')
        if latitude:
            new_business.latitude = latitude
        else:
            new_business.latitude = None

        if longitude:
            new_business.longitude = longitude
        else:
            new_business.longitude = None
        
        db.session.add(new_business)
        db.session.commit()

        # rs = {}
        # rs['bu_uid'] = new_business.bu_uid
        # rs['bu_categorie'] = new_business.bu_categorie
        # rs['bu_type'] = new_business.bu_type
        # rs['bu_name'] = new_business.bu_name
        # rs['bu_description'] = new_business.bu_description
        # rs['bu_city'] = new_business.bu_city
        # rs['bu_address'] = new_business.bu_address
        # rs['phone'] = new_business.phone
        # rs['bu_picture'] = new_business.bu_picture
        # rs['t_uid'] = new_business.t_uid
        # rs['bu_status'] = new_business.bu_status
        # # rs['latitude'] = new_business.latitude
        # # rs['longitude'] = new_business.longitude

        response['status'] = 'success'
        # response['business_infos'] = rs

    except Exception as e:
        response['error_description'] = str(e)
        response['status'] = 'error'

    return response


def InsertAllBusiness():
    response = {}
    business_data = [
        {
            "name":"Pharmacie BERACA",
            "description":"Pharmacie à Yopougon camp militaire petit toit rouge.",
            "city":"Yopougon, Abidjan",
            "address":"camp militaire petit toit rouge",
            "phone":"0709264899",
            "latitude":"5.3185692037751515",
            "longitude":"-4.064772275183709"
        },
        {
            "name":"Pharmacie d'Azito",
            "description":"Pharmacie à Yopougon Niangon Sud.",
            "city":"Yopougon, Abidjan",
            "address":"Niangon Sud",
            "phone":"",
            "latitude":"5.309766171932483",
            "longitude":"-4.087227882712183"
        },
        {
            "name":"Pharmacie Jean-Pierre",
            "description":"Pharmacie à Yopougon Niangon.",
            "city":"Yopougon, Abidjan",
            "address":"Niangon à droite",
            "phone":"2723463003",
            "latitude":"5.322044320521317",
            "longitude":"-4.103301775183712"
        },
        {
            "name":"Pharmacie Artémia",
            "description":"Pharmacie à Yopougon sideci vers le palais de justice.",
            "city":"Yopougon, Abidjan",
            "address":"sideci vers le palais de justice",
            "phone":"",
            "latitude":",5.326668819713181",
            "longitude":"-4.07716151751357"
        },
        {
            "name":"Pharmacie Boissy",
            "description":"Pharmacie à Yopougon Toits Rouges.",
            "city":"Yopougon, Abidjan",
            "address":"En face du Commissariat du 19eme Arrondissement - Toits Rouges",
            "phone":"",
            "latitude":"5.327374219589805",
            "longitude":"-4.051069490523946" 
        },
        {
            "name":"Pharmacie Nouveau Quartier",
            "description":"Pharmacie à Yopougon (ABOBODOUME/LOCODJORO).",
            "city":"Yopougon, Abidjan",
            "address":"Nouveau Quartier après le Restaurant OBV Complexe,",
            "phone":"0759997081",
            "latitude":"5.339151108898771",
            "longitude":"-4.062492481943854"
        },
        {
            "name":"Pharmacie Yasmine Du Nouveau Quartier",
            "description":"Pharmacie à Yopougon Toit-Rouge.",
            "city":"Yopougon, Abidjan",
            "address":"Toit-Rouge,",
            "phone":"",
            "latitude":"5.331905699219375",
            "longitude":"-4.052521366211607"
        },
        {
            "name":"Pharmacie Yasine",
            "description":"Pharmacie à Yopougon Toit-Rouge.",
            "city":"Yopougon, Abidjan",
            "address":"Toit-Rouge,",
            "phone":"",
            "latitude":"5.331841028654585",
            "longitude":"-4.055249333214012"
        },
        {
            "name":"Pharmacie Toit-Rouge",
            "description":"Pharmacie à Yopougon Toit-Rouge.",
            "city":"Yopougon, Abidjan",
            "address":"Toit-Rouge,",
            "phone":"",
            "latitude":"5.331685819271328",
            "longitude":"-4.055619557307197"
        },
        {
            "name":"Pharmacie Sainte Rita",
            "description":"Pharmacie à Yopougon Niangon Nord.",
            "city":"Yopougon, Abidjan",
            "address":"T 112 Non loin de l'Eglise Ste Rita de Cascia, Niangon Nord",
            "phone":"",
            "latitude":"5.3284358441889115",
            "longitude":"-4.096425493790921"
        },
        {
            "name":"Pharmacie Beyniouah",
            "description":"Pharmacie à Yopougon Niangon Nord.",
            "city":"Yopougon, Abidjan",
            "address":"Niangon Nord pas loin du CENTRE MEDICALE SAINT THEOPHILE D'ESPERANCE",
            "phone":"",
            "latitude":"5.323051853870414",
            "longitude":"-4.093593081333024"
        },
        {
            "name":"Pharmacie Niangon Nord",
            "description":"Pharmacie à Yopougon Niangon Nord.",
            "city":"Yopougon, Abidjan",
            "address":"Niangon Nord",
            "phone":"",
            "latitude":"5.329538305782463",
            "longitude":"-4.102396041563789"
        },
                {
            "name":"Pharmacie Esther",
            "description":"Pharmacie à Yopougon Niangon Nord.",
            "city":"Yopougon, Abidjan",
            "address":"Niangon Nord",
            "phone":"",
            "latitude":"5.326159321549768",
            "longitude":"-4.105925808265"
        }, 
        {
            "name":"Pharmacie de la cité verte",
            "description":"Pharmacie à Yopougon cité verte.",
            "city":"Yopougon, Abidjan",
            "address":"Cité verte",
            "phone":"",
            "latitude":"5.32782784772088",
            "longitude":"-4.110054547937452"
        },
        {
            "name":"Pharmacie Théodora",
            "description":"Pharmacie à Yopougon Niangon Sud.",
            "city":"Yopougon, Abidjan",
            "address":"Niangon Sud non loin de CLINIQUE MEDICALE ELITE",
            "phone":"",
            "latitude":"5.31880674123772",
            "longitude":"-4.094811350342529"
        },
        {
            "name":"Pharmacie des ESPERANCES",
            "description":"Pharmacie à Yopougon Niangon Sud.",
            "city":"Yopougon, Abidjan",
            "address":"Yopougon à droite non loin du carrefour Super Sonia",
            "phone":"",
            "latitude":"5.31914392908887",
            "longitude":"-4.0994704273674"
        },
        {   
            "name":"Pharmacie Le LOTUS",
            "description":"Pharmacie à Yopougon Niangon Sud.",
            "city":"Yopougon, Abidjan",
            "address":"Non loin du carrefour allocodrome de Niangon",
            "phone":"2723455797",
            "latitude":"5.317192737877698", 
            "longitude":"-4.08884491291708"
        },
        {
            "name":"Pharmacie Niangon Lokoa",
            "description":"Pharmacie à Yopougon Niangon Sud.",
            "city":"Yopougon, Abidjan",
            "address":"Non loin du LYCÉE MUNICIPAL SIMONE EHIVET GBAGBO",
            "phone":"0546406090",
            "latitude":"5.314795754025947",
            "longitude":"-4.099958907954671"
        },
        {
            "name":"Pharmacie Santa Caterina",
            "description":"Pharmacie à Yopougon Sicogi.",
            "city":"Yopougon, Abidjan",
            "address":"Yopougon Sicogi",
            "phone":"0777677980",
            "latitude":"5.337584875897572",
            "longitude":"-4.075430338884962"
        },
        {
            "name":"Pharmacie Wakouboué",
            "description":"Pharmacie à Yopougon score.",
            "city":"Yopougon, Abidjan",
            "address":"Yopougon score",
            "phone":"0102759915",
            "latitude":"5.339879271504288",
            "longitude":"-4.073674731590526"
        },
        {
            "name":"Pharmacie du 16ème",
            "description":"Pharmacie à Yopougon 16ème.",
            "city":"Yopougon, Abidjan",
            "address":"Non loin du Commissariat du 16ème Arrondissement",
            "phone":"",
            "latitude":"5.3374547290430625",
            "longitude":"-4.0712021270009595"
        },
        {
            "name":"Pharmacie du Marché",
            "description":"Pharmacie à Yopougon Sicogi marché.",
            "city":"Yopougon, Abidjan",
            "address":"Sicogi marché",
            "phone":"0153507272",
            "latitude":"5.337421996569971",
            "longitude":"-4.079113517293957"
        },
        {
            "name":"Pharmacie Saint Raphael",
            "description":"Pharmacie à Yopougon.",
            "city":"Yopougon, Abidjan",
            "address":"Après la Cité novalim en allant vers Amondji",
            "phone":"",
            "latitude":"5.341550680934795",
            "longitude":"-4.087480291909348"
        },
        {
            "name":"Pharmacie Sainte Aude",
            "description":"Pharmacie à Yopougon Siporex.",
            "city":"Yopougon, Abidjan",
            "address":"Siporex non loin du Collège I.P.E.S Yopougon siporex",
            "phone":"",
            "latitude":"5.355570582995303",
            "longitude":"-4.077459571990685"
        },
        {
            "name":"Pharmacie Notre Dame des Victoires",
            "description":"Pharmacie à Yopougon Millionnaire.",
            "city":"Yopougon, Abidjan",
            "address":"Yopougon Millionnaire,",
            "phone":"",
            "latitude":"5.340504988230851",
            "longitude":"-4.0480040463486"
        },
        {
            "name":"Pharmacie Mère de Grâces",
            "description":"Pharmacie à Yopougon.",
            "city":"Yopougon, Abidjan",
            "address":"Yopougon,",
            "phone":"",
            "latitude":"5.355569432644565",
            "longitude":"-4.0526051905238685"
        },
        {
            "name":"Pharmacie du Millionnaire",
            "description":"Pharmacie à Yopougon Millionnaire.",
            "city":"Yopougon, Abidjan",
            "address":"Yopougon Millionnaire après Institut Des Aveugles,",
            "phone":"0101999409",
            "latitude":"5.352282420224109",
            "longitude":"-4.0587220058082085"
        },
        {
            "name":"Pharmacie d'Abobo-Doumé",
            "description":"Pharmacie à Yopougon (Abobodoumé).",
            "city":"Yopougon, Abidjan",
            "address":"Abobodoumé non loin du Lycée Municipal Attécoubé,",
            "phone":"0171288572",
            "latitude":"5.314760621792708",
            "longitude":"-4.035553132853881"
        },
        {
            "name":"Pharmacie Maison Blanche",
            "description":"Pharmacie à Yopougon Maison Blanche.",
            "city":"Yopougon, Abidjan",
            "address":"Maison Blanche,",
            "phone":"2723461453",
            "latitude":"5.347638444605589",
            "longitude":"-4.082718317513527"
        },
        {
            "name":"Pharmacie Niangon Sud",
            "description":"Pharmacie à Yopougon Niangon Sud.",
            "city":"Yopougon, Abidjan",
            "address":"Niangon Sud",
            "phone":"",
            "latitude":"5.315909052366288",
            "longitude":"-4.091707146348606"
        },
        {
            "name":"Pharmacie Che N'Tale",
            "description":"Pharmacie à Yopougon Annaneraie.",
            "city":"Yopougon, Abidjan",
            "address":"Yopougon Annaneraie",
            "phone":"",
            "latitude":"5.351123813205555",
            "longitude":"-4.096807834145619"
        },
        {
            "name":"Pharmacie Forêts",
            "description":"Pharmacie à l'entré de la CITÉ ADO.",
            "city":"Yopougon, Abidjan",
            "address":"Yopougon",
            "phone":"",
            "latitude":"5.401466586512199",
            "longitude":"-4.084942453095683"
        },
        {
            "name":"Pharmacie La Rosée de l'Hermon",
            "description":"Pharmacie à Yopougon .",
            "city":"Yopougon, Abidjan",
            "address":"Niangon Sud non de Académie Diop",
            "phone":"",
            "latitude":"5.31645940417997",
            "longitude":"-4.110178577029194"
        },
        {
            "name":"Pharmacie SIDECI Extension",
            "description":"Pharmacie à Yopougon (SIDECI).",
            "city":"Yopougon, Abidjan",
            "address":"SIDECI Extension",
            "phone":"0758094604",
            "latitude":"5.323787085329905",
            "longitude":"-4.08320927518366"
        },

        {
            "name":"Pharmacie Christ Roi carrefour Jean Paul 2",
            "description":"Pharmacie Christ Roi carrefour Jean Paul 2 à Yopougon Toit rouge.",
            "city":"Yopougon, Abidjan",
            "address":"Carrefour Jean Paul 2 à Yopougon Toit rouge",
            "phone":"0789912806",
            "latitude":"5.330980234560304",
            "longitude":"-4.047439793754489"
        },
        {
            "name":"Pharmacie Christ Roi",
            "description":"Pharmacie à Yopougon.",
            "city":"Yopougon, Abidjan",
            "address":" Avant le poste De Péage du 4ième Pont Yopougon côté toit rouge,",
            "phone":"",
            "latitude":"5.336374837723524",
            "longitude":"-4.042472343153809"
        },
        {
            "name":"Pharmacie Saint Aubin",
            "description":"Pharmacie Saint Aubin Vers Agbayate 1 au Carrefour mosquée blanche",
            "city":"Yopougon, Abidjan",
            "address":"Vers Agbayate 1 au Carrefour mosquée blanche",
            "phone":"0546053436",
            "latitude":"5.31404255646737",
            "longitude":"-4.043811804018835"
        },
        {
            "name":"Pharmacie de Locodjro",
            "description":"Pharmacie Locodjro à Yopougon (Locodjro).",
            "city":"Yopougon, Abidjan",
            "address":"Locodjro, Yopougon,",
            "phone":"L",
            "latitude":"5.332581041431064",
            "longitude":"-4.04178014454388"
        },
        {
            "name":"Pharmacie Saint Martin Faya",
            "description":"Pharmacie à Yopougon (Faya).",
            "city":"Yopougon, Abidjan",
            "address":"Faya, Yopougon,",
            "phone":"Faya, Yopougon,",
            "latitude":null,
            "longitude":null
        },
        {
            "name":"Pharmacie La Vie Yopougon",
            "description":"Pharmacie à Yopougon.",
            "city":"Yopougon, Abidjan",
            "address":"Yopougon,",
            "phone":"Yopougon,",
            "latitude":null,
            "longitude":null
        },
        {
            "name":"Pharmacie Progrès",
            "description":"Pharmacie à Yopougon.",
            "city":"Yopougon, Abidjan",
            "address":"Yopougon,",
            "phone":"Yopougon,",
            "latitude":null,
            "longitude":null
        },
        {
            "name":"Pharmacie Beyniouah",
            "description":"Pharmacie à Yopougon (Niangon).",
            "city":"Yopougon, Abidjan",
            "address":"Niangon, Yopougon,",
            "phone":"Niangon, Yopougon,",
            "latitude":null,
            "longitude":null
        },
        {
            "name":"Nouvelle Pharmacie Awalé",
            "description":"Pharmacie à Yopougon.",
            "city":"Yopougon, Abidjan",
            "address":"Yopougon,",
            "phone":"Yopougon,",
            "latitude":null,
            "longitude":null
        },
        {
            "name":"Pharmacie Saint Raphaël",
            "description":"Pharmacie à Yopougon.",
            "city":"Yopougon, Abidjan",
            "address":"Yopougon,",
            "phone":"Yopougon,",
            "latitude":null,
            "longitude":null
        },

        {
            "name":"Pharmacie Carrefour Pompier",
            "description":"Pharmacie à Yopougon (carrefour pompier).",
            "city":"Yopougon, Abidjan",
            "address":"Carrefour Pompier, Yopougon,",
            "phone":"Carrefour Pompier, Yopougon,",
            "latitude":null,
            "longitude":null
        },
        {
            "name":"Pharmacie CELIA",
            "description":"Pharmacie à Yopougon.",
            "city":"Yopougon, Abidjan",
            "address":"Yopougon,",
            "phone":"Yopougon,",
            "latitude":null,
            "longitude":null
        },
        {
            "name":"Pharmacie RABBI",
            "description":"Pharmacie à Yopougon.",
            "city":"Yopougon, Abidjan",
            "address":"Yopougon,",
            "phone":"Yopougon,",
            "latitude":null,
            "longitude":null
        },
        {
            "name":"Pharmacie Penfina",
            "description":"Pharmacie à Yopougon.",
            "city":"Yopougon, Abidjan",
            "address":"Yopougon,",
            "phone":"Yopougon,",
            "latitude":null,
            "longitude":null
        },
        {
            "name":"Pharmacie Assonvon",
            "description":"Pharmacie à Yopougon.",
            "city":"Yopougon, Abidjan",
            "address":"Yopougon Assonvon,",
            "phone":"Yopougon Assonvon,",
            "latitude":null,
            "longitude":null
        },
        {
            "name":"Pharmacie de la Félicité",
            "description":"Pharmacie à Yopougon.",
            "city":"Yopougon, Abidjan",
            "address":"Yopougon,",
            "phone":"Yopougon,",
            "latitude":null,
            "longitude":null
        },
        {
            "name":"Pharmacie Saint Clément (SARL)",
            "description":"Pharmacie à Yopougon.",
            "city":"Yopougon, Abidjan",
            "address":"Yopougon,",
            "phone":"Yopougon,",
            "latitude":null,
            "longitude":null
        },
        {
            "name":"Pharmacie W. Ponty (William Ponty)",
            "description":"Pharmacie à Yopougon (SICOGI, face collège William Ponty).",
            "city":"Yopougon, Abidjan",
            "address":"SICOGI, Yopougon,",
            "phone":"SICOGI, Yopougon,",
            "latitude":null,
            "longitude":null
        },
        {
            "name":"Pharmacie Sainte Marie",
            "description":"Pharmacie à Yopougon.",
            "city":"Yopougon, Abidjan",
            "address":"Yopougon,",
            "phone":"Yopougon,",
            "latitude":null,
            "longitude":null
        },

        {
            "name":"Nouvelle Pharmacie Principale (Yopougon)",
            "description":"En face de la place Ficgayo, à côté de COSMOS (Yopougon).",
            "city":"Yopougon, Abidjan",
            "address":"Ficgayo, Yopougon, (face COSMOS)",
            "phone":"Ficgayo, Yopougon, (face COSMOS)",
            "latitude":null,
            "longitude":null
        },
        {
            "name":"Pharmacie de la Mairie de Yopougon",
            "description":"À 200 m de la Mairie, face au maquis Tantie Margot (ligne bus 30 – Selmer).",
            "city":"Yopougon, Abidjan",
            "address":"Selmer, Yopougon,",
            "phone":"Selmer, Yopougon,",
            "latitude":null,
            "longitude":null
        }
    ]

    for business in business_data:
        existing = Business.query.filter_by(bu_name=business["name"]).first()
        if not existing:
            db.session.add(Business(
                bu_categorie='Pharmacie',
                bu_type='physique',
                bu_name=business["name"],
                bu_description=business["description"],
                bu_city=business["city"],
                bu_address=business["address"],
                phone=business["phone"],
                bu_status="Active",  # ou Active si c'est une constante
                latitude=business["latitude"],
                longitude=business["longitude"],
                t_uid=request.json.get('t_uid')
            ))

    db.session.commit()
    print("Business enregistrées avec succès.")
    response['status'] = 'Business enregistrées avec succès.'
    return response


def UpdateBusiness():
    response = {}

    try:
        bu_uid = request.form.get('bu_uid')
        update_business = Business.query.filter_by(bu_uid=bu_uid).first()

        if update_business:
            update_business.bu_type = request.form.get('bu_type', update_business.bu_type)
            update_business.bu_name = request.form.get('bu_name', update_business.bu_name)
            update_business.bu_description = request.form.get('bu_description', update_business.bu_description)
            update_business.bu_city = request.form.get('bu_city', update_business.bu_city)
            update_business.bu_website = request.form.get('bu_website', update_business.bu_website)
            update_business.phone = request.form.get('phone', update_business.phone)
            update_business.bu_address = request.form.get('bu_address', update_business.bu_address)

            # Gestion sécurisée de latitude / longitude
            def safe_float(value, default=None):
                try:
                    return float(value)
                except (TypeError, ValueError):
                    return default

            update_business.latitude = safe_float(request.form.get('latitude'), update_business.latitude)
            update_business.longitude = safe_float(request.form.get('longitude'), update_business.longitude)

            # # Upload image si présente
            # uploaded_image = upload_file()
            # if uploaded_image:
            #     update_business.bu_picture = uploaded_image

            db.session.commit()

            business_info = {
                'bu_uid': update_business.bu_uid,
                'bu_type': update_business.bu_type,
                'bu_name': update_business.bu_name,
                'bu_description': update_business.bu_description, 
                'bu_city': update_business.bu_city,
                'bu_website': update_business.bu_website,
                'bu_address': update_business.bu_address,
                'phone': update_business.phone,
                # 'bu_picture': str(IMGHOSTNAME) + str(update_business.bu_picture),
                'bu_status': update_business.bu_status,
                't_uid': update_business.t_uid,
                'bu_categorie': update_business.bu_categorie
            }

            response['status'] = 'success'
            response['business'] = business_info
        else:
            response['status'] = 'error'
            response['error_description'] = "Aucune entité trouvée"

    except Exception as e:
        response['status'] = 'error'
        response['error_description'] = str(e)

    return response


def UpdateStatusBusiness():
    response = {}

    try:
        bu_uid = request.json.get('bu_uid')
        update_business = Business.query.filter_by(bu_uid = bu_uid).first()
        if update_business:
            update_business.bu_status = request.json.get('bu_status', update_business.bu_status)
        
        db.session.add(update_business)
        db.session.commit() 
        
        response['status'] = 'success'
        response['business'] = update_business

    except Exception as e:
        response['status'] = 'error'
        response['error_description'] = str(e)

    return response



def DeleteBusiness():

    response = {}
    try:
        uid = request.json.get('bu_uid')
        deletebusiness = Business.query.filter_by(bu_uid=uid).first()
        if deletebusiness:
            db.session.delete(deletebusiness)
            db.session.commit()

            response['status'] = 'success'

        else:
            response['status'] = 'error'
            response['motif'] = 'utilisateur non trouvé'

    except Exception as e:
        response['error_description'] = str(e)
        response['status'] = 'error'

    return response



def ReadAllBusiness():

    response = {}
    try:
        all_business = Business.query.all()
        business_infos = []
        for business in all_business:
            business_info = {
                'bu_uid': business.bu_uid,              
                'bu_categorie': business.bu_categorie,              
                'bu_type': business.bu_type,              
                'bu_name': business.bu_name,              
                'bu_description': business.bu_description,              
                'bu_city': business.bu_city,              
                'bu_website': business.bu_website,              
                'bu_address': business.bu_address,              
                'phone': business.phone,              
                # 'bu_picture': str(IMGHOSTNAME)+str(business.bu_picture),              
                't_uid': business.t_uid,              
                'bu_status': business.bu_status,              
            }
            business_infos.append(business_info)

        response['status'] = 'success'
        response ['business'] = business_infos

    except Exception as e:
        response['status'] = 'error'
        response['error_description'] = str(e)

    return response



def ReadSingleBusiness():
    response = {}
    try:
        business_uid = request.json.get('bu_uid')
        print(business_uid)
        single_business = Business.query.filter_by(bu_uid=business_uid).first()
        if single_business:
            business_info = {
                'bu_uid': single_business.bu_uid,
                'bu_categorie': single_business.bu_categorie,
                'bu_type': single_business.bu_type,
                'bu_name': single_business.bu_name,
                'bu_description': single_business.bu_description,
                'localisation': f"https://www.google.com/maps?q={single_business.latitude},{single_business.longitude}",
                'bu_city': single_business.bu_city,
                'bu_website': single_business.bu_website,
                'bu_address': single_business.bu_address,
                'phone': single_business.phone,
                # 'bu_picture': str(IMGHOSTNAME)+str(single_business.bu_picture),              
                't_uid': single_business.t_uid,
                'bu_status': single_business.bu_status,
            }
            response['status'] = 'success'
            response['business'] = business_info
            print(business_info)

    except Exception as e:
        response['status'] = 'error'
        response['error_description'] = str(e)

    return jsonify(response)



def ReadAllBusinessByCategories():

    response = {}
    try:
        bu_categorie = request.json.get('bu_categorie')
        all_business = Business.query.filter_by(bu_categorie=bu_categorie).all()
        business_infos = []
        for business in all_business:
            business_info = {
                'bu_uid': business.bu_uid,              
                'bu_categorie': business.bu_categorie,              
                'bu_type': business.bu_type,              
                'bu_name': business.bu_name,              
                'bu_description': business.bu_description,              
                'bu_city': business.bu_city,              
                'bu_website': business.bu_website,              
                'phone': business.phone,              
                'bu_address': business.bu_address,              
                # 'bu_picture': str(IMGHOSTNAME)+str(business.bu_picture),              
                't_uid': business.t_uid,              
                'bu_status': business.bu_status,              
            }
            business_infos.append(business_info)

        response['status'] = 'success'
        response ['business'] = business_infos

    except Exception as e:
        response['status'] = 'error'
        response['error_description'] = str(e)

    return response



def ReadAllBusinessByTeller():

    response = {}
    try:
        t_uid = request.json.get('t_uid')
        all_business = Business.query.filter_by(t_uid=t_uid).all()
        business_infos = []
        for business in all_business:
            business_info = {
                'bu_uid': business.bu_uid,              
                'bu_categorie': business.bu_categorie,              
                'bu_type': business.bu_type,              
                'bu_name': business.bu_name,              
                'bu_description': business.bu_description,              
                'bu_city': business.bu_city,              
                'bu_website': business.bu_website,              
                'phone': business.phone,              
                'bu_address': business.bu_address,              
                # 'bu_picture': str(IMGHOSTNAME)+str(business.bu_picture),              
                't_uid': business.t_uid,              
                'bu_status': business.bu_status,              
            }
            business_infos.append(business_info)

        response['status'] = 'success'
        response ['business'] = business_infos

    except Exception as e:
        response['status'] = 'error'
        response['error_description'] = str(e)

    return response


def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return ''.join([c for c in nfkd_form if not unicodedata.combining(c)])


def normalize_text(text):
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text).lower()
    return text.split()



def haversine_distance(lat1, lon1, lat2, lon2):
    # Rayon de la Terre en kilomètres
    R = 6371.0

    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad

    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c  # distance en km


# def SearchBusinessByCategorie():
#     response = {}
#     try:
#         data = request.json
#         user_id = data.get('user_id')
#         user_latitude = float(data.get('latitude'))
#         user_longitude = float(data.get('longitude'))
#         text = data.get('textSearch', '').strip()
#         print(f"Original text: {text}")
        
#         textSearch = remove_accents(text)
#         print(f"Text after accent removal: {textSearch}") 
        
#         page = int(data.get('page', 1))
#         per_page = int(data.get('per_page', 10))

#         if not textSearch:
#             return jsonify({'status': 'error', 'error_description': 'textSearch is required'}), 400

#         normalized_search = [w for w in normalize_text(textSearch) if len(w) > 2]
#         print(f"Normalized search terms (len > 2): {normalized_search}")

#         matched_businesses = []
#         for word in normalized_search:
#             word_search = f"%{word}%"
#             print(f"Recherche de : {word_search}")
#             all_business = Business.query.filter(
#                 Business.bu_status == 'active',
#                 or_(
#                     Business.bu_categorie.ilike(word_search),
#                     Business.bu_name.ilike(word_search),
#                     Business.bu_description.ilike(word_search),
#                     Business.bu_city.ilike(word_search)
#                 )
#             ).all()
#             print(f"{len(all_business)} résultat(s) pour le mot : {word}")
#             matched_businesses.extend(all_business)

#         matched_businesses = list({business.bu_uid: business for business in matched_businesses}.values())

#         if matched_businesses:
#             # Ajouter la distance à chaque business
#             business_with_distance = []
#             for business in matched_businesses:
#                 if business.latitude is not None and business.longitude is not None:
#                     distance = haversine_distance(user_latitude, user_longitude, business.latitude, business.longitude)
#                 else:
#                     distance = 999999.0  # Valeur arbitrairement grande
#                 business_with_distance.append((business, distance))

#             # Trier par distance croissante
#             business_with_distance.sort(key=lambda x: x[1])
#             total = len(business_with_distance)
#             start = (page - 1) * per_page
#             end = start + per_page
#             paginated_businesses = business_with_distance[start:end]

#             business_infos = []
#             for business, distance in paginated_businesses:
#                 all_favs = Favoris.query.filter_by(bu_uid=business.bu_uid, u_uid=user_id).first()
#                 is_favs = 1 if all_favs else 0
#                 business_infos.append({
#                     'bu_uid': business.bu_uid,
#                     'bu_categorie': business.bu_categorie,
#                     'bu_type': business.bu_type,
#                     'bu_name': business.bu_name,
#                     'bu_description': business.bu_description[:150]+"..." if len(business.bu_description) > 150 else business.bu_description,
#                     'bu_city': business.bu_city,
#                     'localisation': "https://www.google.com/maps?q={business.latitude},{business.longitude}",
#                     'bu_website': business.bu_website,
#                     'phone': business.phone,
#                     'bu_address': business.bu_address,
#                     # 'bu_picture': str(IMGHOSTNAME)+str(business.bu_picture),              
#                     't_uid': business.t_uid,
#                     'is_favs': is_favs,
#                     'bu_status': business.bu_status,
#                     'latitude': business.latitude,
#                     'longitude': business.longitude,
#                     'distance_km': round(distance, 2)
#                 })
#             response['status'] = 'success'
#             response['business'] = business_infos
#             response['textSearch'] = textSearch
#             response['total'] = total
#             response['pages'] = (total + per_page - 1) // per_page
#             response['current_page'] = page
#         else:
#             response['status'] = 'Not found'
#             response['textSearch'] = textSearch

#     except Exception as e:
#         app.logger.error(f"Error in searchBusinessByCategorie: {str(e)}")
#         response['status'] = 'error'
#         response['error_description'] = 'An unexpected error occurred.'

#     return response, 200



def get_location_from_coords(lat, lon, user_agent="CoocleSearch/1.0 (contact@coocle.ci)"):
    url = f"https://nominatim.openstreetmap.org/reverse?format=json&lat={lat}&lon={lon}&zoom=18&addressdetails=1"
    try:
        response = requests.get(url, headers={"User-Agent": user_agent})
        data = response.json()
        address = data.get("address", {})
        city = address.get("city") or address.get("town") or address.get("village") or address.get("state")
        suburb = address.get("suburb") or address.get("neighbourhood") or address.get("city_district")
        return city, suburb
    except Exception as e:
        print("Erreur géocodage inverse:", e)
        return None, None
    
    
GOOGLE_API_KEY = "VOTRE_API_KEY"
def fallback_location():
    url = f"https://www.googleapis.com/geolocation/v1/geolocate?key={GOOGLE_API_KEY}"
    response = requests.post(url)
    data = response.json()
    lat = data["location"]["lat"]
    lng = data["location"]["lng"]
    return jsonify({"lat": lat, "lng": lng})


def SearchBusinessByCategorie():
    # headers = {"User-Agent": NOMINATIM_UA}

    response = {}
    try:
        data = request.json
        user_id = data.get('user_id')
        user_lat = float(data.get('latitude'))
        user_lon = float(data.get('longitude'))
        text = data.get('textSearch', '').strip()
        city = data.get('city')
        page = int(data.get('page', 1))
        per_page = int(data.get('per_page', 10))

        if not text:
            return jsonify({'status': 'error', 'error_description': 'textSearch is required'}), 400
        print('debut1')
        textSearch = remove_accents(text)
        normalized_search = [w for w in normalize_text(textSearch) if len(w) > 2]

        combined_results = []

        # ===== 1. Rechercher dans la base interne =====
        filters = []
        for word in normalized_search:
            word_search = f"%{word}%"
            filters.append(Business.bu_categorie.ilike(word_search))
            filters.append(Business.bu_name.ilike(word_search))
            filters.append(Business.bu_description.ilike(word_search))
            filters.append(Business.bu_city.ilike(word_search))
        # Une seule requête SQL pour tous les mots
        matched_businesses = Business.query.filter(
            Business.bu_status == 'active',
            or_(*filters)
        ).all()

        matched_businesses = list({b.bu_uid: b for b in matched_businesses}.values())

        for business in matched_businesses:
            if business.latitude is not None and business.longitude is not None:
                distance = haversine_distance(user_lat, user_lon, business.latitude, business.longitude)
            else:
                distance = 999999.0
            all_favs = Favoris.query.filter_by(bu_uid=business.bu_uid, u_uid=user_id).first()
            is_favs = 1 if all_favs else 0
            combined_results.append({
                'bu_uid': business.bu_uid,
                'bu_categorie': business.bu_categorie,
                'bu_type': business.bu_type,
                'bu_name': business.bu_name,
                'bu_description': business.bu_description[:150]+"..." if len(business.bu_description) > 150 else business.bu_description,
                'bu_city': business.bu_city,
                'localisation': "https://www.google.com/maps?q={business.latitude},{business.longitude}",
                'bu_website': business.bu_website,
                'phone': business.phone,
                'bu_address': business.bu_address,
                't_uid': business.t_uid,
                'is_favs': is_favs,
                'bu_status': business.bu_status,
                'latitude': business.latitude,
                'longitude': business.longitude,
                "source": "internal",
                'distance_km': round(distance, 2)
            })
        print('debut2')

        # ===== 2. Rechercher dans OSM via Overpass =====
        osm_query = build_overpass_query(textSearch, city)
        url = "https://overpass-api.de/api/interpreter"
        osm_response = requests.get(url, params={"data": osm_query})
        osm_data = osm_response.json()

        for element in osm_data.get("elements", []):
            name = element.get("tags", {}).get("name", "Inconnu")
            city = element.get("tags", {}).get("addr:city")
            suburb = element.get("tags", {}).get("addr:suburb")
            lat = float(element.get("lat"))
            lon = float(element.get("lon"))
            print('lat:', lat, 'lon:', lon)

            # Si city ou suburb est null, on fait un reverse geocoding
            if not city or not suburb:
                city_rev, suburb_rev = get_location_from_coords(lat, lon)
                city = city or city_rev
                suburb = suburb or suburb_rev

            distance = haversine_distance(user_lat, user_lon, lat, lon)

            combined_results.append({
                "bu_name": name,
                "bu_city": city,
                "bu_address": suburb,
                "latitude": lat,
                "longitude": lon,
                'localisation': f"https://www.google.com/maps?q={lat},{lon}",
                "bu_type": "physique",
                "source": "osm",
                "distance_km": round(distance, 2)
            })

        # ===== 3. Trier par distance =====
        print('debut3')

        combined_results.sort(key=lambda x: x["distance_km"])

        # ===== 4. Pagination =====
        total = len(combined_results)
        start = (page - 1) * per_page
        end = start + per_page
        paginated = combined_results[start:end]
        print('debut4')

        response['status'] = 'success'
        response['total'] = total
        response['pages'] = (total + per_page - 1) // per_page
        response['current_page'] = page
        response['business'] = paginated

    except Exception as e:
        app.logger.error(f"Error in combined_search: {str(e)}")
        response['status'] = 'error'
        response['error_description'] = str(e)

    return response


# Fonction qui construit la requête Overpass
def build_overpass_query(user_input, area):
    tagMapping = {
    # Santé
    "pharmacie": "pharmacy",
    "pharmacies": "pharmacy",
    "clinique": "clinic",
    "hôpital": "hospital",
    "hopital": "hospital",
    "centre médical": "clinic",
    "laboratoire": "laboratory",

    # Alimentation
    "restaurant": "restaurant",
    "resto": "restaurant",
    "fast-food": "fast_food",
    "supermarché": "supermarket",
    "supérette": "supermarket",
    "boulangerie": "bakery",
    "café": "cafe",
    "bar": "bar",
    "glacier": "ice_cream",
    "boucherie": "butcher",

    # Transports / véhicules
    "station service": "fuel",
    "station essence": "fuel",
    "parking": "parking",
    "garage": "garage",
    "taxi": "taxi",
    "arrêt de bus": "bus_stop",

    # Education
    "école": "school",
    "college": "school",
    "collège": "school",
    "lycée": "school",
    "université": "university",
    "centre de formation": "school",

    # Finance / services
    "banque": "bank",
    "caisse": "bank",
    "guichet": "atm",
    "bureau de poste": "post_office",

    # Loisirs / tourisme
    "hôtel": "hotel",
    "auberge": "hostel",
    "centre sportif": "sports_centre",
    "terrain de sport": "pitch",
    "cinéma": "cinema",
    "parc": "park",
    "aire de jeux": "playground",
    "musée": "museum",
    "église": "place_of_worship",
    "mosquée": "place_of_worship",
    "temple": "place_of_worship",

    # Commerces divers
    "magasin": "shop",
    "boutique": "shop",
    "supermarché": "supermarket",
    "pharmacie": "pharmacy",
    "librairie": "books",
    "coiffeur": "hairdresser",
    "esthétique": "beauty",
    "centre commercial": "mall",
    }

    keyword = user_input.lower()

    if keyword in tagMapping:
        # Recherche par type connu
        return f"""
        [out:json];
        area["name"="{area}"]->.searchArea;
        node["amenity"="{tagMapping[keyword]}"](area.searchArea);
        out;
        """
    else:
        # Recherche libre par nom (regex insensible à la casse)
        return f"""
        [out:json];
        area["name"="{area}"]->.searchArea;
        node["name"~"{keyword}", i](area.searchArea);
        out;
        """
