import pytest
from graphene.test import Client
from APIPuntosDeAccesoWifi.schema import schema 
from APIPuntosDeAccesoWifi.models import WifiAccesPoint

@pytest.mark.django_db
def test_puntosDeAccesoWifi_endpoint():
    # Creacion de un cliente GraphQL
    WifiAccesPoint.objects.create(id="mi id",programa="mi porgrama",fecha_instalacion="2016-02-25",latitud=129,longitud=129,colonia="Mi colonia",alcaldia="mi alcaldia")
    WifiAccesPoint.objects.create(id="mi id2",programa="mi porgrama2",fecha_instalacion="2016-02-25",latitud=129,longitud=129,colonia="Mi colonia2",alcaldia="mi alcaldia2")
    WifiAccesPoint.objects.create(id="mi id3",programa="mi porgrama3",fecha_instalacion="2016-02-25",latitud=129,longitud=129,colonia="Mi colonia3",alcaldia="mi alcaldia3")
    client = Client(schema)

    # Definicion de la consulta GraphQL
    query = '''
        query {
            puntosDeAccesoWifi(page:1,pageSize:2){
                id
                programa
                latitud
                longitud
                alcaldia
        }
        }
    '''

    # Ejecucion de la consulta
    response = client.execute(query)
    print("Response ....")
    print(response)

    # Verificar que la respuesta no contiene errores
    assert "errors" not in response

    #Obtener cantidad de resultados
    cantidad_de_resultados = len(response["data"]["puntosDeAccesoWifi"])
    print(cantidad_de_resultados)
    #Comprobar que solo se obtuvieron 2 resultados
    assert cantidad_de_resultados == 2
    
    #Comprobar que el id del primero resultado es "mi id"
    #obtener el id del primer resultado
    puntos = response["data"]["puntosDeAccesoWifi"]
    id_primer_resultado = puntos[0]["id"]
    assert "mi id" == id_primer_resultado

@pytest.mark.django_db
def test_puntoDeAccesoWifi_endpoint():
    # Creacion de un cliente GraphQL
    WifiAccesPoint.objects.create(id="mi id",programa="mi programa",fecha_instalacion="2016-02-25",latitud=129,longitud=129,colonia="Mi colonia",alcaldia="mi alcaldia")
    WifiAccesPoint.objects.create(id="mi id2",programa="mi programa2",fecha_instalacion="2016-02-25",latitud=129,longitud=129,colonia="Mi colonia2",alcaldia="mi alcaldia2")
    WifiAccesPoint.objects.create(id="mi id3",programa="mi programa3",fecha_instalacion="2016-02-25",latitud=129,longitud=129,colonia="Mi colonia3",alcaldia="mi alcaldia3")
    # Creacion de un cliente GraphQL
    client = Client(schema)

    # Definicion de la consulta GraphQL
    query = '''
        query {
            puntoDeAcceso(id:"mi id3"){
                id
                programa
        }
        }
    '''

    # Ejecucion de la consulta
    response = client.execute(query)
    print("Response ....")
    print(response)

    # Verificar que la respuesta no contiene errores
    assert "errors" not in response

    
    #Comprobar que el programa es "mi programa3"
    programa = response["data"]["puntoDeAcceso"]["programa"]
    print(programa)

    assert "mi programa3" == programa

