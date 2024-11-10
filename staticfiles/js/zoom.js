let zoomEnabled = false;

// Botão de ativação do modo zoom
const toggleZoomButton = document.getElementById('toggleZoom');

// Adiciona evento para alternar o modo zoom
toggleZoomButton.addEventListener('click', () => {
    zoomEnabled = !zoomEnabled;
    if (zoomEnabled) {
        document.body.classList.add('zoom-enabled');
        toggleZoomButton.classList.add('active');
    } else {
        document.body.classList.remove('zoom-enabled');
        toggleZoomButton.classList.remove('active');
    }
});

// Função para aumentar o texto quando o mouse passa sobre um elemento
document.addEventListener('mouseover', (event) => {
    if (zoomEnabled && event.target.closest('.zoomable')) {
        event.target.classList.add('zoom-text');
    }
});

// Função para retornar ao tamanho normal quando o mouse sai do elemento
document.addEventListener('mouseout', (event) => {
    if (zoomEnabled && event.target.classList.contains('zoom-text')) {
        event.target.classList.remove('zoom-text');
    }
});