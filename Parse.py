import json
from collections import Counter
# -*- coding: utf-8 -*-

def git_data():
    with open("C:\\Users\\Ярослав\\Downloads\\GitStats.json", encoding='utf-8') as file:
        data = json.loads(file.readline())
        registration = False
        timestamps = []
        for string in range (len(data)): 
            if data[string]["email"] == "yaamoskalenko@miem.hse.ru":
                registration = True
                for project in range(len(data[string]["projects"])):
                    for commit in range(len(data[string]["projects"][project]["commits"])):
                        timestamps.append(data[string]["projects"][project]["commits"][commit]["committed_date"][:10])
        dictionary = Counter(timestamps)

    return {'registration': registration, 
        'dictionary': dictionary}

def zulip_data():
    with open("C:\\Users\\Ярослав\\Downloads\\ZulipStats.json", encoding='utf-8') as file:
        data = json.loads(file.readline())
        registration = False
        timestamps = []
        for string in range (len(data)): 
            if data[string]["full_name"] == "Ярослав Москаленко" and data[string]["is_bot"] + data[string]["is_guest"] == 0: 
                registration = True
                for message in range(len(data[string]["messages"])):
                    timestamps.append(data[string]["messages"][message]["timestamp"][:10])
        dictionary = Counter(timestamps)
    
    return {'registration': registration, 
        'dictionary': dictionary}

def jitsi_data():
    with open("C:\\Users\\Ярослав\\Downloads\\JitsiSession.json", encoding='utf-8') as file: 
        data = json.loads(file.readline())
        timestamps = []
        for cnt in range(len(data)):
            if data[cnt]['username'] == 'yaamoskalenko@miem.hse.ru' and data[cnt]['room'][:7] == '312':
                timestamps.append(data[cnt]['date'])
        dictionary = Counter(timestamps)
    return {'dictionary': dictionary}

def jitsi_session():
    with open("C:\\Users\\Ярослав\\Downloads\\JitsiSession.json", encoding='utf-8') as file: 
        data = json.loads(file.readline())
        timestamps = []
        for cnt in range(len(data)):
            if data[cnt]['username'] == 'yaamoskalenko@miem.hse.ru' and data[cnt]['room'][:7] == 'project':
                timestamps.append(data[cnt]['date'])
        dictionary = Counter(timestamps)
    return {'dictionary': dictionary}
