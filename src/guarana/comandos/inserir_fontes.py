from pathlib import Path

from ..config import *
from .helpers import caminho_pasta_existente

def inserir_fontes():
    """
    Copia as fontes de símbolo do Guaraná
    """
    PASTA_ORIGINAL = PASTA_ORIGEM/'fontes/convertido'
    PASTA_DESTINO = caminho_pasta_existente('fontes')

    if not PASTA_DESTINO:
        print(f'{COR_VERMELHO}Guaraná não foi detectado{COR_FIM}. Execute o comando {COR_AMARELO}instalar{COR_FIM}')
        return
    
    arquivos = list(PASTA_ORIGINAL.glob('*'))

    for arquivo in arquivos:
        arquivo_destino = PASTA_DESTINO/arquivo.name
        arquivo.copy(arquivo_destino)
        print(f'Arquivo {COR_AMARELO}{arquivo}{COR_FIM} escrito')
        