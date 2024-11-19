import sqlite3

#print(sqlite3.sqlite_version)

connexion= sqlite3.connect("ma_bd.db")

curseur = connexion.cursor()
curseur.execute('''
create table if not exists utilisateur(
id Integer Primary Key autoincrement,
 nom text not null,
 age Integer not null,
  email text not null unique
)
''')
print("table crée avec succes")
nom="ondoua"
age = 21
email = "dorianondoua188@gmail.com"

curseur.execute('''
insert into utilisateur (nom, age,email)
values(?, ?, ?)

''',(nom,age,email))
print('données insérés avec succes')

#curseur.execute('''
#UPDATE utilisateur
#SET email ='shadowsdod@gmail.com'
#WHERE id =1
#''')
#print('données insérés avec succes')

curseur.execute('SELECT * FROM utilisateur')
resultats = curseur.fetchall()

print(resultats)

for ligne in resultats:
    print(ligne)


# commit pour enregistrer
connexion.commit()

connexion.close()