import json
#Funciones
#Aquí están todas las funciones que usaremos en el proyecto
#Esto va lo primero en el programa
def reg_ingr_diar(dia):
    fecha=input('¿Es su primer ingreso del día?\n1.Sí\n2.No\n')
    if(fecha=='1'):
        ingre=open('ingreso_parqueadero.json','r')
        aringr=json.load(ingre)
        sali=open('salida_parqueadero.json','r')
        arsal=json.load(sali)
        aringr[dia]={'Registrados':[],'Visitantes':[]}
        arsal[dia]={'Pagos Diarios':[],'Pagos Mensuales':[]}
        with open('ingreso_parqueadero.json','w') as file:
            json.dump(aringr, file, indent=4)
        with open('salida_parqueadero.json','w') as file:
            json.dump(arsal, file, indent=4)
    elif(fecha==2):
        print('Dato inválido, vuelva a iniciar el programa')
#Funciones de los datos
def tipo_auto(x=0):
    while x!=-1:
        tipveh=input('Tipo de vehículo:\n 1.Automóvil\n 2.Automóvil eléctrico\n 3.Motocicleta\n 4.Discapacitado\n')
        if('1'==tipveh):
            tipveh='Automóvil'
            x=-1
        elif('2'==tipveh):
            tipveh='Automóvil eléctrico'
            x=-1
        elif('3'==tipveh):
            tipveh='Motocicleta'
            x=-1
        elif('4'==tipveh):
            tipveh='Discapacitado'
            x=-1
        else:
            print('Tipo de vehículo inválido. Vuelva a intentar')
    return tipveh
def pla_pago(x=0):
    while x!=-2:
        plpag=input('Elija su plan de pago:\n 1.Mensualidad\n 2.Diario\n ')
        if('1'==plpag):
            plpag='Mensualidad'
            x=-2
        elif('2'==plpag):
            plpag='Diario'
            x=-2
        else:
            print('Plan de pago inválido. Vuelva a intentar')
    return plpag
def recorrer_id(n=0):
    usua=open('usuarios.json','r')
    datosus=json.load(usua)
    num_id=[]
    usu=[]
    for x in datosus['usuarios']:
        idus=datosus['usuarios'][n][1]
        num_id.append(idus)
        n+=1
        usu.append(x)
    return num_id
def recorrer_pl(n=0):
    usua=open('usuarios.json','r')
    datosus=json.load(usua)
    num_pl=[]
    usu=[]
    for x in datosus['usuarios']:
        idus=datosus['usuarios'][n][3]
        num_pl.append(idus)
        n+=1
        usu.append(x)
    return num_pl
def elegir_piso(x=0):
    while (x!=-1):
        piso=input('Digite el número del piso al que quiere acceder (Recuerde que solo hay 6 pisos): ')
        if(piso=='1'):
            piso='Piso1'
            x=-1
        elif(piso=='2'):
            piso='Piso2' 
            x=-1
        elif(piso=='3'):
            piso='Piso3'
            x=-1
        elif(piso=='4'):
            piso='Piso4'
            x=-1
        elif(piso=='5'):
            piso='Piso5'
            x=-1
        elif(piso=='6'):
            piso='Piso6'
            x=-1
        else:
            print('Número de piso inválido. Vuelva a intentarlo')
    return piso
def con_tip(tipo=0):
    if(tipo==0):
        tipo=tipo_auto()
    
    if(tipo=='Automóvil'):
        tipo=1
    elif(tipo=='Automóvil eléctrico'):
        tipo=2
    elif(tipo=='Motocicleta'):
        tipo=3
    else:
        tipo=4
    return tipo
def extra_tipauto_usuario (placa,n=0,x=0):
    usua=open('usuarios.json','r')
    datosus=json.load(usua)
    for x in datosus['usuarios']:
        idin= placa in x
        if(idin==True):
            tipo=datosus['usuarios'][n][4]    
        n+=1
    return tipo
def recor_plac(dia,placa,n=0,m=0,x=0,y=0):
    ingre=open('ingreso_parqueadero.json','r')
    aringr=json.load(ingre)
    vis=None
    usu=[]
    for x in aringr[dia]['Registrados']:
        if(aringr[dia]['Registrados'][n][3] == placa):
            vis=False
        n+=1
        usu.append(x)
    for y in aringr[dia]['Visitantes']:
        if(aringr[dia]['Visitantes'][m][1] == placa):
            vis=True
        m+=1
        usu.append(y)
    return vis
