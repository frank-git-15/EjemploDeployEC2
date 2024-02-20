from django.urls import path
from graphene_django.views import GraphQLView
from .schema import schema


urlpatterns = [
    #Este es el endpoint que usaremos ipaddress:puerto/graphql
    #Con esto se abrira una vista donde podremos hacer la consultas
    #Sí es local host se verira asi la ruta http://127.0.0.1:8000/graphql
    path("graphql",GraphQLView.as_view(graphiql=True, schema=schema))
]
