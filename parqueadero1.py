from datetime import datetime

parqueaderoCarro = [
                    
"v1","v2","v3","v4","v5","v6","v7","v8","v9","v10",
"v11","v12","v13","v14","v15","v16","v17","v18","v19","v20",
"v21","v22","v23","v24","v25","v26","v27","v28","v29","v30",
"v31","v32","v33","v34","v35","v36","v37","v38","v39","v40",
"v41","v42","v43","v44","v45","v46","v47","v48","v49","v50"
]

parqueaderoMoto = [
                    
"m1","m2","m3","m4","m5","m6","m7","m8","m9","m10",
"m11","m12","m13","m14","m15","m16","m17","m18","m19","m20",
"m21","m22","m23","m24","m25"
]
vehiculos = {}

def agregar(parqueaderoCarro, parqueaderoMoto,vehiculos):
   
    tipoVehiculo = input("Escribe si es moto o carro: ")
    placa = input("Escribe la placa: ")
    espacio = input("Escoga un espacio para agregar: ")
    horaEntrada = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("")
    if tipoVehiculo == 'carro':
            if espacio not in parqueaderoCarro:
                print("El espacio ya esta ocupado")
                menu(parqueaderoCarro,parqueaderoMoto,vehiculos)
            elif espacio in parqueaderoCarro:
                indice = parqueaderoCarro.index(espacio)
                parqueaderoCarro[indice] = 'O'
                vehiculos[placa] = {
                    'indice': indice,
                    'tipoVehiculo': tipoVehiculo,
                    'estado': 'O',
                    'mostrar': espacio,
                    'horaEntrada': horaEntrada
                }
                print(f"Vehículo agregado en el espacio {espacio}.")
                menu(parqueaderoCarro,parqueaderoMoto,vehiculos)
           
    elif tipoVehiculo == 'moto':
            if espacio not in parqueaderoMoto:
                print("El espacio ya esta ocupado")
                menu(parqueaderoCarro,parqueaderoMoto,vehiculos)

            elif espacio in parqueaderoMoto:
                indice = parqueaderoMoto.index(espacio)
                parqueaderoMoto[indice] = 'O'
                vehiculos[placa] = {
                    'indice': indice,
                    'tipoVehiculo': tipoVehiculo,
                    'estado': 'O',
                    'mostrar': espacio,
                    'horaEntrada': horaEntrada
                }
                print(f"Vehículo agregado en el espacio {espacio}.")
                menu(parqueaderoCarro,parqueaderoMoto,vehiculos)

def alquiler(parqueaderoCarro,parqueaderoMoto,vehiculos):
   
    tipoVehiculo = input("Escribe si es moto o carro: ")
    placa = input("Escribe la placa: ")
    espacio = input("Escoga un espacio para agregar: ")
    horaEntrada = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("")

    if tipoVehiculo == 'carro':
            if espacio not in parqueaderoCarro:
                print("El espacio ya esta alquilado")
                menu(parqueaderoCarro,parqueaderoMoto,vehiculos)

            elif espacio in parqueaderoCarro:
                indice = parqueaderoCarro.index(espacio)
                parqueaderoCarro[indice] = 'A'
                vehiculos[placa] = {
                    'indice': indice,
                    'tipoVehiculo': tipoVehiculo,
                    'estado': 'A',
                    'mostrar': espacio,
                    'horaEntrada': horaEntrada
                }
                print(f"Vehículo alquilado en el espacio {espacio}")
                menu(parqueaderoCarro,parqueaderoMoto,vehiculos)
    
    elif tipoVehiculo == 'moto':
        if espacio not in parqueaderoMoto:
                print("El espacio ya esta alquilado")
                menu(parqueaderoCarro,parqueaderoMoto,vehiculos)

        if espacio in parqueaderoMoto:
                indice = parqueaderoMoto.index(espacio)
                parqueaderoMoto[indice] = 'A'
                vehiculos[placa] = {
                    'indice': indice,
                    'tipoVehiculo': tipoVehiculo,
                    'estado': 'A',
                    'mostrar': espacio,
                    'horaEntrada': horaEntrada
                }
                print(f"Vehículo agregado en el espacio {espacio}")
                menu(parqueaderoCarro,parqueaderoMoto,vehiculos)

