let pg_atual = document.location.pathname

// aplicar tema
const aplicarTema = document.getElementById('gua_tema');
if (aplicarTema) {
    aplicarTema.addEventListener('change', () => {
        const temaSelecionado = aplicarTema.value;
        localStorage.setItem('temaSelecionado', temaSelecionado);

        // Remove qualquer tema anterior e adiciona o novo
        guaAplicarTema(temaSelecionado)
    });
}

// ativar itens do menu
let itens_menu = document.querySelectorAll('.conteudo__menu .menu__link')
itens_menu.forEach(item => item.classList.remove('ativo'))
let link_atual = document.querySelector(`[href="${pg_atual}"]`)
link_atual.classList.add('ativo')


// eventos ao carregar
window.addEventListener('DOMContentLoaded', () => {
    const temaSalvo = localStorage.getItem('temaSelecionado');
    
    if (temaSalvo) {
        aplicarTema.value = temaSalvo
        guaAplicarTema(temaSalvo)
    }
});

guaAtivarDesativarAbas()


