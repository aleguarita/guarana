# Changelog

## 0.5.0
- Acordeão
- Ajuste em `avisos.css` que agora tem a variável `--borda`

## 0.4.0
- Aviso
- Fonte de ícones Material do Google
- Arquivo `botoes.css` renomeado para `botao.css`
- Formatação para o botão ativo
- `.bt--secundario` em sua versão básica  modifica demais variantes de botões
- Inclusão da sombra padrão no botão e no aviso
- Inclusão dos comandos do guarana em `rodar.py` permitindo visualizar a
documentação e atualizar o css minificado quando trabalha no flask no ambiente
de desenvolvimento
- Corrigido um erro que fazia com que o arquivo `_guarana_base.css` estava
ignorando a ordem de arquivos, que deveria incluir propriedades e reset em
primeiro lugar.
- Corrigido um bug que impedia a própria instalação da pasta `\static` ao escolher
a opção `--flask` quando havia a possibilidade de existir uma pasta `\static` em
`\.venv`
- Corrigido um erro que importava as macros de forma errada
- Corrigida as propriedades de margem, que estavam sendo ignoradas

## 0.3.0
- Formulários
- Botões
- Macros de Flask
- Abas voltou a ser `.abas` para melhor uso do BEM
- Variáveis locais aparecem no próprio elemento em utils para evitar "adivinhar" qual variável é usada no elemento (como no caso de `--cor-base` que é usada em todos e só aparecia no :root)

## 0.2.0
- Menu
- Tabela
- Abas
- Classes globais: `rolagem_x`
- JS para inserir/retirar a classe `.ativo` para seletores
- O uso de `@container style(--mode: dark | light)` foi substituído por `@midia (prefers-color-scheme: dark | light)` para melhor compatibilidade entre navegadores
- Uso de `@container style(--tema: 'nome tema')` foi trocado para `.tema_nome_tema &` para melhor compatibilidade entre navegadores

## 0.1.1
- Documentação para JS
- Snippets de JS
- Aplicação de temas na documentação

## 0.1.0
- Definição de layers
- Definição de propriedades de css
- Definição de cores e temas
- Snippets
- JavaScript

## 0.0.3
- O comando de minificar é regerado a cada alteração na pasta `/css`
- Comandos para atualizar e resetar
- Comando para rodar

## 0.0.2
- Gerando a base dos arquivos javascript
- Reset de CSS
- Comando flask agora é subcomando de instalar
- Comando para criar CSS minificado
- Arquivo `_guarana_base.css` → contém toda a base do Guaraná
- Arquivo `estilo.css` → arquivo de usuário para usar
- Arquivo `estilo-min.css` → arquivo minificado para o usuário

## 0.0.1
- Abandando o SCSS
- Estrutura base do app
- Comando para a criação do ambiente Flask
