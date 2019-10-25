import sqlite3




db = sqlite3.connect('prueba.db')    # SE REALIZA LA CONEXION A LA BASE DE DATOS
cur = db.cursor()   # SE CREA EL CURSOR, EL CUAL PERMITE REALIZAR TODAS LAS QUERYS QUE QUERAMOS

#cur.execute('''create table pruebapy (id, nombre, apellido, direccion)''') # SE EJECUTA LA QUERY

cur.execute('''insert into pruebapy(id, nombre, apellido, direccion)
                values(1, 'Mario', 'Gomez', 'Calle falsa 123')
                 
            
            
            ''')


db.commit() # GUARDAMOS TODOS LOS CAMBIOS

db.close()  # CERRAMOS LA CONEXION CON LA BASE DE DATOS

