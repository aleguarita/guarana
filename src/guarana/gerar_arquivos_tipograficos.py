import sys
import tempfile
from pathlib import Path

from fontTools.ttLib import TTFont
from fontTools import subset as ft_subset

from guarana.config import ICONES, PASTA_ORIGEM
from guarana.doc import atualizar_doc_base

PASTA_FONTE_BASE = PASTA_ORIGEM / "fontes/base"
PASTA_FONTE_CONVERTIDO = PASTA_ORIGEM / "fontes/convertido"
CODEPOINTS = PASTA_FONTE_BASE / "MaterialSymbolsOutlined[FILL,GRAD,opsz,wght].codepoints"

FONTES = [
    "MaterialSymbolsRounded[FILL,GRAD,opsz,wght].ttf",
    "MaterialSymbolsSharp[FILL,GRAD,opsz,wght].ttf",
]


def carregar_codepoints(caminho: Path) -> dict[str, str]:
    """Lê o arquivo .codepoints e retorna {nome_ícone: hex_codepoint}."""
    codepoints = {}
    with caminho.open("r", encoding="utf-8") as f:
        for linha in f:
            linha = linha.strip()
            if not linha:
                continue
            nome, codigo = linha.split()
            codepoints[nome] = codigo
    return codepoints


def resolver_codepoints(icones: set, codepoints: dict[str, str]) -> dict[str, str]:
    """Cruza os ícones desejados com o mapa de codepoints. Aborta se algum não for encontrado."""
    nao_encontrados = icones - codepoints.keys()
    if nao_encontrados:
        print("ERRO: os seguintes ícones não foram encontrados no arquivo .codepoints:")
        for nome in sorted(nao_encontrados):
            print(f"  - {nome}")
        sys.exit(1)
    return {nome: codepoints[nome] for nome in icones}


def filtrar_gsub(font: TTFont, icones_alvo: set[str]) -> set[str]:
    """
    Reescreve a tabela GSUB mantendo APENAS as ligatures que resultam
    em um dos ícones desejados. Retorna o conjunto de glifos componentes
    necessários para essas ligatures.
    """
    if "GSUB" not in font:
        return set()

    gsub = font["GSUB"].table
    componentes = set()

    for lookup in gsub.LookupList.Lookup:
        for sub in lookup.SubTable:
            # Lookup type 7 = Extension; o payload real está em ExtSubTable
            tabela = getattr(sub, "ExtSubTable", sub)
            if not hasattr(tabela, "ligatures"):
                continue

            novas_ligatures: dict[str, list] = {}
            for primeiro_glifo, lista_lig in tabela.ligatures.items():
                mantidas = [
                    lig for lig in lista_lig if lig.LigGlyph in icones_alvo
                ]
                if mantidas:
                    novas_ligatures[primeiro_glifo] = mantidas
                    componentes.add(primeiro_glifo)
                    for lig in mantidas:
                        componentes.update(lig.Component)

            tabela.ligatures = novas_ligatures

    return componentes


def subsetar_fonte(entrada: Path, saida: Path, icones: set[str], mapa_codepoints: dict[str, str]) -> None:
    """
    Gera um .woff2 subsetado com:
    - Os glifos PUA dos ícones desejados
    - Os glifos latinos usados nas ligatures (apenas os dessas ligatures)
    """
    print(f"  Processando: {entrada.name}")

    font = TTFont(str(entrada))

    # 1. Filtrar a GSUB mantendo só as ligatures dos nossos ícones
    glifos_componentes = filtrar_gsub(font, icones)

    # 2. Salvar o TTF com GSUB filtrada em arquivo temporário
    with tempfile.NamedTemporaryFile(suffix=".ttf", delete=False) as tmp:
        caminho_tmp = Path(tmp.name)
    font.save(str(caminho_tmp))

    # 3. Montar lista de unicodes PUA + glifos componentes para o pyftsubset
    unicodes_pua = [f"U+{cp.upper()}" for cp in mapa_codepoints.values()]
    nomes_glifos = sorted(icones | glifos_componentes)

    # 4. Subsetar com fonttools via API Python
    options = ft_subset.Options()
    options.set(
        flavor="woff2",
        layout_features=["*"],  # preservar todas as features (inclui rlig)
        desubroutinize=True,
    )
    options.glyph_names = True

    with ft_subset.load_font(str(caminho_tmp), options) as fonte_sub:
        subsetter = ft_subset.Subsetter(options)
        subsetter.populate(
            unicodes=[int(u[2:], 16) for u in unicodes_pua],
            glyphs=nomes_glifos,
        )
        subsetter.subset(fonte_sub)
        ft_subset.save_font(fonte_sub, str(saida), options)

    caminho_tmp.unlink()
    tamanho_kb = saida.stat().st_size / 1024
    print(f"  -> {saida.name} ({tamanho_kb:.1f} KB)")


def main() -> None:
    # Validações de ambiente
    if not CODEPOINTS.exists():
        print(f"ERRO: arquivo .codepoints não encontrado em:\n  {CODEPOINTS}")
        sys.exit(1)

    ausentes = [f for f in FONTES if not (PASTA_FONTE_BASE / f).exists()]
    if ausentes:
        print("ERRO: fontes base não encontradas em", PASTA_FONTE_BASE)
        for f in ausentes:
            print(f"  - {f}")
        sys.exit(1)

    PASTA_FONTE_CONVERTIDO.mkdir(parents=True, exist_ok=True)
    # Limpar pasta de destino antes de gerar
    if PASTA_FONTE_CONVERTIDO.exists():
        for arquivo in PASTA_FONTE_CONVERTIDO.iterdir():
            if arquivo.is_file():
                arquivo.unlink()

    # Resolver codepoints
    print(f"Carregando codepoints de {CODEPOINTS.name}...")
    todos_codepoints = carregar_codepoints(CODEPOINTS)

    print(f"Resolvendo {len(ICONES)} ícones...")
    mapa = resolver_codepoints(ICONES, todos_codepoints)
    for nome, cp in sorted(mapa.items()):
        print(f"  {nome}: U+{cp.upper()}")

    # Gerar as três fontes
    print("\nGerando fontes subsetadas...")
    for nome_fonte in FONTES:
        entrada = PASTA_FONTE_BASE / nome_fonte
        nome = entrada.stem
        nome = nome.lower().replace('materialsymbols', 'material_symbols_')
        nome = nome.replace("[FILL,GRAD,opsz,wght]".lower(), "_[FILL,GRAD,opsz,wght]")
        saida = PASTA_FONTE_CONVERTIDO / (nome + ".woff2")
        subsetar_fonte(entrada, saida, ICONES, mapa)

    print(
        f"\nConcluído. {len(FONTES)} fontes geradas em:\n  {PASTA_FONTE_CONVERTIDO}")


if __name__ == "__main__":
    main()
    atualizar_doc_base.main()