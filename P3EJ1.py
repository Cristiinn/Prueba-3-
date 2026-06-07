#Ingresar medicos 
residente_junior = 0
especialista_senior = 0

while True:
    try: 
        cantidad_medicos = int (input ("¿Cuantos medicos desea registrar?: "))
        if cantidad_medicos >0 :
            print (f"Se han ingresado {cantidad_medicos} médicos")
            break
        else:
             print ("Registro médico inválido! Ingresa un entero positivo para continuar")
    except: 
            print ("Registro médico inválido! Ingresa un entero positivo para continuar")
        
    
for i in range (cantidad_medicos):
     print(f"\n--- Registro médico {i+1} ---")
     while True: 
          apodo = input ("Ingrese apodo del médico (este debe tener al menos 6 carácteres y no contener espacios):  ").strip()
          if (len(apodo) <6 ) or (' ' in apodo):
               print ("El apodo debe tener almenos 6 carácteres y no contener espacios!!!!!>:(")
               
          else: 
               print ("Apodo registrado exitosamente :) ")
               break

     while True: 
            try: 
                años_experiencia = int (input("Ingrese cantidad de años de experiencia del/la médico : "))
                if años_experiencia >0:
                    print (f"Se le han ingresado {años_experiencia} años de experiencia al médico ")
                    break
                else: 
                     print ("¡Error clínico! Ingresa un número entero positivo para la experiencia.")
            except:
                    print ("¡Error clínico! Ingresa un número entero positivo para la experiencia.") 

   

     if años_experiencia <= 5:
        print("Médico residente junior")
        residente_junior += 1

     else:
        print("Médico especialista senior")
        especialista_senior += 1

        print(f"\n¡El hospital cuenta con {especialista_senior} Especialistas Senior y {residente_junior} Residentes Junior! ¡Sistema listo para operar!")


                        
