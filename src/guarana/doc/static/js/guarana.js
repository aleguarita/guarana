// Base para a aplicação e remoção de tema. O tema é aplicado ou removido
// diretamente no <body>
// -----------------------------------------------------------------------------
function guaRemoverTemas() {
    let root = document.documentElement

    root.classList.forEach(temas => {
        if (temas.startsWith('tema_')) {
            root.classList.remove(temas)
        }
    })
}

function guaAplicarTema(tema) {
    guaRemoverTemas()
    let root = document.documentElement
    root.classList.add(tema)
}