def recor_plan(dia,placa,n=0):
    ingre=open('ingreso_parqueadero.json','r')
    aringr=json.load(ingre)
    pago_diario=False
    usu=[]
    for x in aringr[dia]['Registrados']:
        if(aringr[dia]['Registrados'][n][3] == placa):
            print(x)
            if(aringr[dia]['Registrados'][n][5] == 'Diario'):
                pago_diario=True
        n+=1
    usu.append(x)
    return pago_diario
def recortip_sal(dia,coor,vis,x=0,w=0):
    ingre=open('ingreso_parqueadero.json','r')
    aringr=json.load(ingre)
    while x < len(aringr[dia]['Visitantes']):
        if(aringr[dia]['Visitantes'][x][4] == coor):
            tipo=aringr[dia]['Visitantes'][x][2]
            tipo=con_tip(tipo)
        x+=1
    while w < len(aringr[dia]['Registrados']):
        if(aringr[dia]['Registrados'][w][6] == coor):
            tipo=aringr[dia]['Registrados'][w][4]
            tipo=con_tip(tipo)
        w+=1
    return tipo
def recorcoor_sal(dia,vis,placa,n=0,z=0,x=0,w=0):
    ingre=open('ingreso_parqueadero.json','r')
    aringr=json.load(ingre)
    if(vis==True):
        while x < len(aringr[dia]['Visitantes']):
            if(aringr[dia]['Visitantes'][x][1] == placa):
                coor=aringr[dia]['Visitantes'][x][4]
            x+=1
    else:
        while w < len(aringr[dia]['Registrados']):
            if(aringr[dia]['Registrados'][w][3] == placa):
                coor=aringr[dia]['Registrados'][w][6]
            w+=1
    return coor
def tipo_usu(x=0):
    while x!=-2:
        tiusu=input('Tipo de usuario:\n 1.Personal Administrativo\n 2.Profesor\n 3.Estudiante\n')
        if('1'== tiusu):
            tiusu='Personal Administrativo'
            x=-2
        elif('2'== tiusu):
            tiusu='Profesor'
            x=-2
        elif('3'== tiusu):
            tiusu='Estudiante'
            x=-2
        else:
            print('Plan de pago inválido. Vuelva a intentar')
    return tiusu
#Registro:
def eliminar_regis(id,x=0):
    usua=open('usuarios.json','r')
    datosus=json.load(usua)
    while x < len(datosus['usuarios']):
        idx=recorrer_id()
        idin = id in idx
        print(idin)
        if(idin==True):
            del datosus['usuarios'][x]
            with open('usuarios.json','w') as file:
                json.dump(datosus,file,indent=4)
            num_id=recorrer_id()
            idinf= id in num_id
            if(idinf == False):
                print('Eliminación exitosa')
        x+=1
def registro_usuarios (x=0):
    nomap=input('Escriba sus nombres y apellidos: ')
    numid=eval(input('Escriba su número de identificación: '))
    placa=input('Escriba la placa de su vehículo: ')
    tiusu=tipo_usu()
    tipveh=tipo_auto()
    plpag=pla_pago()
    usua=open('usuarios.json','r')
    datosus=json.load(usua)
    num_id=recorrer_id()
    idinf=numid in num_id
    if(idinf==True):
        print('Usted ya se registó, recuerde que no puede registrar más de un vehículo a su nombre.')
        redig=input('¿Desea eliminar su registro anterior?\n 1.Sí\n 2.No\n')
        if(redig=='1'):
            eliminar_regis(numid)
    else:
        datosus['usuarios'].append([nomap,numid,tiusu,placa,tipveh,plpag])
        with open('usuarios.json','w') as file:
            json.dump(datosus,file,indent=4)
        num_id=recorrer_id()
        idinf= numid in num_id
        if(idinf == True):
            print('Registro exitoso')
        else:
            print('Revise sus datos')
#Ingreso:
#  Parqueaderos disponibles
def reco_pisos(tipo):
    dispo=open('disponibilidad.json','r')
    ardis=json.load(dispo)
    x=0
    postotal=0
    for x in range (5):
        y=0
        posti=0
        if(x==0):
            piso='Piso1'
        elif(x==1):
            piso='Piso2'
        elif(x==2):
            piso='Piso3'
        elif(x==3):
            piso='Piso4'
        elif(x==4):
            piso='Piso5'
        else:
            piso='Piso6'
        while y < len(ardis[piso]):
            z=0
            posiciones=0
            while z < len(ardis[piso][y]):
                ele=ardis[piso][y][z]
                if(tipo==ele):
                    posiciones+=1
                z+=1
            posti+=posiciones
            y+=1
        postotal+=posti
    print('Hay '+str(postotal)+' estacionamientos disponibles para usted.')
