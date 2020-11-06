import sqlite3 as lite
import sys

con = lite.connect("pets.db")

with con:
    cur = con.cursor()
    flag=1
    while flag==1:
        person_id=input("Please input person's id, enter -1 to exit: ")
        if person_id!="-1":
            cur.execute("SELECT * FROM person WHERE id="+person_id)
            persons = cur.fetchall()
            if len(persons)==0:
                print("The person's id you inputed is not existed.")
                # flag=0
            else:
                print(persons[0][1]+" "+persons[0][2]+", "+str(persons[0][3])+" years old.")
                cur.execute("SELECT B.* FROM person_pet A JOIN pet B ON A.pet_id=B.id WHERE A.person_id="+person_id)
                pets=cur.fetchall()
                for pet in pets:
                    print(persons[0][1]+" "+persons[0][2]+" owned "+pet[1]+", a "+pet[2]+", that was "+str(pet[3])+" years old.")
        else:
            flag=0