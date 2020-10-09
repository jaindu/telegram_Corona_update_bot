import requests
import json
import io



TOKEN = 'PUT YOUR TOKEN HERE'
URL = 'https://api.telegram.org/bot{}/'.format(TOKEN)



def sendText(text,chat):
    r=requests.get('https://api.telegram.org/bot' + TOKEN
                 + '/sendMessage?chat_id=' + chat + '&text='
                 + text +'&parse_mode=HTML')
    print(r.text)

def get_updates(offset=None):
    url = URL + 'getUpdates'
    if offset:
        url += '?offset={}'.format(offset)
    js = get_json_from_url(url)
    return js

def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_url(url):
    response = requests.get(url)
    content = response.content.decode('utf8')
    return content

def get_last_update_id(updates):
    update_ids = []
    for update in updates['result']:
        update_ids.append(int(update['update_id']))
    return max(update_ids)

def corona(updates):
    #print(updates)
    
    for update in updates['result']:
        
        #print(update['message'])
        
        try:
        
            try:
                print(update['message'])
                namee=update['message']['chat']['title']
                fromm=update['message']['from']['username']
                sms=update['message']['text']
                datee=str(update['message']['date'])
                liyawena=namee+' '+fromm+' '+datee+' '+sms
                with io.open('groups/'+namee, "a", encoding="utf-8") as f:
                    f.write(liyawena)
                    f.write("\n")
                    f.write(str(update))
                    f.write("\n")
                    f.write("\n")
            except:
                try:
                    print(update['message'])
                    #namee=update['message']['chat']['title']
                    fromm=update['message']['from']['username']
                    sms=update['message']['text']
                    datee=str(update['message']['date'])
                    liyawena=' '+fromm+' '+datee+' '+sms
                    with io.open('pm/'+fromm, "a", encoding="utf-8") as f:
                        f.write(liyawena)
                        f.write("\n")
                        f.write(str(update))
                        f.write("\n")
                        f.write("\n")
                except:
                    print(update['message'])
                    #namee=update['message']['chat']['title']
                    fromm=update['message']['from']['first_name']
                    sms=update['message']['text']
                    datee=str(update['message']['date'])
                    liyawena=' '+fromm+' '+datee+' '+sms
                    with io.open('pm/'+fromm, "a", encoding="utf-8") as f:
                        f.write(liyawena)
                        f.write("\n")
                        f.write(str(update))
                        f.write("\n")
                        f.write("\n")
              
            if update['message']['text']=='/corona@coronasrilankabot' or update['message']['text']=='/corona':
                r=requests.get('https://hpb.health.gov.lk/api/get-current-statistical')
                jsondata=json.loads(r.text)
                #tes=jsondata['data']['update_date_time']
                update_date_time=str(jsondata['data']['update_date_time'])
                local_new_cases	=str(jsondata['data']['local_new_cases'])
                local_active_cases=str(jsondata['data']['local_active_cases'])
                local_total_cases=str(jsondata['data']['local_total_cases'])
                local_deaths=str(jsondata['data']['local_deaths'])
                local_recovered=str(jsondata['data']['local_recovered'])
                local_total_number_of_individuals_in_hospitals=str(jsondata['data']['local_total_number_of_individuals_in_hospitals'])
                global_new_cases=str(jsondata['data']['global_new_cases'])
                global_total_cases=str(jsondata['data']['global_total_cases'])
                global_deaths=str(jsondata['data']['global_deaths'])
                global_new_deaths=str(jsondata['data']['global_deaths'])
                global_recovered=str(jsondata['data']['global_recovered'])
                
                #textt='*Current Situation*'+'%0D%0A'+update_date_time+' වනවිට'+'%0D%0A'+'%0D%0A'+'ශ්‍රී ලංකාව තුළ තත්ත්වය'+'%0D%0A'+'%0D%0A'+'නව රෝගීන් සංඛ්‍යාව = '+local_new_cases+'%0D%0A'+'ප්‍රතිකාර ලබන රෝගීන් සංඛ්‍යාව ='+local_active_cases+'%0D%0A'+'තහවුරු කරනලද රෝගීන් සංඛ්‍යාව(සමුච්චිත) = '+local_total_cases+'%0D%0A'+'මරණ සංඛ්‍යාව = '+local_deaths+'%0D%0A'+'සුවය ලබා පිටව ගිය සංඛ්‍යාව = '+local_recovered+'%0D%0A'+'දැනට රෝහල්වල විමර්ශන යටතේ සිටින පුද්ගලයින් = '+local_total_number_of_individuals_in_hospitals+'%0D%0A'+'%0D%0A'+'__ලොව පුරා තත්ත්වය__'+'%0D%0A'+'%0D%0'+'නව රෝගීන් සංඛ්‍යාව = '+global_new_cases+'%0D%0A'+'තහවුරු කරනලද රෝගීන් සංඛ්‍යාව(සමුච්චිත) = '+global_total_cases+'%0D%0A'+'මරණ සංඛ්‍යාව = '+global_deaths+'සුවය ලැබූ සංඛ්‍යාව = '+global_recovered     
                textt=str('<b>CURRENT SITUATION</b>'+'%0D%0A'+'%0D%0A'+'<u>'+update_date_time+' වන විට</u>'+'%0D%0A'+'%0D%0A'+'<u>ශ්‍රී ලංකාවේ තත්ත්වය</u>'+'%0D%0A'+'%0D%0A'+'තහවුරු කරනලද රෝගීන් සංඛ්‍යාව(සමුච්චිත) = '+local_total_cases+'%0D%0A'+'ප්‍රතිකාර ලබන රෝගීන් සංඛ්‍යාව = '+local_active_cases+'%0D%0A'+'නව රෝගීන් සංඛ්‍යාව = '+local_new_cases+'%0D%0A'+'දැනට රෝහල්වල විමර්ශන යටතේ සිටින පුද්ගලයින් = '+local_total_number_of_individuals_in_hospitals+'%0D%0A'+'සුවය ලබා පිටව ගිය සංඛ්‍යාව = '+local_recovered+'%0D%0A'+'මරණ සංඛ්‍යාව = '+local_deaths+'%0D%0A'+'%0D%0A'+'<u>ලොව පුරා තත්ත්වය</u>'+'%0D%0A'+'%0D%0A'+'තහවුරු කරනලද රෝගීන් සංඛ්‍යාව(සමුච්චිත) = '+global_total_cases+'%0D%0A'+'නව රෝගීන් සංඛ්‍යාව = '+global_new_cases+'%0D%0A'+'මරණ සංඛ්‍යාව = '+global_deaths+'%0D%0A'+'සුවය ලැබූ සංඛ්‍යාව = '+global_recovered+'%0D%0A'+'%0D%0A'+'%0D%0A'+'සියලු තොරතුරු රජයේ සහ පිලිගත් මුලාශ්‍ර මගිනි'+'%0D%0A'+'@coronasrilankabot')
                
                chat_id=str(update['message']['chat']['id'])
                sendText(textt,chat_id)
                
                
                
                print('hi')
            elif update['message']['text']=='/start@coronasrilankabot' or update['message']['text']=='/start':
                text='Corona Updates - Sri Lanka'+'%0D%0A'+'%0D%0A'+'ශ්‍රී ලංකාවේ කොරෝනා තතු එසැනින් දැනගන්න. @coronasrilankabot. ඔබගේ Group එකට Add කරගත් පසු ස්වයංක්‍රියව නවතම කොරෝනා තතු ලබාගත හැක. '+'%0D%0A'+'%0D%0A'+'සියළු තොරතුරු රජයේ සහ වෙනත් පිළිගත හැකි මූලාශ්‍ර මගිනි.'+'%0D%0A'+'%0D%0A'+'සරලව /corona විධානය භාවිතයෙන් ලංකාවේ සහ ලෝකයේ නවතම තොරතුරු දැනගන්න'
                chat_id=str(update['message']['chat']['id'])
                sendText(text,chat_id)
        except:
            print('eRR')
        


    
last_update_id = None
while True:

    updates = get_updates(last_update_id)
    #print(updates)
 
    
    if len(updates["result"]) > 0:
        last_update_id = get_last_update_id(updates) + 1
        #print(last_update_id)
        
        corona(updates)
    
