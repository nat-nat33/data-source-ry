import psycopg2
import sys

# print to see if you have access to the clean new list of contact data
# print(thin_contact_list)

# start with no connection
con = None

# try to connect
try:
    # adapter to connect to postgres db 
    con = psycopg2.connect(database='hsbd', user='nat') 
    # allows python code to execute sql commands
    cur = con.cursor()
    # execute method that process sql commands in db
    cur.execute('SELECT version()')          
    # error check connection to db
    ver = cur.fetchone()
    print (ver, "i can conncet")    
    
    # loop through clean list and insert to db
    for contact in thin_contact_list:
        cur.execute("INSERT INTO contacts(first_name, last_name, email) VALUES ('"+ contact['firstname'] + "','" + contact['lastname'] + "',' " + contact['email'] + "')")
        # error check print to see if each record was inserted
        print('inserted')
    
    # commit everything in this session to db
    con.commit()

# exception error handling for failed connection    
except psycopg2.DatabaseError as e:
    print ('Error %s' % e)    
    sys.exit(1)
    

# closes session to db after everything runs    
finally:
    
    if con:
        con.close()