def mapa_pisos(tipo,piso,y=0):
    dispo=open('disponibilidad.json','r')
    ardis=json.load(dispo)
    posti=0
    print('¿Cómo entender el mapa?\n0 = Parqueadero disponible\nX = Parqueadero no disponible')
    while y < len(ardis[piso]):
        z=0
        posiciones=0
        dispo=''
        while z < len(ardis[piso][y]):
            ele=ardis[piso][y][z]
            if(tipo==ele):
                dispo+='  0'
                posiciones+=1
            else:
                dispo+='  X'
            z+=1
        posti+=posiciones
        print(dispo)
        y+=1
    print('Hay '+str(posti)+' estacionamientos disponibles para usted en este piso.')
def archivar_ingreso(tipo,piso):
    dispo=open('disponibilidad.json','r')
    ardis=json.load(dispo)
    print('Ingrese las coordenadas de su estacionamiento (comience a contar desde el 0)')
    fila=int(input('Fila (cuente de arriba a abajo): '))
    columna=int(input('Columna (cuente de izquiera a derecha): '))
    if(tipo==ardis[piso][fila][columna]):
        coor=[piso,fila,columna]
        ardis[piso][fila][columna]=0
        with open('disponibilidad.json','w') as file:
            json.dump(ardis,file,indent=4)
        print('Puede ingresar, muchas gracias por registrarse.')
    else:
        print('Sus coordenadas son inválidas. Vuelva a intentar')
        return archivar_ingreso(tipo,piso)
    return coor
def disp(tipo=0,z=0):
    tipo=con_tip(tipo)
    reco_pisos(tipo)
    while z!=-1:
        piso=elegir_piso()
        mapa_pisos(tipo,piso)
        vol=input('1.Estacionar en este piso\n2.Ver mapa de otro piso\n')
        if(vol=='1'):
            coor=archivar_ingreso(tipo,piso)
            z=-1
    return coor
#  Registro diario
def ingr_vis(dia,placa,auto,coor):
    ingre=open('ingreso_parqueadero.json','r')
    aringr=json.load(ingre)
    infvis=['Visitante',placa,auto,'Diario',coor]
    aringr[dia]['Visitantes'].append(infvis)
    with open('ingreso_parqueadero.json','w') as file:
        json.dump(aringr, file, indent=4)
def ingr_usu(dia,placa,coor,x=0, n=0):
    ingre=open('ingreso_parqueadero.json','r')
    aringr=json.load(ingre)
    usua=open('usuarios.json','r')
    datosus=json.load(usua)
    for x in datosus['usuarios']:
        idin= placa in x
        if(idin==True):
            datosus['usuarios'][n].append(coor)
            infusreg=datosus['usuarios'][n]    
        n+=1
    aringr[dia]['Registrados'].append(infusreg)
    with open('ingreso_parqueadero.json','w') as file:
        json.dump(aringr, file, indent=4)
def ingr(dia):
    placa=input('Ingrese la placa del vehículo: ')
    usua=open('usuarios.json','r')
    json.load(usua)
    num_pl=recorrer_pl()
    numpl= placa in num_pl
    if(numpl==True):
        coor=disp()
        extra_tipauto_usuario(placa)
        ingr_usu(dia,placa,coor)
    else:
        auto=tipo_auto()
        coor=disp(auto)
        ingr_vis(dia,placa,auto,coor)
#Cobro:
def pago_diario(dia,placa,horas,vis,n=0,z=0,x=0,w=0):
    min=horas/60
    cobro=0
    ingre=open('ingreso_parqueadero.json','r')
    aringr=json.load(ingre)
    sali=open('salida_parqueadero.json','r')
    arsal=json.load(sali)
    if(vis==True):
        cobro=3000*min
        print('Su valor a pagar es de $'+str(cobro)+' pesos.')
        while z!=-1:
            eje=input('1.Terminé mi pago\n')
            if(eje=='1'):
                while x < len(aringr[dia]['Visitantes']):
                    if(aringr[dia]['Visitantes'][x][1] == placa):
                        aringr[dia]['Visitantes'][x].append(cobro)
                        lis=aringr[dia]['Visitantes'][x]
                        arsal[dia]["Pagos Diarios"].append(lis)
                        with open('salida_parqueadero.json','w') as file:
                            json.dump(arsal,file,indent=4)
                    x+=1
                print('Muchas gracias por visitarnos')
                z=-1
            else:
                print('Por favor termine su pago')
    else:
        tipousu=0
        usu=[]
        for x in aringr[dia]['Registrados']:
            if(aringr[dia]['Registrados'][n][3] == placa):
                tipousu=aringr[dia]['Registrados'][n][2]
            n+=1
            usu.append(x)
        if(tipousu=='Estudiante'):
            cobro=1000*min
        elif(tipousu=='Profesor'):
            cobro=2000*min
        else:
            cobro=1500*min
        print('Su valor a pagar es de $'+str(cobro)+' pesos.')
        while z!=-1:
            eje=input('1.Terminé mi pago\n')
            if(eje=='1'):
                while w < len(aringr[dia]['Registrados']):
                    if(aringr[dia]['Registrados'][w][3] == placa):
                        lis=aringr[dia]['Registrados'][w]
                        aringr[dia]['Registrados'][w].append(cobro)
                        arsal[dia]["Pagos Diarios"].append(lis)
                        with open('salida_parqueadero.json','w') as file:
                            json.dump(arsal,file,indent=4)
                    w+=1
                print('Muchas gracias por visitarnos')
                z=-1
            else:
                print('Por favor termine su pago')
