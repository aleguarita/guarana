import re
from pathlib import Path
from datetime import date

from ..config import *
from .helpers import separador, caminho_pasta_existente

hoje = date.today().strftime("%d/%m/%Y")

# region HEADERS
texto_base_header =\
f"""/*
{separador()}
ARQUIVO BASE DE {NOME}
NÃO ALTERE! ELE É GERADO AUTOMATICAMENTE E TUDO SE PERDE AO ATUALIZAR
FAÇA ALTERAÇÕES NO ARQUIVO estilo.css
{separador('-')}
Versão: {VERSAO}
Última alteração nesse sistema em: {hoje}
{separador()}
*/\n
"""

texto_estilo_header =\
f"""/*
{separador()}
Arquivo principal do sistema utilizando {NOME}
Se for o usar o estilo-min.css, altere tudo aqui e execute o comando:
python -m {NOME.lower()} min
Se estiver trabalhando com Flask o arquivo rodar.py já inclui o comando acima
{separador('-')}
Criado nesse sistema em: {hoje}
Versão do {NOME} neste arquivo: {VERSAO}
{separador()}
*/
"""

texto_arquivo_fonte =\
f"""/*
{separador()}
Arquivo de ícones Material com base em https://fonts.google.com/icons.
Estilo -ESTILO-
Caso deseje esse estilo, altere o arquivo estilo.css, no import indicado.
{separador('-')}
Veja esses arquivos com o comando:
python -m {PASTA_PROJETO} rodar
{separador('-')}
Criado nesse sistema em: {hoje}
Versão do {NOME} neste arquivo: {VERSAO}
{separador()}
*/
"""
# endregion


def criar_base_css():
    """
    Cria o arquivo CSS base, que vai incluir todos os elementos e será importado
    para o arquivo principal
    """
    pasta_base = PASTA_ORIGEM/PASTA_CSS/'base'
    pasta_destino = caminho_pasta_existente(PASTA_CSS)

    if not pasta_destino:
        print(f'{COR_VERMELHO}Guaraná não foi detectado{COR_FIM}. Execute o comando {COR_AMARELO}instalar{COR_FIM}')
        return

    arquivo_destino = pasta_destino/ARQUIVO_BASE
    arquivos = sorted(pasta_base.glob(
        '*'), key=lambda f: (0 if f.name.startswith('_') else 1, f.name))

    texto = texto_base_header

    for arquivo in arquivos:
        texto += arquivo.read_text().strip() + '\n'

    if not arquivo_destino.exists():
        print(f'Arquivo {COR_VERDE}{pasta_destino}/{ARQUIVO_BASE}{COR_FIM} criado')
    else:
        print(f'Arquivo {COR_AMARELO}{pasta_destino}/{ARQUIVO_BASE}{COR_FIM} reescrito')

    texto += criar_import_utils_css()
    arquivo_destino.write_text(texto)


def criar_arquivos_fontes():
    """
    CRIA OS TRÊS ARQUIVOS DE SÍMBOLO
    """
    pasta_destino = caminho_pasta_existente(PASTA_CSS)
    estilos = {'rounded', 'sharp'}

    texto_css = """@layer reset {
    @font-face {
        font-family: 'Icones';
        font-style: normal;
        font-weight: 100 400 700;
        src: url(LOCALIZACAO) format('woff2');
    }
}
"""


    for estilo in estilos:
        arquivo_destino = pasta_destino/f'_ico_{estilo}.css'
        arquivo_fonte = f"{PASTA_PROJETO}/fontes/material_symbols_{estilo}_[FILL,GRAD,opsz,wght].woff2"

        texto = texto_arquivo_fonte.replace('-ESTILO-', estilo)
        texto += texto_css.replace('LOCALIZACAO', f'"{arquivo_fonte}"')

        arquivo_destino.write_text(texto, encoding='utf-8')


