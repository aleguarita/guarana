from ..config import *
from .helpers import caminho_pasta_existente
from .js import gerar_js
from .snippets import gerar_snippets
from .macros_django import gerar_macros
from .criar_css import criar_base_css, criar_estilo_css, preencher_pasta_utils
from .inserir_fontes import inserir_fontes


def atualizar(resetar:bool=False):
    pasta_static = caminho_pasta_existente('static')
    if not pasta_static:
        print(f'{COR_VERMELHO}Guaraná não foi detectado{COR_FIM}. Execute o comando {COR_AMARELO}instalar{COR_FIM}')
        return
    
    criar_base_css()
    criar_estilo_css(resetar)
    preencher_pasta_utils(resetar)
    inserir_fontes()
    gerar_js(resetar)
    gerar_snippets()
    gerar_macros()