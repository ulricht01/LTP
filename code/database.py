import mariadb

def otevri_spojeni():
    config = {
        'user': 'root',
        'password': 'secret',
        'host': 'mariadb-mc',
        'port': 3306,
        'database': 'minecraft',
    }
    connection = mariadb.connect(**config)
    cursor = mariadb.Cursor(connection)
    return connection, cursor

def vytvor_db():
    config = {
            'user': 'root',
            'password': 'secret',
            'host': 'mariadb-mc',
            'port': 3306,
        }
    connection = mariadb.connect(**config)
    cursor = mariadb.Cursor(connection)
    cursor.execute("CREATE DATABASE IF NOT EXISTS minecraft")
    cursor.close()
    connection.close()

def vytvor_tabulky():
    connection, cursor = otevri_spojeni()
    cursor.execute("""CREATE TABLE IF NOT EXISTS uzivatele(
                                id INT(6) NOT NULL AUTO_INCREMENT PRIMARY KEY,
                                uuid VARCHAR(36) NOT NULL,
                                uzivatel VARCHAR(20) NOT NULL,
                                heslo VARCHAR(20) NOT NULL
                            ) ENGINE=InnoDB;""")
    cursor.close()
    connection.close()

def pridej_uzivatele(uuid, uzivatel, heslo):
    connection, cursor = otevri_spojeni()
    cursor.execute(""" INSERT INTO uzivatele (uuid, uzivatel, heslo) VALUES (%s, %s, %s)""", (uuid, uzivatel, heslo,))
    cursor.close()
    connection.commit()
    connection.close()

def check_uzivatel(uzivatel):
    connection, cursor = otevri_spojeni()
    cursor.execute(""" SELECT uzivatel FROM uzivatele WHERE uzivatel = %s LIMIT 1""", (uzivatel,))
    result = cursor.fetchone()
    connection.commit()
    connection.close()
    return result

def vypis_whitelist():
    connection, cursor = otevri_spojeni()
    cursor.execute(""" SELECT uuid, uzivatel FROM uzivatele""")
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result