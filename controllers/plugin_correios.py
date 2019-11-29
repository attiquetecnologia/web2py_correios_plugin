#-*- coding: utf-8 -*-

# NOTE: é preciso disponibilizar o cep de destino na sessão para que seja possível consultar novamente
# sem a necessidade usar a interface.???

# Outra objservação o usuário precisa selecionar no carrinho a forma de frete que deseja, se
# retirar na loja ou via correios.
# Ele deve ter a flexibilidade de selecionar formas de entrega diferentes para o mesmo pedido?
# Ou deve fazer isto em pedidos diferentes.

def index():
	"""
	 Use:
	 LOAD('plugin_correios','index', vars=dict(cep_origem=response.company_cep, peso=product.pkg_weight/1000, comprimento=product.pkg_length, altura=product.pkg_height, largura=product.pkg_height, frete_gratis=product.pickup_at_store, prazo_frete_gratis=product.deadline_withdrawn))
	"""
	
	return dict()

def preco_prazo():
	"""
	Encontra o preço e o prazo de entrega na api dos correios
	"""

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
	    ,'sCepDestino': request.vars.cep # external
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