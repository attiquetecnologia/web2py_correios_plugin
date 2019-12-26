#-*- coding: utf-8 -*-

# Outra objservação o usuário precisa selecionar no carrinho a forma de frete que deseja, se
# retirar na loja ou via correios.
# Ele deve ter a flexibilidade de selecionar formas de entrega diferentes para o mesmo pedido?
# Ou deve fazer isto em pedidos diferentes.

def index():
	"""
	 Use:
	 LOAD('plugin_correios','index', vars=dict(cep_origem=response.company_cep, peso=product.pkg_weight/1000, comprimento=product.pkg_length, altura=product.pkg_height, largura=product.pkg_height, frete_gratis=product.pickup_at_store, prazo_frete_gratis=product.deadline_withdrawn))
	"""
	# del session.plugin_correios
	from gluon.storage import Storage
	# Garante que os dados do cep sejam consultados apenas uma unica vez
	if not session.plugin_correios:
		session.plugin_correios = Storage()
		session.plugin_correios.frete = Storage()
		session.plugin_correios.frete.sCepDestino = ''
		session.plugin_correios.frete.Erro=0
	elif not session.plugin_correios.frete:
		session.plugin_correios.frete = Storage()
		session.plugin_correios.frete.sCepDestino = ''
		session.plugin_correios.frete.Erro=0
	
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

	# 1 - Precisa comparar os dados da sessão com os do cep
	frete = session.plugin_correios.frete
	v = request.vars
	if v.cep != frete.sCepDestino:
		# refaz o calculo e coloca na sessão
		frete = Frete(**parameters)
		frete.find()
		session.plugin_correios.frete = Storage(**frete.__dict__)
	# 2 - Os as variáveis de peso e altura podem ter mudado, outro produto
	elif v.peso != frete.nVlPeso or v.altura != frete.nVlAltura or v.largura != frete.nVlLargura:
		# refaz o calculo e coloca na sessão
		frete = Frete(**parameters)
		frete.find()
		session.plugin_correios.frete = Storage(**frete.__dict__)
	elif v.cep == '':
		session.plugin_correios.frete = Storage(**{'sCepDestino':'', 'Erro': 0})
		
	return dict()