@pytest.mark.django_db
def test_puntosdeAccesoPorColonia_endpoint():
    # Creacion de un cliente GraphQL
    #Se crean 6 registros de prueba donde 3 registros o puntos de acceso pertenecen a la misma colonia
    WifiAccesPoint.objects.create(id="mi id",programa="mi programa",fecha_instalacion="2016-02-25",latitud=129,longitud=129,colonia="Mi colonia",alcaldia="mi alcaldia")
    WifiAccesPoint.objects.create(id="mi id2",programa="mi programa2",fecha_instalacion="2016-02-25",latitud=129,longitud=129,colonia="Mi colonia2",alcaldia="mi alcaldia2")
    WifiAccesPoint.objects.create(id="mi id3",programa="mi programa3",fecha_instalacion="2016-02-25",latitud=129,longitud=129,colonia="Mi colonia3",alcaldia="mi alcaldia3")
    WifiAccesPoint.objects.create(id="mi id4",programa="mi programa",fecha_instalacion="2016-02-25",latitud=129,longitud=129,colonia="Mi colonia",alcaldia="mi alcaldia")
    WifiAccesPoint.objects.create(id="mi id5",programa="mi programa2",fecha_instalacion="2016-02-25",latitud=129,longitud=129,colonia="Mi colonia",alcaldia="mi alcaldia2")
    WifiAccesPoint.objects.create(id="mi id6",programa="mi programa3",fecha_instalacion="2016-02-25",latitud=129,longitud=129,colonia="Mi colonia3",alcaldia="mi alcaldia3")
    # Creacion de un cliente GraphQL
    client = Client(schema)

    # Definicion de la consulta GraphQL
    query = '''
        query {
            puntosdeAccesoPorColonia(colonia:"Mi colonia",page:1,pageSize:23){
                id
                colonia
        }
        }
    '''

    # Ejecucion de la consulta
    response = client.execute(query)
    print("Response ....")
    print(response)

    # Verificar que la respuesta no contiene errores
    assert "errors" not in response

    
    #Se revisa cuantos puntos de acceso hubo en la colonia Mi colonia
    cantidad_resultados = len(response["data"]["puntosdeAccesoPorColonia"])
    print(cantidad_resultados)

    #Deben de ser 3 puntos de acceso
    assert cantidad_resultados == 3



@pytest.mark.django_db
def test_puntosDeAccesoMasCercanos_endpoint():
    # Creacion de un cliente GraphQL
    #Se crean 6 registros de prueba donde se le colocaron los datos de latitud y longitud
    WifiAccesPoint.objects.create(id="mi id",programa="mi programa",fecha_instalacion="2016-02-25",latitud=19.432813,longitud=-99.116267,colonia="Mi colonia1",alcaldia="mi alcaldia")
    WifiAccesPoint.objects.create(id="mi id2",programa="mi programa2",fecha_instalacion="2016-02-25",latitud=19.430822,longitud=-99.115276,colonia="Mi colonia2",alcaldia="mi alcaldia2")
    WifiAccesPoint.objects.create(id="mi id3",programa="mi programa3",fecha_instalacion="2016-02-25",latitud=19.430822,longitud=-99.115276,colonia="Mi colonia3",alcaldia="mi alcaldia3")
    WifiAccesPoint.objects.create(id="mi id4",programa="mi programa",fecha_instalacion="2016-02-25",latitud=19.437175,longitud=-99.114399,colonia="Mi colonia4",alcaldia="mi alcaldia")
    WifiAccesPoint.objects.create(id="mi id5",programa="mi programa2",fecha_instalacion="2016-02-25",latitud=19.4384,longitud=-99.1177,colonia="Mi coloni5",alcaldia="mi alcaldia2")
    WifiAccesPoint.objects.create(id="mi id6",programa="mi programa3",fecha_instalacion="2016-02-25",latitud=19.42711,longitud=-99.1171,colonia="Mi colonia6",alcaldia="mi alcaldia3")
    # Creacion de un cliente GraphQL
    client = Client(schema)

    # Definicion de la consulta GraphQL
    query = '''
        query {
            puntosDeAccesoMasCercanos(latitud:19.42700,longitud:-99.1171,page:1,pageSize:2){
                id
                colonia
                latitud
                longitud

        }
        }
    '''

    # Ejecucion de la consulta
    response = client.execute(query)
    print("Response ....")
    print(response)

    # Verificar que la respuesta no contiene errores
    assert "errors" not in response

    
    #Se revisa cuantos puntos de acceso hubo en la colonia Mi colonia
    cantidad_resultados = len(response["data"]["puntosDeAccesoMasCercanos"])
    print(cantidad_resultados)

    #Deben de ser 3 puntos de acceso
    assert cantidad_resultados == 2

    #Revisar si el primer resultado tiene el ID "mi id6"

    id_primer_resultado = response["data"]["puntosDeAccesoMasCercanos"][0]["id"]
    print(id_primer_resultado)

    assert id_primer_resultado == "mi id6"
    