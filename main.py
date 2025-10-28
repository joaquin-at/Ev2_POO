import os

from dao import DepartamentoDAO, EmpleadoDAO, ProyectoDAO, RegistroTiempoDAO, UsuarioDAO

### Menú de login###

def menu_login():
    while True:
        os.system('cls')
        print('==== Sistema de Gestión de Empleados - EcoTech Solutions ====')
        print('1. Iniciar Sesión')
        print('2. Crear Cuenta')
        print('0. Salir')

        opcion = input('\nSeleccione una opción: ')
        os.system('cls')

        if opcion == '1':
            print('==== Iniciar Sesión ====')
            username = input('Ingrese nombre de usuario: ')
            password = input('Ingrese contraseña: ')

            usuarioDao = UsuarioDAO()
            usuario = usuarioDao.login(username, password)

            if usuario:
                print(f'\nBienvenido {usuario.username} ({usuario.rol})')
                menu_main(usuario)
            else: print('\nUsuario y/o contraseña inválidos')

        elif opcion == '2':
            print('==== Crear nueva cuenta ====')
            id_empleado = input('Ingrese ID de empleado: ')
            username = input('Ingrese nombre de usuario: ')
            password = input('Ingrese contraseña: ')
            rol = input('Ingrese rol (admin / empleado): ')

            usuarioDao = UsuarioDAO()
            usuarioDao.crear_usuario(id_empleado, username, password, rol)
            print('\nCuenta creada correctamente.')
        
        elif opcion == '0':
            print('Saliendo del sistema...')
            break

        else:
            print('Opción no válida.')

        input('\nPresione ENTER para continuar...')


### Menu Principal ###

def menu_main(usuario):
    while True:
        os.system('cls')
        print(f'Bienvenido/a {usuario.username} | Rol: {usuario.rol}')
        print('==== Menú Principal ====')
        print('1. Registrar nuevo empleado')
        print('2. Ver empleados')
        print('3. Crear departamento')
        print('4. Ver proyectos')
        print('5. Registrar horas trabajadas')
        print('0. Cerrar sesión')

        opcion = input('\nSeleccione una opción: ')
        os.system('cls')

        empleadoDao = EmpleadoDAO()
        deptoDao = DepartamentoDAO()
        proyectoDao = ProyectoDAO()
        registroDao = RegistroTiempoDAO()

        if opcion == '1':
            print('==== Registrar Empleado ====')
            id_empleado = input('ID Empleado: ')
            nombre = input('Nombre: ')
            direccion = input('Dirección:')
            telefono = input('Teléfono: ')
            email = input('Correo:')
            fecha_inicio = input('Fecha de inicio (YYYY-MM-DD): ')
            salario = input('Salario: ')
            tipo_empleado = input('Tipo de empleado: ')
            id_departamento = input('ID Departamento (opcional): ')

            empleadoDao.insertar_empleado(id_empleado, id_departamento or None, nombre, direccion, telefono, email, fecha_inicio, salario, tipo_empleado)
            print('nEmpleado registrado con éxito.')
        
        elif opcion =='2':
            print('==== Lista de Empleados ====')
            empleados = empleadoDao.listar_empleado()
            for emp in empleados:
                print(emp)
            input('\nPresione ENTER para continuar...')

        elif opcion == '3':
            print('==== Crear Departamento ====')
            id_dep = input('ID Departamento:')
            nombre = input('Nombre: ')
            id_gerente = input('ID Gerente: ')
            id_empleado = input('ID Empleado Gerentes: ')
            deptoDao.insertar_departamento(id_dep, nombre, id_gerente, id_empleado)
            print('\nDepartamento creado correctamente.')

        elif opcion == '4':
            print('==== Lista de proyectos ====')
            proyectos = proyectoDao.listar_proyectos()
            for p in proyectos:
                print(p)
            input('\nPresione ENTER para continuar...')

        elif opcion == '5':
            print('==== Registrar Horas de Trabajo ====')
            id_reg = input('ID Registro: ')
            id_emp = input('ID empleado: ')
            id_proy = input('ID Proyecto: ')
            fecha = input('Fecha (YYYY-MM-DD): ')
            horas = input('Horas trabajadas: ')
            desc = input('Descripción de tareas: ')
            registroDao.insertar_registro(id_reg, id_emp, id_proy, fecha, horas, desc)
            print('\nHoras registradas correctamente.')

        elif opcion == '0':
            print('Cerrando sesión...')
            break

        else:
            print('Opción no válida.')
        input('\nPresione ENTER para continuar...')

### Ejecución ###
if __name__ == '__main__':
    menu_login()





        

    