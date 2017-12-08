from pprint import pprint
import urllib.request, json
import 

# Store api key value into variable
APIKEY_VALUE = "demo"

# concat api query string with api key
APIKEY = "?hapikey=" + APIKEY_VALUE

# hs api end point stored to a variable
HS_API_URL = "http://api.hubapi.com"

thin_contact_list = []

def get_contacts():
    # builds the correct url
    xurl = "/contacts/v1/lists/all/contacts/all"
    url = HS_API_URL + xurl + APIKEY 
    # Now we use urllib to open the url and read it
    response = urllib.request.urlopen(url).read()
    #loads to json obj to all_contacts variable
    all_contacts = json.loads(response)
    #return the contact data
    return all_contacts

def process_contacts(contact_list):
    new_contact_list = []
    
    #create a loop through contacts dict and store values to new list
    for i in range(len(contacts['contacts'])):

        #store values needed to variables
        first_name= contacts['contacts'][i]['properties']['firstname']['value']
        last_name= contacts['contacts'][i]['properties']['lastname']['value']
        
        email = ''
        for identity in contacts['contacts'][i]['identity-profiles'][0]['identities']:
            if identity['type'] == 'EMAIL':
                email = identity['value']
        
        created_on= contacts['contacts'][i]['addedAt']
        last_login= contacts['contacts'][i]['identity-profiles'][0]['saved-at-timestamp']

        #added mock values to blanks in fields
        if(first_name == ''):
         first_name = 'Amanda'

        if(last_name == ''):
         last_name = 'Miranda'

        if(email == ''):
         email = 'unicorn@aweseomeco.com'

        #created contact dict to go into db
        contact = {"firstname": first_name,
                   "lastname": last_name,
                   "email": email,
                   "createdon": created_on,
                   "lastlogin": last_login
                  }

        new_contact_list.append(contact)
    
    return new_contact_list
        
# Start processing logic
if __name__== "__main__":
    #invoke function to get data from api
    contacts = get_contacts()
    #process list of contacts
    thin_contact_list = process_contacts(contacts)
    
    # print(thin_contact_list)