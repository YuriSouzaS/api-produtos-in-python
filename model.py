import mysql.connector
from mysql.connector import errorcode
import os

key: str = os.getenv("MYDB")

config = {

    'user': 'whoami',
    'password': key,
    'host': 'localhost',
    'port': '3306',
    'database': 'bdapi'
}

setProd = {}

def cnx():

    try:
        conn = mysql.connector.connect(**config)
        
    except mysql.connector.Error as err:
        
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:  
            print('Erro na conexão')
            
        elif err.errno == errorcode.ER_BAD_DB_ERROR:           
            print('Banco de dados não existe')
            
        else:
            print(err)
            
    else:
        conn.close()
    
    return True

    
def insert(name: str, amount: int, desc: str, image: str, price: float) -> None:
    
    query = f"""INSERT INTO produtos
                (NAME, AMOUNT, DESCRIPTION, IMAGE, PRICE )
                VALUES ('{name}', {amount}, '{desc}', '{image}', {price})"""
    
    conn = mysql.connector.connect(**config)
    
    if conn and conn.is_connected():
        with conn.cursor() as cursor:
            cursor.execute(query)
            res = cursor.lastrowid
            
            conn.commit()
            
        cursor.close()
        
    conn.close()


def select_all():
    
    conn = mysql.connector.connect(**config)
    
    if conn and conn.is_connected():
        
        with conn.cursor() as cursor:

            cursor.execute("SELECT * FROM produtos")

            rows = cursor.fetchall()

            count = 0
            for i in rows:
                count += 1
                setProd[str(i[0])] = {"name":i[1],"amount": i[2], "desc": i[3], "image": i[4], "price": i[5]}
            
            cursor.close()
                
        conn.close()
        
    else:
        print('conexão fechada')
    
    return setProd

def alter(new_value: int, id: int):
    conn = mysql.connector.connect(**config)
    
    query = f"UPDATE produtos SET amount = {new_value} WHERE id = {id}"
    
    if conn and conn.is_connected():
        
        with conn.cursor() as cursor:
           
           cursor.execute(query)
        
           conn.commit()
    return True

def delete(id: int):
    conn = mysql.connector.connect(**config)
    
    query = f""" DELETE FROM produtos WHERE id = {id} """
    
    if conn and conn.cursor():
        with conn.cursor() as cursor:
            
            cursor.execute(query)
            
            conn.commit()
            
    return True