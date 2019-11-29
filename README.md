# web2py_correios_plugin
This project is a simple price and term calculator plugin in the brasilian post office webservices.
This plugin will be use intentional by brasilians but can be adapted for others post officers tha use REST or SOAP

Este projeto é um plug-in simples de calculadora de preço e prazo nos webservices dos correios brasileiros.
Este plugin será usado intencionalmente por brasileiros, mas pode ser adaptado para outros agentes do correio que usam REST ou SOAP

# Install
To install just download the latest release from this site to install the plugin via web2py admin or download and copy the files manually.

Para instalar basta baixar o ultimo release neste site para instalar o plugin via admin do web2py ou baixar e copiar os arquivos manualmente.

# Usage
LOAD('plugin_correios','index', vars=dict(cep_origem=response.company_cep, peso=product.pkg_weight/1000, comprimento=product.pkg_length, altura=product.pkg_height, largura=product.pkg_height, frete_gratis=product.pickup_at_store, prazo_frete_gratis=product.deadline_withdrawn))

# vars
cep_origem : 00000-000 or 00000000
peso : Kg If weight in grains divide by 1000
comprimento : centimeters If length in milimiters divide by 100
altura: centimeters If height in milimiters divide by 100
prazo_frete_gratis : if pick up at store product so require a deadline for the customer to pick up at the store
frete_gratis : boolean, customer can be pikcup at the store

cep_origem: 00000-000 ou 00000000
peso: Kg Se o peso dos grãos se dividir por 1000
comprimento: centímetros Se o comprimento em milimitros se dividir por 100
altura: centímetros Se a altura em milimitros se dividir por 100
prazo_frete_gratis: se retirado na loja, exija um prazo para que o cliente a retire na loja
frete_gratis: booleano, cliente pode ser pikcup na loja