def arch_salida_usu(dia,placa,n=0):
    ingre=open('ingreso_parqueadero.json','r')
    aringr=json.load(ingre)
    usu=[]
    for x in aringr[dia]['Registrados']:
        if(aringr[dia]['Registrados'][n][3] == placa):
            sali=open('salida_parqueadero.json','r')
            arsal=json.load(sali)
            arsal[dia]['Pagos Mensuales'].append(aringr[dia]['Registrados'][n])
            with open('salida_parqueadero.json','w') as file:
                json.dump(arsal, file, indent=4)
            print('Muchas gracias por visitarnos')
        n+=1
    usu.append(x)
def retirar_veh(dia,placa,horas,z=0,n=0,x=0):
    ingre=open('ingreso_parqueadero.json','r')
    json.load(ingre)
    vis= recor_plac(dia,placa)
    if (vis == False):
        plan=recor_plan(dia,placa)
        if (plan == True):
            pago_diario(dia,placa,horas,vis)
        else:
            print('Usted tiene plan de pago mensual, no debe pagar nada')
            arch_salida_usu(dia,placa)
        archivar_salida(dia,vis,placa)
    elif (vis == True):
        pago_diario(dia,placa,horas,vis)
        archivar_salida(dia,vis,placa)
    else:
        print('La placa no coincide con ninguna registrada. Intente de nuevo')
#Retiro vehículos:
def archivar_salida(dia,vis,placa):
    dispo=open('disponibilidad.json','r')
    ardis=json.load(dispo)
    coor=recorcoor_sal(dia,vis,placa)
    piso=coor[0]
    fila=coor[1]
    columna=coor[2]
    tipo=recortip_sal(dia,coor,vis)
    if(0==ardis[piso][fila][columna]):
        ardis[piso][fila][columna]=tipo
        with open('disponibilidad.json','w') as file:
            json.dump(ardis,file,indent=4)
#Estadisticas:
#Por tipo de usuario
def busca_tip_usu():
    ingre=open('ingreso_parqueadero.json','r')
    aringr=json.load(ingre)
    ran=[]
    x=0
    totalvisitas=0
    perad=0
    prof=0
    est=0
    vis=0
    for x in aringr.keys():
        y=0
        for y in aringr[x].keys():
            z=0
            n=0
            for z in aringr[x][y]:
                totalvisitas+=1
                if 'Personal Administrativo' in aringr[x][y][n]:
                    perad+=1
                elif 'Profesor' in aringr[x][y][n]:
                    prof+=1
                elif 'Estudiante' in aringr[x][y][n]:
                    est+=1
                else:
                    vis+=1
                n+=1
                ran.append(z)

    datos={'Total de ocupacion':totalvisitas,'Personal Administrativo':perad,'Profesores':prof,'Estudiantes':est,'Visitantes':vis}
    return datos
def estadística_tipo_usu(x=0):
    dic_datos=busca_tip_usu()
    arch=open('Estadística_tipo_usuario.txt','w')
    arch.writelines('Cantidad de vehiculos estacionados segun tipo de usuario\n')
    datos=dic_datos.items()
    for x in datos:
        arch.writelines(str(x)+'\n')
    arch.close()
#Por tipo de vehiculo
def busca_tip_veh():
    ingre=open('ingreso_parqueadero.json','r')
    aringr=json.load(ingre)
    ran=[]
    x=0
    totalvisitas=0
    auto=0
    auotele=0
    moto=0
    disc=0
    for x in aringr.keys():
        y=0
        for y in aringr[x].keys():
            z=0
            n=0
            for z in aringr[x][y]:
                totalvisitas+=1
                if 'Automóvil' in aringr[x][y][n]:
                    auto+=1
                elif 'Automóvil eléctrico' in aringr[x][y][n]:
                    auotele+=1
                elif 'Motocicleta' in aringr[x][y][n]:
                    moto+=1
                else:
                    disc+=1
                n+=1
                ran.append(z)

    datos={'Total de ocupacion':totalvisitas,'Automovil':auto,'Automovil electrico':auotele,'Motocicleta':moto,'Discapacitados':disc}
    return datos
