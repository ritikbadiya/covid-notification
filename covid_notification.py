#!/usr/bin/env python3
import json
import requests
import plyer
import time
import datetime
def show_notification(country):
    date=datetime.date.today().strftime("%d %B, %Y")
    res=requests.get('https://corona-rest-api.herokuapp.com/Api/{}/'.format(country))
    if not res.status_code==200:
        print('bad request')
        return None
    Total_cases=res.json()['Success']['cases']
    New_cases=res.json()['Success']['todayCases']
    Active_cases=res.json()['Success']['active']
    Counry=res.json()['Success']['country']
    ms="""country       :{} \nTotal_cases   :{} \nNew_cases     :{} \nActive_cases  :{} """.format(Counry,Total_cases,New_cases,Active_cases)
    #address of icon
    icon='./virus.png'
    plyer.notification.notify(title='COVID UPDATE '+date,app_name='COVID_NOTIFIER',message=ms,app_icon=icon)
    #time.sleep()
show_notification(input('country'))
