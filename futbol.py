
def res(matriz,num):
    contvic=0                    
    contderr=0                    
    contemp=0  
    conpuntos=0                  
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if i!=j: 
                if i==num:
                    if matriz[i][j]<matriz[j][i]:
                        
                        contderr+=1
                    elif matriz[i][j]>matriz[j][i]:
                        contvic+=1  
                        conpuntos+=3
                    else:
                        conpuntos+=1
                        contemp+=1
    listaestadisticas=[contvic,contderr,contemp,conpuntos]
    return listaestadisticas
                    
matriz=[[0,4,2,1],
        [5,0,3,2],
        [0,2,0,1],
        [1,0,2,0]]

estadisticasequipo1=res(matriz,0)
print(f"Equipo 1: Victorias={estadisticasequipo1[0]}, Derrotas={estadisticasequipo1[1]}, Empates={estadisticasequipo1[2]}, puntosTotales= {estadisticasequipo1[3]}")


estadisticasequipo2=res(matriz,1)
print(f"Equipo 2: Victorias={estadisticasequipo2[0]}, Derrotas={estadisticasequipo2[1]}, Empates={estadisticasequipo2[2]},  puntosTotales= {estadisticasequipo2[3]}")


estadisticasequipo3=res(matriz,2)
print(f"Equipo 3: Victorias={estadisticasequipo3[0]}, Derrotas={estadisticasequipo3[1]}, Empates={estadisticasequipo3[2]}, puntosTotales= {estadisticasequipo3[3]}")


estadisticasequipo4=res(matriz,3)
print(f"Equipo 4: Victorias={estadisticasequipo4[0]}, Derrotas={estadisticasequipo4[1]}, Empates={estadisticasequipo4[2]}, puntosTotales= {estadisticasequipo4[3]}")