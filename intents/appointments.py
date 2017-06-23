from __future__ import print_function
from future.standard_library import install_aliases
import requests

install_aliases()  # not sure what this does...


# k1 api example
def first_visit(base_url, token, business_token, day='Today'):
    print(business_token)
    url = base_url + "/k1/clients_ajax/get_client_appointments_info_for_day/" + day + "/" + business_token + "/all"
    print(url)
    headers = {'Token': token}
    response = requests.post(url, None, True, verify=False, headers=headers)
    result = response.json()
    print(result)

    text = "First visit of " + day + ": \n"
    text += result['models'][0]['first_name'] + "\n at "
    text += result['models'][0]['start_date'] + "\n"
    text += result['models'][0]['appt_status']

    return {
        "speech": text,
        "displayText": text,
    }

def today(base_url, token, business_token, day='Today'):
    print(business_token)
    url = base_url + "/k1/clients_ajax/get_client_appointments_info_for_day/" + day + "/" + business_token + "/all"
    print(url)
    headers = {'Token': token}
    response = requests.post(url, None, True, verify=False, headers=headers)
    result = response.json()
    print(result)

    text = "Your appointments for " + day + ": \n"
    for m in result['models']:
        text += "-" + m['first_name'] + " with "
        text += m['services'][0]['staff_first_name'] + " at "
        text += m['start_date'] + " "
        text += m['appt_status'] + "\n"
    return {
        "speech": text,
        "displayText": text,
    }
