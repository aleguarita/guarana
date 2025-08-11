const aplicarTema = document.getElementById('gua_tema');

if (aplicarTema) {
    aplicarTema.addEventListener('change', () => {
        const temaSelecionado = aplicarTema.value;
        localStorage.setItem('temaSelecionado', temaSelecionado);

        // Remove qualquer tema anterior e adiciona o novo
        guaAplicarTema(temaSelecionado)
    });
}

window.addEventListener('DOMContentLoaded', () => {
    const temaSalvo = localStorage.getItem('temaSelecionado');
    
    if (temaSalvo) {
        aplicarTema.value = temaSalvo
        guaAplicarTema(temaSalvo)
    }
});