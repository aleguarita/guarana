// Base para a aplicação e remoção de tema. O tema é aplicado ou removido
// diretamente no <body>
// -----------------------------------------------------------------------------
function guaRemoverTemas() {
    let body = document.documentElement

    body.classList.forEach(temas => {
        if (temas.startsWith('tema_')) {
            body.classList.remove(temas)
        }
    })
}

function guaAplicarTema(tema) {
    guaRemoverTemas()
    let body = document.documentElement
    body.classList.add(tema)
}