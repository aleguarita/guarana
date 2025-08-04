# Guaraná
Baseado no Front_Alego, gem de Ruby que desenvolvi para a Assembleia Legislativa do Estado de Goiás, esse módulo Python instala um framework css funcional para módulos Flask ou mesmo para HTML estático, que dá a base para trabalhar, sem limitar com um estilo fixo caso decida alterar, mas também permite fazer um site rápido com mudanças mínimas.

Além dos arquivos de CSS, inclui alguns JS básicos para algumas funcionalidades pontuais e vários snippets de VSCode para facilitar o uso.

[Changelog](changelog.md)

## Instalando
Para o funcionamento é necessário Python 3.12 ou superior. No seu ambiente virtual execute:

```bash
pip install guarana_aag
```

Na pasta do seu sistema execute o comando
```bash
python -m guarana instalar
```

Como parâmetro opcional, utilize `--flask` caso seu sistema esteja zerado, isso vai instalar também os arquivos básicos para um sistema em flask, incluindo views como a 404.html

<!-- Para atualizar os arquivos do guarana, utilize o comando:
```bash
python -m guarana atualizar
``` -->

## CSS a ser usado
Depois de instalado, serão criados alguns arquivos de `.css` na raíz.

- `_guarana_base.css` - esse arquivo contém a base do Guaraná e não deve ser alterado, já que é gerado dinamicamente
- `estilo.css` - o arquivo a ser trabalhado. Ele pode ser importado diretamente no HTML. Note, porém, que há muitos `@import` o que gera várias requisições HTTP
- `estilo-min.css` - todo o Guaraná compactado em um único CSS, importe no HTML para ser mais eficiente posteriormente. Esse arquivo é gerado dinamicamente através do comando:

```bash
python -m guarana min
```