def estadística_tipo_veh(x=0):
    dic_datos=busca_tip_veh()
    arch=open('Estadística_tipo_vehículo.txt','w')
    arch.writelines('Cantidad de estacionados segun tipo de vehiculo\n')
    datos=dic_datos.items()
    for x in datos:
        arch.writelines(str(x)+'\n')
    arch.close()
#Porcentaje ocupación
def cuenta_ocu():
    ingre=open('disponibilidad.json','r')
    dispo=json.load(ingre)
    ran=[]
    p1=0
    p2=0
    p3=0
    p4=0
    p5=0
    p6=0
    x=0
    total=0
    for x in dispo.keys():
        y=0
        m=0
        for y in dispo[x]:
            z=0
            n=0
            for z in dispo[x][m]:
                if 0 == dispo[x][m][n]:
                    total+=1
                    if x=='Piso1':
                        p1+=1
                    elif x=='Piso2':
                        p2+=1
                    elif x=='Piso3':
                        p3+=1
                    elif x=='Piso4':
                        p4+=1
                    elif x=='Piso5':
                        p5+=1
                    else:
                        p6+=1
                n+=1
                ran.append(z)
            ran.append(y)
            m+=1
    dato={'Piso 1':p1,'Piso 2':p2,'Piso 3':p3,'Piso 4':p4,'Piso 5':p5,'Piso 6':p6}
    return total,dato
def porcentaje_global(total):
    porc_glo=total/550
    porc_glo*=100
    return porc_glo
def porcentaje_pisos(datospis):
    for x in datospis.keys():
        if x == 'Piso 6':
            por=(datospis[x]/50)*100
            datospis[x]=por
        else:
            datospis[x]=datospis[x]
    return datospis
def ocupación(x=0):
    total,datospis=cuenta_ocu()
    glo=porcentaje_global(total)
    porcentaje_pisos(datospis)
    arch=open('Porcentaje_ocupación.txt','w')
    arch.writelines('Porcentaje de ocupacion del parqueadero\n')
    arch.writelines('Porcentaje grobal: '+str(glo)+'%\n')
    for x in datospis.items():
        arch.writelines(str(x)+'\n')
    arch.close()
