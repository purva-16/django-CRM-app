import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost' ,
    user = 'root' ,
    passwd = 'Ksap11213$',

) 

# prepare cursor obj

cursorObject = dataBase.cursor()

# create dtdbse

cursorObject.execute("CREATE DATABASE elderco ")

print ("ALL DONE")
