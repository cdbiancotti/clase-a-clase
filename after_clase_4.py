max_horas_desarrollador_tiempo_completo = 50
max_extras_desarrollador_tiempo_completo = 10
porcentaje_extra_desarrollador_tiempo_completo = 1.5

max_horas_desarrollador_tiempo_parcial = 25
max_extras_desarrollador_tiempo_parcial = 5
porcentaje_extra_desarrollador_tiempo_parcial = 1.5

max_horas_lider_de_equipo = 65
max_extras_lider_de_equipo = 15
porcentaje_extra_lider_de_equipo = 2

max_horas_reclutador_a = 45
max_extras_reclutador_a = 5
porcentaje_extra_reclutador_a = 1.75

desarrollador_tiempo_completo = '1'
desarrollador_tiempo_parcial = '2'
lider_de_equipo = '3'
reclutador_a = '4'

flag = True
while flag:
    puesto = input('''En cual de los siguientes puestos te desarrollas:
    1. Desarrollador a tiempo completo.
    2. Desarrollador a tiempo parcial.
    3. Líder de equipo.
    4. Reclutador/a.
    ( Ingrese el numero correspondiente a su posición o digite 0 para salir.) ''')
    if puesto == '0':
        flag = False
        continue
    valor_horas = float(input('Cuanto cobras por hora? '))
    horas_trabajadas = float(input('Cuantas horas trabajaste esta semana? '))

    porcentaje_a_utilizar = 0
    horas_base_posicion = 0
    max_horas_extras_posicion = 0

    if puesto == desarrollador_tiempo_completo:
        horas_base_posicion = max_horas_desarrollador_tiempo_completo - max_extras_desarrollador_tiempo_completo
        max_horas_extras_posicion = max_extras_desarrollador_tiempo_completo
        porcentaje_a_utilizar = porcentaje_extra_desarrollador_tiempo_completo

    elif puesto == desarrollador_tiempo_parcial:
        horas_base_posicion = max_horas_desarrollador_tiempo_parcial - max_extras_desarrollador_tiempo_parcial
        max_horas_extras_posicion = max_extras_desarrollador_tiempo_parcial
        porcentaje_a_utilizar = porcentaje_extra_desarrollador_tiempo_parcial

    elif puesto == lider_de_equipo:
        horas_base_posicion = max_horas_lider_de_equipo - max_extras_lider_de_equipo
        max_horas_extras_posicion = max_extras_lider_de_equipo
        porcentaje_a_utilizar = porcentaje_extra_lider_de_equipo

    elif puesto == reclutador_a:
        horas_base_posicion = max_horas_reclutador_a - max_extras_reclutador_a
        max_horas_extras_posicion = max_extras_reclutador_a
        porcentaje_a_utilizar = porcentaje_extra_reclutador_a

    if horas_trabajadas > horas_base_posicion + max_horas_extras_posicion:
        print('Te excediste en la cantidad de horas trabajadas.')
        horas_trabajadas = horas_base_posicion + max_horas_extras_posicion

    horas_extra_trabajadas = horas_trabajadas - horas_base_posicion
    cobro_horas_base = horas_base_posicion * valor_horas
    cobro_horas_extras = horas_extra_trabajadas * valor_horas * porcentaje_a_utilizar

    salario_semanal = cobro_horas_base + cobro_horas_extras

    print('Tu salario de esta semana es de', salario_semanal, end='\n\n')

else:
    print('Nos vemos!')