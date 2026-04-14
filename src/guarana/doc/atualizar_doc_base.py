from pathlib import Path
from datetime import date
import re

CAMADAS = 'doc_gua, view, prism';

#region PASTAS E ARQUIVOS
pasta_atual = Path(__file__).parent
pasta_destino = pasta_atual/'static/css'
pasta_origem = pasta_atual.parent/'origem/css'
pasta_base = pasta_origem/'base'
pasta_utils = pasta_origem/'utils'

arquivo_destino = pasta_destino/'guarana.css'
arquivos_base = sorted(list(pasta_base.glob('*')))
arquivos_utils = list(pasta_utils.glob('*'))
# endregion


# TEXTO A SER USADO
texto = f'/*{date.today().strftime("%d/%m/%Y")}*/\n'

# TEXTO DO ESTILO.CSS
regex_layers = r'(\s*@layer\s+.*?)(\s*);'
estilo_original = pasta_origem/'estilo.css'

for arquivo in arquivos_base:
    texto += f'\n{arquivo.read_text('utf-8')}\n'

for arquivo in arquivos_utils:
    texto += f'\n{arquivo.read_text('utf-8')}\n'

    
texto += re.sub(regex_layers, r'\1' + f', {CAMADAS}' + r';', estilo_original.read_text())
texto = texto.replace('/* IMPORTS */\n@import url(ARQUIVO_BASE);\n', '')

arquivo_destino.write_text(texto, 'utf-8')

# COPIA JS
arquivo_js_destino = pasta_atual/'static/js/guarana.js'
arquivo_js_origem = pasta_atual.parent/'origem/js/guarana.js'

arquivo_js_destino.write_text(arquivo_js_origem.read_text('utf-8'), 'utf-8')

# GERA ARQUIVO FINAL DE MACROS
# mescla _macros_base.html com as macros de usuário do guaraná
arquivo_macro_destino = pasta_atual/'templates/partials/todas_macros.html'
arquivo_macro_base = pasta_atual/'templates/_macros_base.html'
arquivo_macro_guarana = pasta_atual.parent/'origem/macros/guarana.html'

texto_macros = "{#\nARQUIVO AUTOMÁTICO, NÃO ESCREVA\n"
texto_macros += "=".ljust(80, '=')
texto_macros += "\n#}\n\n"
texto_macros += arquivo_macro_base.read_text('utf-8')
texto_macros += arquivo_macro_guarana.read_text('utf-8')

arquivo_macro_destino.write_text(texto_macros, 'utf-8')
