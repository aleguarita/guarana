from pathlib import Path
import subprocess

from guarana.config import *

PASTA_FONTE_BASE = PASTA_ORIGEM / "fontes/base"
PASTA_FONTE_CONVERTIDO = PASTA_ORIGEM / "fontes/convertido"
CODEPOINTS = PASTA_FONTE_BASE / "MaterialSymbolsOutlined[FILL,GRAD,opsz,wght].codepoints"

def buscar_unicodes(lista_icones: set, arquivo_codepoints: Path):
    if not arquivo_codepoints.exists():
        raise FileNotFoundError(f"arquivo .codepoints não encontrado em {arquivo_codepoints.resolve()}")

    codepoints = arquivo_codepoints.read_text(encoding='utf-8').splitlines()
    codepoints = {i[0]: f'U+{i[1].upper()}' for i in [i.split() for i in codepoints]}

    return [codepoints[i] for i in lista_icones]


def gerar_subset(unicodes: list, nome_fonte: str):
    fonte_origem = PASTA_FONTE_BASE / nome_fonte
    nome_destino = nome_fonte.lower().replace('materialsymbols', 'material_symbols_')
    nome_destino = nome_destino.replace('[fill,grad,opsz,wght]', '_subset')

    if not unicodes:
        print("Nenhum unicode encontrado")
        return

    if not fonte_origem.exists():
        raise FileNotFoundError(f"Fonte original não encontrada em {fonte_origem.resolve()}")
    
    fonte_destino = PASTA_FONTE_CONVERTIDO / nome_fonte.replace('[FILL,GRAD,opsz,wght]', '.subset')

    comando = [
        'pyftsubset',
        fonte_origem,
        f'--unicodes={",".join(unicodes)}',
        '--flavor=woff2',
        f'--output-file={PASTA_FONTE_CONVERTIDO / nome_destino}'
    ]

    print(f"Gerando subsets com {len(unicodes)} ícones...")

    resultado = subprocess.run(comando, capture_output=True, text=True)

    if resultado.returncode == 0:
        print(f"{COR_VERDE}Sucesso!{COR_FIM} Fonte otimizada gerada: {COR_AMARELO}{fonte_destino}{COR_FIM}")
    else:
        print(f"{COR_VERMELHO}Erro ao executar o pyftsubset: {COR_FIM}")
        print(resultado.stderr)


if __name__ == "__main__":
    try:
        lista_unicodes = buscar_unicodes(ICONES, CODEPOINTS)
    
        arquivos = [f.name for f in PASTA_FONTE_BASE.iterdir() if f.name.endswith("woff2")]
        for arquivo in arquivos:
            gerar_subset(lista_unicodes, arquivo)
    
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

    