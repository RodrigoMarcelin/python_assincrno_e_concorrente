import multiprocessing
from math import ceil
import time
import arcpy

def export_shape(dissolve, lista):
    for item in lista:
        variavel = r"C:\Users\Rodrigo\Documents\Documentos_do_Rodrigo\cursos\Assincrono_e_concorrente\{}.shp".format(item)
        variavel_1 = r"C:\Users\Rodrigo\Documents\Documentos_do_Rodrigo\cursos\Assincrono_e_concorrente\saida\{}.shp".format(item)
        arcpy.MakeFeatureLayer_management(dissolve, variavel, f"UP = '{item}'")
        arcpy.CopyFeatures_management(variavel, variavel_1)






def lista_print(core, lista):
  
    for item in lista:
        print(f"core: {core}, exec:{item}")
        

if __name__ == "__main__":

    dissolve = r"C:\Users\Rodrigo\Downloads\SUPORTE_HEXAGON_DAVI\ups\UP.shp"
    lista = []
    with arcpy.da.SearchCursor(dissolve, ["UP"]) as cursor:
        for row in cursor:
            up = row[0]
            lista.append(up)


    qtd_cores = multiprocessing.cpu_count()
    process = []
    lista_entrada = lambda test_list, x: [test_list[n:n+ceil(len(test_list)/x)] for n in range(0, len(test_list), ceil(len(test_list)/x))]
    lista_saida = lista_entrada(lista, qtd_cores)
    
    count = 0
    for i in lista_saida:
        lista_entre = i
        count += 1
        process.append(multiprocessing.Process(target=export_shape, args=(dissolve, lista_entre,)))

    
    # pc = process[0]
    # pc.start()
    # pc.join()
    [joao.start() for joao in process]

    [joao.join() for joao in process]
