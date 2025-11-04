from flask import request
import uuid
from config.db import db
from model.tt import Advertisement


def CreateAdvertisement():
    
    response = {}
    try:
        new_advertisement = Advertisement()
        new_advertisement.ad_type = request.json.get('ad_type')
        new_advertisement.ad_title = request.json.get('ad_title')
        new_advertisement.ad_email = request.json.get('ad_email')
        new_advertisement.ad_description = request.json.get('ad_description')
        new_advertisement.ad_mobile = request.json.get('ad_mobile')
        new_advertisement.ad_address = request.json.get('ad_address')
        new_advertisement.number_broadcasts = request.json.get('number_broadcasts')
        new_advertisement.ad_start_date = request.json.get('ad_start_date')
        new_advertisement.ad_end_date = request.json.get('ad_end_date')
        
        db.session.add(new_advertisement)
        db.session.commit()

        rs = {}
        rs['ad_type'] = new_advertisement.ad_type
        rs['ad_title'] = new_advertisement.ad_title
        rs['ad_email'] = new_advertisement.ad_email
        rs['ad_description'] = new_advertisement.ad_description
        rs['ad_mobile'] = new_advertisement.ad_mobile
        rs['ad_address'] = new_advertisement.ad_address
        rs['number_broadcasts'] = new_advertisement.number_broadcasts
        rs['ad_start_date'] = new_advertisement.ad_start_date
        rs['ad_end_date'] = new_advertisement.ad_end_date

        response['satus'] = 'success'
        response['advertisement'] = rs

    except Exception as e:
        response['error_description'] = str(e)
        response['status'] = 'error'

    return response


def UpdateAdvertisement():

    response = {}
    try:
        update_advertisement = Advertisement.query.filter_by(ad_uid="efa34482-9325-48be-9cac-9875e7fc8991").first_or_404()
        update_advertisement.ad_type = request.json.get('ad_type', update_advertisement.ad_type)
        update_advertisement.ad_title = request.json.get('ad_title', update_advertisement.ad_title)
        update_advertisement.ad_email = request.json.get('email', update_advertisement.ad_email)
        update_advertisement.ad_description = request.json.get('description', update_advertisement.ad_description)            
        update_advertisement.ad_mobile = request.json.get('mobile', update_advertisement.ad_mobile)
        update_advertisement.ad_address = request.json.get('ad_address', update_advertisement.ad_address)
        update_advertisement.number_broadcasts = request.json.get('number_broadcasts', update_advertisement.number_broadcasts)
        update_advertisement.ad_end_date = request.json.get('ad_end_date', update_advertisement.ad_end_date)
        
        db.session.add(update_advertisement)
        db.session.commit() 

        rs = {}
        rs['ad_uid'] = update_advertisement.ad_uid
        rs['ad_type'] = update_advertisement.ad_type
        rs['ad_title'] = update_advertisement.ad_title
        rs['ad_email'] = update_advertisement.ad_email
        rs['ad_description'] = update_advertisement.ad_description
        rs['ad_mobile'] = update_advertisement.ad_mobile
        rs['ad_address'] = update_advertisement.ad_address
        rs['number_broadcasts'] = update_advertisement.number_broadcasts
        rs['ad_start_date'] = update_advertisement.ad_start_date
        rs['ad_end_date'] = update_advertisement.ad_end_date
        
        response['status'] = 'success'
        response['advertisement'] = rs

    except Exception as e:
        response['status'] = 'error'
        response['error_description'] = str(e)

    return response



def DeleteAdvertisement():

    response = {}
    try:
        ad_uid = request.json.get('ad_uid')
        deleteAdvertisement = Advertisement.query.filter_by(ad_uid=ad_uid).first_or_404()

        db.session.delete(deleteAdvertisement)
        db.session.commit()
        response['status'] = 'success'

    except Exception as e:
        response['error_description'] = str(e)
        response['status'] = 'error'

    return response



def ReadAllAdvertisement():

    response = {}
    try:
        all_advertisement = Advertisement.query.all()
        All_advertisement = []
        for advertisement in all_advertisement:
            rs = {}
            rs['ad_uid'] = advertisement.ad_uid
            rs['ad_type'] = advertisement.ad_type
            rs['ad_title'] = advertisement.ad_title
            rs['ad_email'] = advertisement.ad_email
            rs['ad_description'] = advertisement.ad_description
            rs['ad_mobile'] = advertisement.ad_mobile
            rs['ad_address'] = advertisement.ad_address
            rs['number_broadcasts'] = advertisement.number_broadcasts
            rs['ad_start_date'] = advertisement.ad_start_date
            rs['ad_end_date'] = advertisement.ad_end_date
            All_advertisement.append(rs)

        response['status'] = 'success'
        response ['advertisement'] = All_advertisement

    except Exception as e:
        response['status'] = 'error'
        response['error_description'] = str(e)

    return response



def ReadSingleAdvertisement():

    response = {}
    try:
        ad_uid = request.json.get('ad_uid')
        single_advertisement = Advertisement.query.filter_by(ad_uid=ad_uid).first_or_404()
        rs = {}
        rs['ad_uid'] = single_advertisement.ad_uid
        rs['ad_type'] = single_advertisement.ad_type
        rs['ad_title'] = single_advertisement.ad_title
        rs['ad_email'] = single_advertisement.ad_email
        rs['ad_description'] = single_advertisement.ad_description
        rs['ad_mobile'] = single_advertisement.ad_mobile
        rs['ad_address'] = single_advertisement.ad_address
        rs['number_broadcasts'] = single_advertisement.number_broadcasts
        rs['ad_start_date'] = single_advertisement.ad_start_date
        rs['ad_end_date'] = single_advertisement.ad_end_date

        response['status'] = 'success'
        response['advertisement'] = rs

    except Exception as e:
        response['status'] = 'error'
        response['error_description'] = str(e)

    return response

