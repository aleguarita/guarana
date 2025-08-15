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


// Ativação e desativação de Abas
// -----------------------------------------------------------------------------
function guaAtivarDesativarAbas(classe="abas", ativo="ativo", atributo="data-aba") {
    let nav = `${classe}__item`
    let conteudo = `${classe}__conteudo`

    let todos_nav = document.querySelectorAll(`.${nav}`)
    let todos_conteudo = document.querySelectorAll(`.${conteudo}`)

    if (todos_nav.length != todos_conteudo.length) {
        console.log(`Existem ${todos_nav.length} links de aba e ${todos_conteudo.length} conteúdos de aba`)
        return
    }

    if (todos_conteudo.length > 0) {
        todos_nav.forEach(item => {
            let id_href = item.getAttribute(atributo).replace('#', '')
            let aba_atual = document.getElementById(id_href)
            
            item.addEventListener('click', () => {
                // retira classes ativas
                let nav_ativo_atual = document.querySelector(`.${nav}.${ativo}`)
                if (nav_ativo_atual) {
                    nav_ativo_atual.classList.remove(ativo)
                }

                let nav_conteudo_atual = document.querySelector(`.${conteudo}.${ativo}`)
                if (nav_conteudo_atual) {
                    nav_conteudo_atual.classList.remove(ativo)
                }
    
                // aplica classes ativa
                item.classList.add(ativo)
                aba_atual.classList.add(ativo)
            })
        })
    }

}