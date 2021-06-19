import requests

def get_tokenByDevName(dev_name,
                       url = "http://ip_address:port", 
                       username = "tenant@thingsboard.org", 
                       password = "tenant", 
                       header_type = "application/json"):
    
    headers = {'content-type':header_type, 'Accept':header_type}
    data_auth = {'username':username, 'password':password}
    
    # get Authorization Token
    back = requests.post(url+'/api/auth/login', json=data_auth, headers=headers)
    token = back.json().get('token')
    
    headers_auth = {'Accept':'application/json', 
                    'X-Authorization':'Bearer '+token}

    url_dev_byName = url+'/api/tenant/devices?deviceName='+dev_name

    devByName = requests.get(url_dev_byName, headers=headers_auth)

    dev_id = devByName.json().get('id').get('id')

    url_dev_credencial = url+'/api/device/'+dev_id+'/credentials'

    credentials = requests.get(url_dev_credencial, headers=headers_auth)

    dev_token = credentials.json().get('credentialsId')
    
    return dev_token

def create_dev(dev_name,
               token_name = 'default',
               dev_profile = "default",
               url = "http://ip_address:port", 
               username = "tenant@thingsboard.org", 
               password = "tenant", 
               header_type = "application/json", 
               rest_answer = False):
    
    headers = {'content-type':header_type, 'Accept':header_type}
    data_auth = {'username':username, 'password':password}
    
    # get Authorization Token
    back = requests.post(url+'/api/auth/login', json=data_auth, headers=headers)
    token = back.json().get('token')
    
    headers_auth = {'Accept':'application/json', 
                    'X-Authorization':'Bearer '+token}
    
    device = {
        "name": dev_name,
        "type": dev_profile,
        "additionalInfo": {
            "description": " "
            }
        }
    
    if token_name != "default":
        r = requests.post(url+'/api/device?accessToken='+token_name, json=device, headers=headers_auth)
    else:
        r = requests.post(url+'/api/device', json=device, headers=headers_auth)
    
    if rest_answer:
        print(r.json())


def delete_dev(dev_name,
               url = "http://ip_address:port", 
               username = "tenant@thingsboard.org", 
               password = "tenant", 
               header_type = "application/json", 
               rest_answer = False):
    
    headers = {'content-type':header_type, 'Accept':header_type}
    data_auth = {'username':username, 'password':password}
    
    # get Authorization Token
    back = requests.post(url+'/api/auth/login', json=data_auth, headers=headers)
    token = back.json().get('token')
    
    headers_auth = {'Accept':'application/json', 
                    'X-Authorization':'Bearer '+token}
    
    url_dev_byName = url+'/api/tenant/devices?deviceName='+dev_name

    devByName = requests.get(url_dev_byName, headers=headers_auth)

    dev_id = devByName.json().get('id').get('id')
    
    delete_url = url+'/api/device/'+dev_id
    
    r = requests.delete(delete_url, headers=headers_auth)
    
    if rest_answer:
        print(r)