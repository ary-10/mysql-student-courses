import mysql.connector

# -------------------------------
# 1. Connexion initiale à MySQL
# -------------------------------
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""  
)

if conn.is_connected():
    print("Connexion réussie à MySQL")
else:
    print("Problème de Connexion à MySQL")


# -------------------------------
# 2. Création de la base de données
# -------------------------------
cursor = conn.cursor()
cursor.execute("DROP DATABASE IF EXISTS Rx2DB")
cursor.execute("CREATE DATABASE  Rx2DB")
print("Base de données Rx2DB créée")

# -------------------------------
# Connexion à la base Rx2DB
# -------------------------------
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  
    database="Rx2DB"
)

if conn.is_connected():
    print("Connexion réussie à Rx2DB")
else:
    print("Problème de Connexion à Rx2DB")


# -------------------------------
# 3. (1) Création de la table Etudiants
# -------------------------------
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS Etudiants (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(100),
    age INT
)
""")
print(" Table Etudiants créée")

# -------------------------------
# 3. (2) Création de la table Cours
# -------------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS Cours (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titreCours VARCHAR(100),
    idEtudiant INT,
    FOREIGN KEY (idEtudiant) REFERENCES Etudiants(id) ON DELETE CASCADE
)
""")
print(" Table Cours créée")

# -------------------------------
# 4.a - Insertion des étudiants
# -------------------------------
etudiants = [("Arij", 20), ("Wajdi", 19), ("Hadil", 21)]
cursor.executemany("INSERT INTO Etudiants (nom, age) VALUES (%s, %s)", etudiants)
conn.commit()
# -------------------------------
# 4.b - Affichage de nombre d'étudiants ajoutés
# -------------------------------
print(cursor.rowcount, "étudiants ajoutés")

# -------------------------------
# 4.c Insertion des cours
# -------------------------------
cours = [("Ingénierie des bases de données", 1), ("Compilation", 2), ("Réseaux IP", 1)]
cursor.executemany("INSERT INTO Cours (titreCours, idEtudiant) VALUES (%s, %s)", cours)
conn.commit()
# -------------------------------
# 4.d - Affichage de nombre de cours ajoutés
# -------------------------------
print(cursor.rowcount,"cours ajoutés")

# -------------------------------
# 5. Affichage des étudiants
# -------------------------------
cursor.execute("SELECT * FROM Etudiants")
print("Étudiants :")
for row in cursor.fetchall():
    print(row)

# -------------------------------
#   Affichage des cours
# -------------------------------
cursor.execute("SELECT * FROM Cours")
print("Cours :")
for row in cursor.fetchall():
    print(row)

# -------------------------------
# 6. Modifier l’âge de Wajdi
# -------------------------------
cursor.execute("UPDATE Etudiants SET age = 20 WHERE nom = 'Wajdi'")
conn.commit()
print(cursor.rowcount, "ligne(s) modifiée(s) pour Wajdi")

# -------------------------------
# 7. Supprimer l’étudiant Karim
# -------------------------------
cursor.execute("DELETE FROM Etudiants WHERE age = 20")
conn.commit()
print(cursor.rowcount, "ligne(s) supprimée(s)")

# -------------------------------
# 8. Affichage final des étudiants
# -------------------------------
cursor.execute("SELECT * FROM Etudiants")
print("Étudiants après suppression :")
for row in cursor.fetchall():
    print(row)

# -------------------------------
# Affichage des cours après suppression
# -------------------------------
cursor.execute("SELECT * FROM Cours")
print("Cours après suppression :")
for row in cursor.fetchall():
    print(row)


cursor.close()
conn.close()