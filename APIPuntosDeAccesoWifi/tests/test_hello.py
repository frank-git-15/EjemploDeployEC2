import pytest
import json
from graphene.test import Client
from APIPuntosDeAccesoWifi.schema import schema

#pytest.mark.django_db marca la prueba para usar una base de datos de Django, 
@pytest.mark.django_db
def test_hello_endpoint():
    client = Client(schema)
    query = '''query { hello }'''
    response = client.execute(query)

    assert "Hello" in response["data"]["hello"]