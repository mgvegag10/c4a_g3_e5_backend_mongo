# c4a_g3_e5_backend
Backend logica de la aplicacion

Versión de Python usada : 3.10

1. Clonar la rama main del repositorio.
3. Instalar los requerimientos de requeriments.txt
2. Abrir DataBase.py del directorio Database.
3. Reescribir las credenciales de la base de datos local de postgresql
     Configuración
     app.config['SQLALCHEMY_DATABASE_URI'] = 'dialect+driver://username:password@host:port/database'
     
     Ejemplo:
     app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Juancarrillo@localhost/postgres'
