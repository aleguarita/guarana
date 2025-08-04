from pathlib import Path
from datetime import date

from ..config import *
from .helpers import separador, caminho_pasta_existente

hoje = date.today().strftime("%d/%m/%Y")
texto_header =\
f"""
/*
{separador()}
ARQUIVO BASE DE {NOME}
NÃO ALTERE! ELE É GERADO AUTOMATICAMENTE E TUDO SE PERDE AO ATUALIZAR
{separador('-')}
Versão: {VERSAO}
Última alteração nesse sistema em: {hoje}
{separador()}
*/\n
"""

def criar_css_base():
    """
    Cria o arquivo SCSS base, que vai incluir todos os elementos e será importado
    para o arquivo principal
    """
    pasta_base = PASTA_ORIGEM/PASTA_CSS/'base'
    pasta_destino = caminho_pasta_existente(PASTA_CSS)
    arquivo_destino = pasta_destino/ARQUIVO_BASE
    arquivos = list(pasta_base.glob('*'))

    texto = texto_header

    for arquivo in arquivos:
        texto += arquivo.read_text()

    if not arquivo_destino.exists():
        print(f'Arquivo {COR_VERDE}{pasta_destino}/{ARQUIVO_BASE}{COR_FIM} criado')
    else:
        print(f'Arquivo {COR_VERMELHO}{pasta_destino}/{ARQUIVO_BASE}{COR_FIM} reescrito')

    arquivo_destino.write_text(texto)
    