def salida(parqueaderoCarro, parqueaderoMoto, vehiculos):
    placa = input("Escriba la placa: ")

    fechaSalidaInput = input("Escriba la fecha de salida (formato YYYY-MM-DD): ")
    horaSalidaInput = input("Escriba la hora de salida (formato HH:MM:SS): ")
    try:
        horaSalida = datetime.strptime(f"{fechaSalidaInput} {horaSalidaInput}", "%Y-%m-%d %H:%M:%S")
    except ValueError:
        print("El formato de la hora de salida es incorrecto.")
        menu(parqueaderoCarro, parqueaderoMoto, vehiculos)
        return

    if placa not in vehiculos:
        print("El vehículo no está en el parqueadero.")
        menu(parqueaderoCarro, parqueaderoMoto, vehiculos)
        return

    vehiculo = vehiculos[placa]
    tipoVehiculo = vehiculo['tipoVehiculo']
    espacio = vehiculo['mostrar']
    indice = vehiculo['indice']
    estado = vehiculo['estado']
    
    if estado == 'A':
        print(f"El vehículo {tipoVehiculo} está en un espacio alquilado, no se genera cobro.")
        
    else:
        if tipoVehiculo == 'carro':
            parqueadero = parqueaderoCarro
            tarifaPorHora = 3000
        elif tipoVehiculo == 'moto':
            parqueadero = parqueaderoMoto
            tarifaPorHora = 1000
        else:
            print("Tipo de vehículo no válido.")
            menu(parqueaderoCarro, parqueaderoMoto, vehiculos)
            return

        horaEntrada = vehiculo['horaEntrada']
        entrada = datetime.strptime(horaEntrada, "%Y-%m-%d %H:%M:%S")

        totalHoras = (horaSalida - entrada).total_seconds() / 3600  # Convertir segundos a horas

        if totalHoras >= 11.2:  # Aplicar descuento si corresponde
            descuento = (tarifaPorHora * totalHoras * 0.15)
            pagoFinal = (tarifaPorHora * totalHoras) - descuento
        else:
            pagoFinal = tarifaPorHora * totalHoras

        print(f"Total de horas: {totalHoras:.2f} horas")
        print(f"El valor a pagar del vehículo es ${pagoFinal:,.2f}")

        # Restaurar el espacio a su estado original
        parqueadero[indice] = espacio

        print(f"El vehículo {tipoVehiculo} ha salido del espacio {espacio} el {horaSalida}.")
  
        # Eliminar el vehículo del diccionario
        del vehiculos[placa]

    menu(parqueaderoCarro, parqueaderoMoto, vehiculos)

def menu(parqueaderoCarro,parqueaderoMoto,vehiculos):
        print()
        print("Bienvenido al sistema de parqueadero")
        print("1. Mostrar matriz del parqueadero")
        print("2. Alquiler")
        print("3. Registrar entrada")
        print("4. Registrar salida y facturar")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            
            for i in range(len(parqueaderoCarro)):
                    print(parqueaderoCarro[i], end=' ')
                    if (i + 1) % 10 == 0:
                        print()
            print("****************************")
            
            for i in range(len(parqueaderoMoto)):
                    print(parqueaderoMoto[i], end=' ')
                    if (i + 1) % 10 == 0:
                        print()
            print("\n****************************")
            menu(parqueaderoCarro,parqueaderoMoto,vehiculos)
            for i in range(len(parqueaderoMoto)):
                print(parqueaderoMoto[i], end=' ')
            if (i + 1) % 10 == 0:
                print()
        elif opcion == '2':
            alquiler(parqueaderoCarro, parqueaderoMoto,vehiculos)
        elif opcion ==  '3':
            agregar(parqueaderoCarro,parqueaderoMoto,vehiculos)
        elif  opcion == '4':
             salida(parqueaderoCarro,parqueaderoMoto,vehiculos)
        elif opcion == '5':
            print("Gracias por utilizar el sistema de parqueadero")
            exit()
        else:
         print("")
         print("SELECCIONE UNA OPCION VALIDA")
         menu(parqueaderoCarro,parqueaderoMoto,vehiculos)
menu(parqueaderoCarro,parqueaderoMoto,vehiculos)