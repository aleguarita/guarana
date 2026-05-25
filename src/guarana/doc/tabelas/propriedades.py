from ...config import *

propriedades_css = [
    {
        'nome': '--cor-erro',
        'tipo': 'cor',
        'heranca': 'não',
        'uso': ['Variável de cor vermelha para indicar erros ou urgência.', '`--cor-txt: var(--cor-erro)`'],
        'categoria': 'fechada',
        'atualizada': '0.1.0'
    },
    {
        "nome": "--cor-ok",
        "tipo": "cor",
        "heranca": "não",
        "uso": ["Variável de cor verde para indicar sucesso.", '`--cor-bg: var(--cor-ok)`'],
        'categoria': 'fechada',
        'atualizada': '0.1.0'
    },
    {
        "nome": "--cor-alerta",
        "tipo": "cor",
        "heranca": "não",
        "uso": ["Variável de cor amarela para indicar alerta, aviso.", '`--cor-txt: var(--cor-alerta)`'],
        'categoria': 'fechada',
        'atualizada': '0.1.0'
    },
    {
        "nome": "--sans",
        "tipo": "texto separado por vírgulas",
        "heranca": "não",
        "uso": ["Valor padrão para fontes sem serifa. Use como completemento, da fonte que for usar, se for personalizar.", '`--fonte: var(--sans)`'],
        'categoria': 'fechada',
        'atualizada': '0.1.0'
    },
    {
        "nome": "--serif",
        "tipo": "Texto separado por vírgulas",
        "heranca": "não",
        "uso": ["Valor padrão para fontes serifadas. Use como completemento, da fonte que for usar, se for personalizar.", '`--fonte: var(--serif)`'],
        'categoria': 'fechada',
        'atualizada': '0.1.0'
    },
    {
        "nome": "--cor-1",
        "tipo": "cor",
        "heranca": "não",
        "uso": ["Variável de paleta de cores, a cor principal.", '`--cor-txt: var(--cor-1)`'],
        'categoria': 'aberta',
        'atualizada': '0.1.0'
    },
    {
        "nome": "--cor-2",
        "tipo": "cor",
        "heranca": "não",
        "uso": ["Variável de paleta de cores, a cor secundária.", '`--cor-txt: var(--cor-2)`'],
        'categoria': 'aberta',
        'atualizada': '0.1.0'
    },
    {
        "nome": "--cor-3",
        "tipo": "cor",
        "heranca": "não",
        "uso": ["Variável de paleta de cores, a cor terciária.", '`--cor-txt: var(--cor-3)`'],
        'categoria': 'aberta',
        'atualizada': '0.1.0'
    },
    {
        "nome": "--transicao",
        "tipo": "valores separados por espaço",
        "heranca": "sim",
        "uso": [f"Variável para a transição padrão, sem indicar qual a nome afetada. Diversos elementos em utilitários fazem uso dessa variável por padrão, de forma que ao alterar o valor inicial, vai alterar diversos elementos do {NOME}", '`transition: var(--transicao)`'],
        'categoria': 'aberta',
        'atualizada': '0.1.0'
    },
    {
        "nome": "--cor-bg",
        "tipo": "cor",
        "heranca": 'sim',
        "uso": ["Variável usada em diversos elementos e no body (no reset) que já contam com `background-color` para essa cor, bastando alterar essa variável.", '`--cor-bg: red`'],
        'categoria': 'variável',
        'atualizada': '0.1.0'
    },
    {
        "nome": "--cor-txt",
        "tipo": "cor",
        "heranca": 'sim',
        "uso": ["Variável usada em diversos elementos e no body (no reset) que já contam com `color` para essa cor, bastando alterar essa variável.", '`--cor-txt: hsl(0, 0%, 0%)`'],
        'categoria': 'variável',
        'atualizada': '0.1.0'
    },
    {
        'nome': '--cor-link',
        'tipo': 'cor',
        'heranca': 'sim',
        'uso': ['Utilizada para definir a cor de texto (ou fundo) do link, no estado normal.', 'Está declarado diretamente na tag `a` dentro da layer `base`, mas pode ser aplicado por cascata', 'Se eliminada, utiliza o valor padrão de CSS', '`--cor-link: var(--cor-2);`'],
        'categoria': 'variável',
        'atualizada': '0.3.0',
    },
    {
        'nome': '--cor-hover',
        'tipo': 'cor',
        'heranca': 'sim',
        'uso': ['Utilizada para definir a cor de texto (ou fundo) do link, no estado hover.', 'Está declarado diretamente no seletor `a:hover` dentro da layer `base`, mas pode ser aplicado por cascata', 'Se eliminada, utiliza o valor padrão de CSS', '`--cor-hover: var(--cor-2);`'],
        'categoria': 'variável',
        'atualizada': '0.3.0',
    },
    {
        'nome': '--cor-visitado',
        'tipo': 'cor',
        'heranca': 'sim',
        'uso': ['Utilizada para definir a cor de texto (ou fundo) do link, no estado visitado.', 'Está declarado diretamente no seletor `a:visited` dentro da layer `base`, mas pode ser aplicado por cascata', 'Se eliminada, utiliza o valor padrão de CSS', '`--cor-hover: var(--cor-link);`'],
        'categoria': 'variável',
        'atualizada': '0.3.0',
    },
    {
        'nome': '--cor-titulo',
        'tipo': 'cor',
        'heranca': 'sim',
        'uso': ['Utilizada para definir a cor do título (normalmente do texto). Se for usar a cor padrão, pode simplesmente eliminar a variável.', '`--cor-titulo: var(--cor-2);`'],
        'categoria': 'fechada',
        'atualizada': '0.3.0',
    },
    {
        "nome": "--tema",
        "tipo": "texto",
        "heranca": "sim",
        "uso": ["Variável usada no `:root` para indicar qual o tema de cores utilizado. Valor inicial: \"padrão\".", '`--tema: \"alto contraste\"`'],
        'categoria': 'variável',
        'atualizada': '0.1.0'
    },
    {
        "nome": "--gap",
        "tipo": "porcentagem / medida",
        "heranca": "sim",
        "uso": ["Variável usada nos utilitários para indicar qual a medida de gap de um container que seja flex ou grid. O valor padrão varia de elemento por elemento", '`--gap: 1rem`'],
        'categoria': 'variável',
        'atualizada': '0.3.0'
    },
    {
        'nome': '--borda',
        'tipo': 'medida, texto e cor separado por espaço',
        'heranca': 'sim',
        'uso': ['Formata a borda do elemento', 'borda: 1px solid var(--cor-base)'],
        'categoria': 'variável',
        'atualizada': '0.3.0',
    },
    {
        "nome": "--rd",
        "tipo": "porcentagem / medida",
        "heranca": "sim",
        "uso": [f"variável para arredondar a borda. Diversos elementos em utilitários fazem uso dessa variável por padrão, de forma que ao alterar o valor inicial, vai alterar diversos elementos do {NOME}", '`border-radius: var(--rd)`'],
        'categoria': 'aberta',
        'atualizada': '0.1.0'
    },
    {
        "nome": "--cor-base",
        "tipo": "cor",
        "heranca": "sim",
        "uso": ["Variável usada em diversos elementos internos e serve como base de cor principal para que seja aplicado tons, permitindo alterações rápidas em todo o componente alterando apenas essa variável.", "Pode ser chamada com o snippet <code>gua_cor_base</code>.", '`--cor-base: var(--cor-1);`', '`--cor-txt: hsl(from var(--cor-base) h calc(s - 10) calc(l * .25)`'],
        'categoria': 'variável',
        'atualizada': '0.1.0'
    },
    {
        "nome": "--cor-secundaria",
        "tipo": "cor",
        "heranca": "sim",
        "uso": ["Variável usada em diversos elementos internos (menos usada que a `--cor-base`). Serve como base de cor secundária para que seja aplicado tons nos elementos e permitindo alterações rápidas em todo o componente alterando apenas essa variável.", "Pode ser chamada com o snippet <code>gua_cor_secundaria</code>.", '`--cor-secundaria: var(--cor-2);`', '`--cor-txt: hsl(from var(--cor-secundaria) h calc(s - 10) calc(l * .25)`'],
        'categoria': 'variável',
        'atualizada': '0.1.0'
    },
    {
        "nome": "--sombra",
        "tipo": "valores separados por espaço",
        "heranca": "sim",
        "uso": [f"variável para a sombra padrão. Diversos elementos em utilitários fazem uso dessa variável por padrão, de forma que ao alterar o valor inicial, vai alterar diversos elementos do {NOME}", '`box-shadow: var(--sombra)`'],
        'categoria': 'aberta',
        'atualizada': '0.1.0'
    },
    {
        "nome": "--pd",
        "tipo": "porcentagem / medida separados por espaço",
        "heranca": "sim",
        "uso": ["Variável utilizada para o padding de um utilitário.", '`--pd: .5em 1em;`', '`padding: var(--pd-i);`'],
        'categoria': 'variável',
        'atualizada': '0.3.0'
    },
    {
        "nome": "--mg",
        "tipo": "porcentagem / medida separados por espaço",
        "heranca": "sim",
        "uso": ["Variável utilizada para a margem de um utilitário.", '`--mg: 1em auto;`', '`margin: var(--mg);`'],
        'categoria': 'aberta',
        'atualizada': '0.3.0'
    },
    {
        "nome": "--modo",
        "tipo": "color-scheme",
        "heranca": 'sim',
        "uso": ["Variável usada no :root e em eventual tema para determinar qual o modo de cor usado. O root já faz uso de", '`color-scheme`', "bastando alterar o modo quando indicado. Veja mais em <a href='cores'>cores</a>", '`--modo: dark`'],
        'categoria': 'aberto',
        'atualizada': '0.1.0'
    },
    {
        "nome": "--fonte",
        "tipo": "texto separado por vírgula",
        "heranca": 'sim',
        "uso": ["variável usada no `<body>` e já conta com`font-family` para essa essa fonte, bastando alterar essa variável. Caso algum elemento vá apresentar outra fonte, chamar o `font-family` normalmente e declare nova variável de fonte no `:root`.", '`--fonte: \'Roboto\', var(--sans)`'],
        'categoria': 'variável',
        'atualizada': '0.1.0'
    },
    {
        'nome': '--txt',
        'tipo': 'medida / porcentagem',
        'heranca': 'sim',
        'uso': ['Determina o tamanho da fonte em elementos específicos.', '`--txt: 1.2em;`'],
        'categoria': 'variável',
        'atualizada': '0.3.0',
    },
    {
        'nome': '--cor-destaque',
        'tipo': 'cor',
        'heranca': 'sim',
        'uso': ['Uma variação de destaque de uma cor escolhida.', 'Lembre-se de redeclarar no seletor, caso você altere a cor utilizada.', "Pode ser chamada com o snippet <code>gua_cor_destaque</code> que já inclui um facilitador para criar o modo de cor."],
        'categoria': 'variável',
        'atualizada': '0.2.0',
    },
    {
        'nome': '--cor-suave',
        'tipo': 'cor',
        'heranca': 'sim',
        'uso': ['Uma variação de suave de uma cor escolhida.', 'Lembre-se de redeclarar no seletor, caso você altere a `cor-base`.', "Pode ser chamada com o snippet <code>gua_cor_suave</code> que já inclui um facilitador para criar o modo de cor."],
        'categoria': 'variável',
        'atualizada': '0.2.0',
    },
    {
        'nome': '--borda-vertical',
        'tipo': 'porcentagem / medida separadas por espaço',
        'heranca': 'sim',
        'uso': ['Define a espessura da(s) borda(s) vertical(is) do elemento (como nas colunas de uma tabela). Sobrepõe a medida utilizada na variável `--borda`', '`--borda-vertical: 0 1px`', 'border-inline-width: var(--borda-vertical);' ],
        'categoria': 'variável',
        'atualizada': '0.3.0',
    },
    {
        'nome': '--borda-horizontal',
        'tipo': 'porcentagem / medida separadas por espaço',
        'heranca': 'sim',
        'uso': ['Define a espessura da(s) borda(s) horizontal(is) do elemento (como nas linha de uma tabela). Sobrepõe a medida utilizada na variável `--borda`', '`--borda-horizontal: 0 1px`', 'border-block-width: var(--borda-horizontal);' ],
        'categoria': 'variável',
        'atualizada': '0.3.0',
    },
    {
        'nome': '--cor-borda',
        'tipo': 'cor',
        'heranca': 'sim',
        'uso': ['Utilizada em alguns elementos para definir a cor da borda, sobrepondo este elemendo da variável `--borda`'],
        'categoria': 'variável',
        'atualizada': '0.3.0',
    },
    {
        'nome': '--outline',
        'tipo': 'medida, texto e cor separados por espaço',
        'heranca': 'sim',
        'uso': ['Formata o outline do elemento atual'],
        'categoria': 'variável',
        'atualizada': '0.3.0',
    },
    {
        'nome': '--placeholder',
        'tipo': 'cor',
        'heranca': 'sim',
        'uso': ['Variável local para formulários, formata o placeholder dos campos'],
        'categoria': 'variável',
        'atualizada': '0.3.0',
    },
    {
        'nome': '--col-max',
        'tipo': 'medida',
        'heranca': 'sim',
        'uso': ['Variável para sistema de grid responsiva, indicando a largura máxima que a coluna pode atingir'],
        'categoria': 'variável',
        'atualizada': '0.3.0',
    },
    {
        'nome': '--colunas',
        'tipo': 'Propriedade modelo de grid',
        'heranca': 'sim',
        'uso': ['Determina a quantidade de colunas ou a formatação da mesma em um sistema de grid'],
        'categoria': 'variável',
        'atualizada': '0.3.0',
    },
    {
        'nome': '--line-height',
        'tipo': 'medida',
        'heranca': 'não',
        'uso': ['Determina o `line-height` dos elementos, seguindo. Essa medida foi criada com base no reset de <a href="https://www.joshwcomeau.com/css/custom-css-reset/#four-increase-line-height-5" target="_blank">Josh Comeau</a>.'],
        'categoria': 'fechada',
        'atualizada': '0.4.0',
    },
    
]
