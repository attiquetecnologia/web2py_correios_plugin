# web2py_correios_plugin
This project is a simple price and term calculator plugin in the brasilian post office webservices.
This plugin will be use intentional by brasilians but can be adapted for others post officers tha use REST or SOAP

# Usage
LOAD('plugin_correios','index', vars=dict(cep_origem=response.company_cep, peso=product.pkg_weight/1000, comprimento=product.pkg_length, altura=product.pkg_height, largura=product.pkg_height, frete_gratis=product.pickup_at_store, prazo_frete_gratis=product.deadline_withdrawn))

# vars
cep_origem : 00000-000 or 00000000
peso : Kg If weight in grains divide by 1000
comprimento : centimeters If length in milimiters divide by 100
altura: centimeters If height in milimiters divide by 100
prazo_frete_gratis : if pick up at store product so require a deadline for the customer to pick up at the store
frete_gratis : boolean, customer can be pikcup at the store