#Archivos:
def archivos_1():
    x={"usuarios": [
		["Dick Safford", 68433071, "Personal Administrativo", "LML817", "Automóvil", "Diario"],
		["Seely Salazar", 60844675, "Personal Administrativo", "CGH793", "Discapacitado", "Diario"],
		["Wakanda Schacht", 87399338, "Personal Administrativo", "BHO805", "Discapacitado", "Mensualidad"],
		["Beccalynn Nuno", 92881565, "Personal Administrativo", "JGO075", "Motocicleta", "Diario"],
		["Abundiantus Scroggs", 54208046, "Personal Administrativo", "HAN014", "Automóvil Eléctrico", "Mensualidad"],
		["Arran Zakrzewski", 52220774, "Personal Administrativo", "BND469", "Automóvil", "Mensualidad"],
		["Ludlow Cosenza", 55736674, "Profesor", "GDD423", "Motocicleta", "Diario"],
		["Ydel Cosenza", 83660267, "Personal Administrativo", "ADA415", "Discapacitado", "Diario"],
		["Halfrida Seely", 56345501, "Profesor", "NLC501", "Automóvil Eléctrico", "Mensualidad"],
		["Alyssa Cosenza", 56564894, "Estudiante", "DEH820", "Motocicleta", "Diario"],
		["Mercutio Braziel", 78852145, "Profesor", "NDM819", "Motocicleta", "Diario"],
		["Savita France", 79179368, "Personal Administrativo", "IIO972", "Motocicleta", "Mensualidad"],
		["Yoninah Schacht", 48148919, "Profesor", "OAG681", "Discapacitado", "Mensualidad"],
		["Dian Frankel", 46900165, "Profesor", "NFO807", "Motocicleta", "Mensualidad"],
		["Bae Kwan", 74758912, "Profesor", "KPN991", "Automóvil Eléctrico", "Mensualidad"],
		["Rollo Rushton", 58069811, "Estudiante", "GKL697", "Motocicleta", "Diario"],
		["Sunil Matheny", 68375813, "Estudiante", "COF952", "Discapacitado", "Diario"],
		["Calixte Belford", 66595778, "Profesor", "PHE566", "Automóvil Eléctrico", "Diario"],
		["Abundiantus Calixto", 95902170, "Personal Administrativo", "MOI952", "Automóvil", "Diario"],
		["Sigi Sharpe", 47953025, "Profesor", "CMJ913", "Motocicleta", "Mensualidad"]]}
    with open('Usuarios.json','w') as file:
        json.dump(x,file,indent=4)
    y={"Piso1": [[4, 4, 1, 2, 2, 2, 1, 1, 1, 4], 
    [1, 4, 1, 4, 1, 3, 1, 4, 2, 4], 
    [4, 4, 3, 4, 2, 3, 4, 3, 4, 2], 
    [1, 3, 1, 4, 3, 2, 2, 4, 3, 1], 
    [4, 3, 3, 4, 3, 4, 3, 2, 4, 1], 
    [4, 2, 1, 3, 4, 2, 2, 1, 1, 2], 
    [2, 3, 3, 1, 1, 3, 3, 2, 3, 1], 
    [1, 4, 2, 2, 1, 3, 1, 1, 2, 4], 
    [2, 4, 1, 4, 2, 1, 1, 2, 1, 3], 
    [2, 3, 1, 2, 4, 4, 2, 1, 3, 2]], 
    "Piso2": [[2, 2, 2, 3, 2, 1, 2, 2, 2, 1], 
    [2, 4, 1, 2, 3, 1, 3, 4, 1, 4], 
    [2, 1, 3, 4, 4, 1, 1, 1, 1, 4], 
    [3, 4, 3, 1, 2, 1, 1, 2, 3, 3], 
    [2, 3, 1, 1, 2, 1, 2, 3, 4, 1], 
    [3, 4, 2, 3, 3, 4, 3, 2, 1, 4], 
    [3, 1, 1, 2, 1, 4, 1, 1, 1, 3], 
    [1, 3, 2, 1, 4, 4, 1, 1, 3, 4], 
    [4, 3, 3, 2, 2, 4, 4, 1, 4, 3], 
    [2, 4, 3, 3, 1, 3, 3, 1, 2, 4]], 
    "Piso3": [[3, 4, 2, 4, 3, 2, 3, 1, 4, 2], 
    [3, 3, 2, 2, 4, 3, 3, 4, 4, 2], 
    [4, 4, 3, 3, 4, 3, 3, 1, 2, 3], 
    [1, 1, 2, 2, 2, 2, 4, 3, 4, 4], 
    [4, 2, 1, 1, 1, 1, 3, 3, 3, 2], 
    [1, 4, 2, 4, 2, 1, 2, 1, 1, 4], 
    [4, 3, 2, 4, 3, 1, 2, 1, 4, 1], 
    [3, 2, 3, 4, 2, 4, 1, 2, 4, 2], 
    [3, 4, 2, 4, 2, 4, 4, 4, 2, 2], 
    [3, 2, 4, 4, 1, 2, 3, 4, 2, 1]], 
    "Piso4": [[3, 4, 4, 3, 2, 1, 3, 4, 1, 1], 
    [4, 1, 1, 1, 4, 1, 4, 1, 1, 4], 
    [3, 1, 2, 2, 4, 4, 2, 2, 3, 4], 
    [1, 2, 4, 4, 4, 2, 2, 2, 3, 3], 
    [3, 2, 4, 4, 4, 1, 2, 3, 3, 2], 
    [1, 1, 4, 2, 3, 2, 1, 4, 3, 2], 
    [4, 3, 3, 3, 1, 4, 1, 4, 2, 4], 
    [2, 1, 2, 4, 1, 2, 3, 4, 3, 2], 
    [3, 3, 3, 4, 4, 2, 1, 2, 4, 2], 
    [4, 3, 4, 2, 3, 1, 2, 1, 3, 2]], 
    "Piso5": [[3, 3, 2, 1, 4, 3, 3, 2, 1, 4], 
    [1, 3, 1, 1, 1, 4, 1, 1, 4, 2], 
    [4, 3, 4, 1, 1, 4, 3, 1, 4, 3], 
    [1, 3, 4, 1, 3, 1, 2, 2, 2, 1], 
    [4, 3, 2, 1, 3, 4, 4, 2, 1, 1], 
    [4, 3, 2, 1, 4, 1, 2, 2, 1, 4], 
    [4, 2, 1, 2, 2, 2, 4, 1, 2, 2], 
    [3, 4, 1, 4, 2, 3, 2, 4, 2, 3], 
    [3, 2, 2, 4, 3, 3, 2, 2, 2, 1], 
    [4, 4, 2, 3, 3, 4, 4, 4, 3, 2]], 
    "Piso6": [[3, 4, 2, 1, 2, 2, 4, 4, 2, 1], 
    [4, 3, 1, 3, 4, 3, 4, 1, 3, 1], 
    [2, 3, 2, 1, 1, 4, 2, 3, 2, 1], 
    [2, 3, 1, 2, 2, 4, 2, 2, 1, 2], 
    [1, 3, 2, 1, 4, 2, 2, 2, 1, 2]]}
    with open('Tipos_Parqueaderos.json','w') as file:
        json.dump(y,file,indent=4)
    dis={"Piso1": [[4, 4, 1, 2, 2, 2, 1, 1, 1, 4], 
    [1, 4, 1, 4, 1, 3, 1, 4, 2, 4], 
    [4, 4, 3, 4, 2, 3, 4, 3, 4, 2], 
    [1, 3, 1, 4, 3, 2, 2, 4, 3, 1], 
    [4, 3, 3, 4, 3, 4, 3, 2, 4, 1], 
    [4, 2, 1, 3, 4, 2, 2, 1, 1, 2], 
    [2, 3, 3, 1, 1, 3, 3, 2, 3, 1], 
    [1, 4, 2, 2, 1, 3, 1, 1, 2, 4], 
    [2, 4, 1, 4, 2, 1, 1, 2, 1, 3], 
    [2, 3, 1, 2, 4, 4, 2, 1, 3, 2]], 
    "Piso2": [[2, 2, 2, 3, 2, 1, 2, 2, 2, 1], 
    [2, 4, 1, 2, 3, 1, 3, 4, 1, 4], 
    [2, 1, 3, 4, 4, 1, 1, 1, 1, 4], 
    [3, 4, 3, 1, 2, 1, 1, 2, 3, 3], 
    [2, 3, 1, 1, 2, 1, 2, 3, 4, 1], 
    [3, 4, 2, 3, 3, 4, 3, 2, 1, 4], 
    [3, 1, 1, 2, 1, 4, 1, 1, 1, 3], 
    [1, 3, 2, 1, 4, 4, 1, 1, 3, 4], 
    [4, 3, 3, 2, 2, 4, 4, 1, 4, 3], 
    [2, 4, 3, 3, 1, 3, 3, 1, 2, 4]], 
    "Piso3": [[3, 4, 2, 4, 3, 2, 3, 1, 4, 2], 
    [3, 3, 2, 2, 4, 3, 3, 4, 4, 2], 
    [4, 4, 3, 3, 4, 3, 3, 1, 2, 3], 
    [1, 1, 2, 2, 2, 2, 4, 3, 4, 4], 
    [4, 2, 1, 1, 1, 1, 3, 3, 3, 2], 
    [1, 4, 2, 4, 2, 1, 2, 1, 1, 4], 
    [4, 3, 2, 4, 3, 1, 2, 1, 4, 1], 
    [3, 2, 3, 4, 2, 4, 1, 2, 4, 2], 
    [3, 4, 2, 4, 2, 4, 4, 4, 2, 2], 
    [3, 2, 4, 4, 1, 2, 3, 4, 2, 1]], 
    "Piso4": [[3, 4, 4, 3, 2, 1, 3, 4, 1, 1], 
    [4, 1, 1, 1, 4, 1, 4, 1, 1, 4], 
    [3, 1, 2, 2, 4, 4, 2, 2, 3, 4], 
    [1, 2, 4, 4, 4, 2, 2, 2, 3, 3], 
    [3, 2, 4, 4, 4, 1, 2, 3, 3, 2], 
    [1, 1, 4, 2, 3, 2, 1, 4, 3, 2], 
    [4, 3, 3, 3, 1, 4, 1, 4, 2, 4], 
    [2, 1, 2, 4, 1, 2, 3, 4, 3, 2], 
    [3, 3, 3, 4, 4, 2, 1, 2, 4, 2], 
    [4, 3, 4, 2, 3, 1, 2, 1, 3, 2]], 
    "Piso5": [[3, 3, 2, 1, 4, 3, 3, 2, 1, 4], 
    [1, 3, 1, 1, 1, 4, 1, 1, 4, 2], 
    [4, 3, 4, 1, 1, 4, 3, 1, 4, 3], 
    [1, 3, 4, 1, 3, 1, 2, 2, 2, 1], 
    [4, 3, 2, 1, 3, 4, 4, 2, 1, 1], 
    [4, 3, 2, 1, 4, 1, 2, 2, 1, 4], 
    [4, 2, 1, 2, 2, 2, 4, 1, 2, 2], 
    [3, 4, 1, 4, 2, 3, 2, 4, 2, 3], 
    [3, 2, 2, 4, 3, 3, 2, 2, 2, 1], 
    [4, 4, 2, 3, 3, 4, 4, 4, 3, 2]], 
    "Piso6": [[3, 4, 2, 1, 2, 2, 4, 4, 2, 1], 
    [4, 3, 1, 3, 4, 3, 4, 1, 3, 1], 
    [2, 3, 2, 1, 1, 4, 2, 3, 2, 1], 
    [2, 3, 1, 2, 2, 4, 2, 2, 1, 2], 
    [1, 3, 2, 1, 4, 2, 2, 2, 1, 2]]}
    with open('Disponibilidad.json','w') as file:
        json.dump(dis,file,indent=4)
