#-*- coding: utf-8 -*-

def consume():
	from plugin_correios import Frete
	from gluon.storage import Storage
	if not request.vars:
		raise HTTP(500)

	## Example to test
	# diametro=0&peso=1&cep_origem=70002900&largura=20&formato=1&comprimento=20&servico=04510&cep_destino=04547000&altura=20		
	parameters = {
	    'nCdEmpresa':'' # not necessary
	    ,'sDsSenha':'' # not necessary
	    ,'sCepOrigem': request.vars.cep_origem # external
	    ,'sCepDestino': request.vars.cep_destino # external
	    ,'nVlPeso': request.vars.peso or 1 # external
	    ,'nCdFormato': request.vars.formato or 1 # 1 package, 2 envelope
	    ,'nVlComprimento': request.vars.comprimento # external
	    ,'nVlAltura': request.vars.altura # external
	    ,'nVlLargura': request.vars.largura # external
	    ,'nVlDiametro': request.vars.diametro or 0 # external
	    ,'sCdMaoPropria':'n'
	    ,'nVlValorDeclarado':'0' # not necessary
	    ,'sCdAvisoRecebimento':'n' # not necessary
	    ,'nCdServico': request.vars.servico or '04014' # SEDEX, SEDEX10
	    ,'StrRetorno':'xml' # necessary
	    ,'nIndicaCalculo':'3' # what?
	  }

	frete = Frete(**parameters)
	frete.find()
	
	return dict(frete=Storage(frete.__dict__))