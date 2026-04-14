from pathlib import Path

from ..config import *
from .helpers import caminho_pasta_existente

def gerar_macros():
    origem = PASTA_ORIGEM/PASTA_MACRO/'guarana.html'
    destino = caminho_pasta_existente(PASTA_MACRO)/'guarana.html'

    if not caminho_pasta_existente(PASTA_MACRO).exists():
        return
    
    texto_origem = origem.read_text('utf-8')
    destino.write_text(texto_origem, encoding='utf-8')