def arch_ingreso_salida():
    k={}
    with open('salida_parqueadero.json','w') as file:
        json.dump(k,file,indent=4)
    with open('ingreso_parqueadero.json','w') as file:
        json.dump(k,file,indent=4)

#Programa
x=0
dia=input('Ingrese la fecha de hoy: ')
reg_ingr_diar(dia)
ejecutar=0
while x!=-1:
    if (ejecutar==0):
        ejecutar=input('1.Ingresar vehículos\n2.Retirar vehículo\n3.Registro de usuarios\n4.Ver estadísticas\n5.Reiniciar archivos\n6.Salir\n')

    if(ejecutar=='1'):
        ingr(dia)
        redi=input('1.Seguir con el ingreso de vehículos\n2.Retirar vehículo\n3.Volver al menú principal\n')
        if(redi=='1'):
            ejecutar='1'
        elif(redi=='2'):
            ejecutar='2'
        else:
            ejecutar=0
    elif(ejecutar=='2'):
        placa=input('Ingrese la placa del vehículo: ')
        horas=int(input('Ingrese el número de horas: '))
        retirar_veh(dia,placa,horas)
        redi=input('1.Seguir con el retiro de vehículos\n2.Ingresar vehículo\n3.Volver al menú principal\n')
        if(redi=='1'):
            ejecutar='2'
        elif(redi=='2'):
            ejecutar='1'
        else:
            ejecutar=0
    elif(ejecutar=='3'):
        registro_usuarios()
        ejecutar=0
    elif(ejecutar=='4'):
        print('¡ADVERTENCIA! Esta función es de uso exclusivo de la Oficina de Servicios Generales de la Universidad')
        función=input('1.Soy parte de la OSGU\n2.Volver al menú principal\n')
        if(función=='1'):
            arch=input('¿A qué archivo quisiera acceder?\n1.Ocupación por usuario\n2.Ocupación por vehículo\n3.Porcentaje de ocupación\n')
            if arch=='1':
                estadística_tipo_usu()
                print('Revise sus archivos para encontrar el reporte')
                nu=input('1.Acceder a otro archivo\n2.Salir\n')
                if nu=='1':
                    ejecutar='4'
                else:
                    ejecutar=0
            elif arch=='2':
                estadística_tipo_veh()
                print('Revise sus archivos para encontrar el reporte')
                nu=input('1.Acceder a otro archivo\n2.Salir\n')
                if nu=='1':
                    ejecutar='4'
                else:
                    ejecutar=0
            elif arch=='3':
                ocupación()
                print('Revise sus archivos para encontrar el reporte')
                nu=input('1.Acceder a otro archivo\n2.Salir\n')
                if nu=='1':
                    ejecutar='4'
                else:
                    ejecutar=0

        else:
            ejecutar=0
    elif(ejecutar=='5'):
        print('¡ADVERTENCIA! Esta función es de uso exclusivo de la Oficina de Servicios Generales de la Universidad')
        función=input('1.Soy parte de la OSGU\n2.Volver al menú principal\n')
        if(función=='1'):
            reiniciar=input('1.Reiniciar (Usuarios, tipos de parqueadero,disponibilidad)\n2.Reiniciar archivos de ingreso (Se eliminará TODA la información guardada en estos archivos)\n3.Salir\n')
            if(reiniciar=='1'):
                archivos_1()
                print('Operación exitosa')
            elif(reiniciar=='2'):
                arch_ingreso_salida()
                print('Operación exitosa. Recuerde que el programa se cierra al realizar esta operación.')
                x=-1
            ejecutar=0
        else:
            ejecutar=0
    elif(ejecutar=='6'):
        x=-1
    else:
        print('Indicación inválida. Intentelo de nuevo')
        ejecutar=0