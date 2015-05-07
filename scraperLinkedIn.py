import MySQLdb
import sys
import json
from linkedin_data import get_profile_json_data
from create_tables import create_tables
from add_data_to_db import insert_data

static_json = {"schools": ["University of Illinois at Urbana-Champaign", "Illinois Mathematics and Science Academy"], "companies": ["SurveyMonkey", "Dev Bootcamp", "Zazzle", "Fileboard", "Ace Metrix", "AOL"], "name": "Henry Wang"}
generated_json = get_profile_json_data("https://www.linkedin.com/in/henrytwang")
generated_json_to_dict = json.loads(generated_json)

db1 = MySQLdb.connect(host="localhost",user="root",passwd="",db="testdb")
cursor = db1.cursor()

create_tables(cursor)

insert_data(cursor, converted_json_data_2)

# # open a database connection
# # be sure to change the host IP address, username, password and database name to match your own
# connection = MySQLdb.connect(
#     host = 'localhost',
#     user = 'root',
#     passwd = '',
#     port = 3000)
# # prepare a cursor object using cursor() method
# cursor = connection.cursor ()
# # execute the SQL query using execute() method.
# cursor.execute ("SELECT VERSION()")
# # fetch a single row using fetchone() method.
# row = cursor.fetchone ()
# # print the row[0]
# # (Python starts the first row in an array with the number zero - instead of one)
# print "Server version:", row[0]
# # close the cursor object
# cursor.close ()
# # close the connection
# connection.close ()
# # exit the program
# sys.exit()
