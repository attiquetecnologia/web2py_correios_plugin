#-*- coding: utf-8 -*-

"""
web2py_correios: web2py plugin for price and deadline calculation in post office webservices.
The purpose of this file is to be independent of any non-native frameworks and libraries.

web2py_correios: plugin web2py para calculo de preço e prazo usando o webservice dos correios.
O objetivo deste arquivo em módules é ser independente de bibliotecas não nativas do python.
"""

__author__ = 'Rodrigo Attique'
__email__ = 'attiquetecnologia@gmail.com'
__copyright__ = 'Copyright(c) 2019-2020 Rodrigo Attique '
__license__ = 'MIT'
__version__ = '0.1.3'
# possible options: Prototype, Development, Production
__status__ = 'Development'

import requests
import xml.etree.ElementTree as ET

class Frete:
  """docstring for Frete
    This class used by consult price-and-deadlines
    Classe responsável por consultar preço e prazo
  """
  # http://ws.correios.com.br
  # The url above return de following xml structure
  # Esta url retorna a seguinte estrutura xml
  """
  <Servicos>
    <cServico>
      <Codigo>04510</Codigo>
      <Valor>27,80</Valor>
      <PrazoEntrega>6</PrazoEntrega>
      <ValorSemAdicionais>27,80</ValorSemAdicionais>
      <ValorMaoPropria>0,00</ValorMaoPropria>
      <ValorAvisoRecebimento>0,00</ValorAvisoRecebimento>
      <ValorValorDeclarado>0,00</ValorValorDeclarado>
      <EntregaDomiciliar>S</EntregaDomiciliar>
      <EntregaSabado>N</EntregaSabado>
      <obsFim/>
      <Erro>0</Erro>
      <MsgErro/>
    </cServico>
  </Servicos>"""

  endpoint = 'http://ws.correios.com.br'
  resource = '/calculador/CalcPrecoPrazo.aspx?wsdl&'
  parameters = ''

  def __init__(self, **parameters):
    """
      **parameters : dictionary of url parameters specified in the post office manual price-and-deadlines http://www.correios.com.br/a-a-z/pdf/calculador-remoto-de-precos-e-prazos/manual-de-implementacao-do-calculo-remoto-de-precos-e-prazos
      **parameters : dicionário contendo as variáveis para post em url
    """

    for k, v in parameters.items():
      # The parameters are compiled to url parameter format
      self.parameters = self.parameters + "%s=%s&" % (k,v)
    
  def find(self):
    """ Consume webservice url and set values ​​in class dynamic attributes """
    # need try??
    
    url = "".join([self.endpoint, self.resource, self.parameters])
    with open('log.txt', 'w') as file: file.write(url)
    r = requests.get(url, headers = {'content-type': 'application/xml; charset=utf-8'})
    r.encoding='utf-8'
    
    root = ET.fromstring(r.content)

    for element in root.iter('cServico'):
      for p in element:
        # print(p) # test
        self.__dict__[p.tag] = p.text

if __name__=='__main__':
  # The below code shall be used in controller
  parameters = {
    'nCdEmpresa':'' # not necessary
      ,'sDsSenha':'' # not necessary
      ,'sCepOrigem':'14780028' # external
      ,'sCepDestino':'13010040' # external
      ,'nVlPeso':'1' # external
      ,'nCdFormato':'1' # 1 package, 2 envelope
      ,'nVlComprimento':'20' # external
      ,'nVlAltura':'20' # external
      ,'nVlLargura':'20' # external
      ,'nVlDiametro':'0' # external
      ,'sCdMaoPropria':'n'
      ,'nVlValorDeclarado':'0' # not necessary
      ,'sCdAvisoRecebimento':'n' # not necessary
      ,'nCdServico':'04510' # SEDEX, SEDEX10
      ,'StrRetorno':'xml' # necessary
      ,'nIndicaCalculo':'3' # what?
  }

  frete = Frete(**parameters)
  frete.find()
  if frete.MsgErro:
    print(frete.MsgErro)
  else:
    print(frete.__dict__)