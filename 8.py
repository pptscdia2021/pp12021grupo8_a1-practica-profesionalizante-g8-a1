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

            consulta = "SELECT ed.dept_no, sum(salary) FROM salaries es, dept_emp ed where es.emp_no= ed.emp_no group by dept_no;"
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
