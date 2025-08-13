// Base para a aplicação e remoção de tema. O tema é aplicado ou removido
// diretamente no <html>
// -----------------------------------------------------------------------------
function guaRemoverTemas() {
    let body = document.documentElement

    body.classList.forEach(temas => {
        if (temas.startsWith('tema')) {
            body.classList.remove(temas)
        }
    })
}
function guaAplicarTema(tema) {
    guaRemoverTemas()
    let body = document.documentElement
    body.classList.add(tema)
}

// Busca pelos elementos que contenham a classe escolhida e retira a classe
// `ativo` (ou uma variação passada no segundo parâmetro) em todos os itens
// com a classe, inserindo o `ativo` no item clicado
// -----------------------------------------------------------------------------
function guaAtivarDesativar(classe, classe_ativa="ativo") {
    let todos_itens = document.querySelectorAll(`.${classe}`)
    
    if (todos_itens.length > 0) {
        todos_itens.forEach(item => {
            item.addEventListener('click', () => {
                // retirar o item atual (se tiver)
                let ativo_atual = document.querySelector(`.${classe}.${classe_ativa}`)
                if (ativo_atual) {
                    ativo_atual.classList.remove(classe_ativa)
                }
                
                item.classList.add(classe_ativa)
            })
        })
    }
}