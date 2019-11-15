#-*- coding: utf-8 -*-

def consume():
	from plugin_correios import Frete

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
	    ,'nCdServico':'04014' # SEDEX, SEDEX10
	    ,'StrRetorno':'xml' # necessary
	    ,'nIndicaCalculo':'3' # what?
	  }

	frete = Frete(**parameters)
	frete.find()
	from gluon.storage import Storage
	return dict(frete=Storage(frete.__dict__))