def preencher_pasta_utils(resetar:bool=False):
    origem = PASTA_ORIGEM/'css/utils'
    destino = caminho_pasta_existente(PASTA_PROJETO)

    if not destino:
        print(f'{COR_VERMELHO}Guaraná não foi detectado{COR_FIM}. Execute o comando {COR_AMARELO}instalar{COR_FIM}')
        return

    arquivos = list(origem.glob('*'))
    for arquivo in arquivos:
        arquivo_destino = destino/arquivo.name
        
        if arquivo_destino.exists() and not resetar:
            print(f'O {COR_VERMELHO}{arquivo}{COR_FIM} já existe e não foi reescrito')
            continue

        texto_data = f'\n{separador('-')}\n'
        texto_data += f'Versão: {VERSAO}.\nArquivo criado em: {hoje}\n'
        texto_data += separador()

        texto = arquivo.read_text()
        texto = texto.replace('/*\n', f'/*\n{separador()}\n', 1)
        texto = texto.replace('\n*/', f'{texto_data}\n*/', 1)

        arquivo_destino.write_text(texto, encoding='utf-8')

        if arquivo_destino.exists():
            print(f'Arquivo {COR_VERMELHO}{arquivo}{COR_FIM} reescrito')
        else:
            print(f'Arquivo {COR_AMARELO}{arquivo}{COR_FIM} criado')


def criar_import_utils_css():
    texto =  '/*\n'
    texto += separador()
    texto += '\nIMPORTS\n'
    texto += separador()
    texto += '\n*/\n'

    arquivos = list(caminho_pasta_existente(PASTA_PROJETO).glob('*.css'))
    for arquivo in arquivos:
        texto += f'@import url({PASTA_PROJETO}/{arquivo.name});\n'

    return texto


def criar_estilo_css(resetar:bool=False):
    """
    Cria o arquivo CSS estilo.css para o usuário trabalhar
    """
    arquivo_original = PASTA_ORIGEM/PASTA_CSS/'estilo.css'
    pasta_destino = caminho_pasta_existente(PASTA_CSS)
    arquivo_destino = pasta_destino/'estilo.css'

    texto = texto_estilo_header
    texto += arquivo_original.read_text()
    texto = texto.replace('ARQUIVO_BASE', ARQUIVO_BASE)
    texto = texto.replace('ARQUIVO_FONTE', ARQUIVO_BASE_FONTE)

    if not arquivo_destino.exists():
        print(
            f'Arquivo {COR_VERDE}{pasta_destino}/estilo.css{COR_FIM} criado')
    elif resetar:
        print(
            f'Arquivo {COR_AMARELO}{pasta_destino}/estilo.css{COR_FIM} reescrito')
    else:
        criar_estilo_css_min()
        return


    arquivo_destino.write_text(texto, encoding='utf-8')
    criar_estilo_css_min()


def criar_estilo_css_min():
    pasta_destino = caminho_pasta_existente(PASTA_CSS)
    arquivo_destino = pasta_destino/'estilo-min.css'

    header = f'/*{NOME}:{hoje}*/'
    texto = Path(pasta_destino/'estilo.css').read_text()

    while '@import' in texto:
        texto = substituir_imports(texto)

    if arquivo_destino.exists():
        print(f'Atualizado {COR_AMARELO}estilo-min.css{COR_FIM}')
    else:
        print(f'Gerando {COR_AMARELO}estilo-min.css{COR_FIM}')

    arquivo_destino.write_text(header+minificar_css(texto), encoding='utf-8')


def substituir_imports(css:str):
    padrao = r'@import\s+url\(([^)]+)\);'
    matches = re.findall(padrao, css)
    pasta_destino = caminho_pasta_existente(PASTA_CSS)

    for caminho in matches:
        try:
            arquivo = pasta_destino/caminho.strip()
            conteudo = arquivo.read_text()
            css = re.sub(
                rf'@import\s+url\({re.escape(caminho)}\);',
                conteudo, 
                css)
        except FileNotFoundError:
            print(f"Arquivo '{caminho}' não encontrado.")
        except Exception as e:
            print(f"Erro ao ler '{caminho}': {e}")

    return css


def minificar_css(css:str):
    css_sem_comentarios = re.sub(r'/\*.*?\*/', '', css, flags=re.DOTALL)
    
    # Remove quebras de linha, tabulações e espaços extras
    css_minificado = re.sub(r'\s+', ' ', css_sem_comentarios)

    # Remove espaços ao redor de símbolos comuns
    css_minificado = re.sub(r'\s*([{};:,])\s*', r'\1', css_minificado)
    
    return css_minificado.strip()
