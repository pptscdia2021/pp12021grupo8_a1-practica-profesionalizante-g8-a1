import pymysql
try:
    conexion = pymysql.connect(host='localhost',
                               user='root',
                               password='Ceci2803',
                               db='employees')
    try:
        with conexion.cursor() as cursor:

            # Como el num de empleado 1000 ya existe, busco el maximo emp_no con
            # SELECT max(emp_no) FROM employees e inserto el siguiente

            consulta = "INSERT INTO employees VALUES ('500001', 'd010', '2021-01-01', '9999-01-01');"
            # Podemos llamar muchas veces a .execute con datos distintos
            #cursor.execute(consulta, ('500000', '1985-01-01','Pepe', 'Pe','M','1985-01-01'))
            #cursor.execute(consulta, ())
            #cursor.execute(consulta, ())
            #cursor.execute(consulta, ())
        conexion.commit()
    finally:
        conexion.close()
except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
    print("Ocurrió un error al conectar: ", e)
