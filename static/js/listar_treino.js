document.addEventListener('DOMContentLoaded', function() {
    console.log('💪 Sistema de Treinos carregado!');
    iniciarAnimacoes();
    iniciarInteracoes();
});

// Função para mostrar/ocultar exercícios
function toggleExercicios(treinoId) {
    const lista = document.getElementById(`exercicios-${treinoId}`);
    const botao = document.querySelector(`#toggle-text-${treinoId}`);
    const icon = botao.parentElement.querySelector('i');
    
    if (lista.classList.contains('show')) {
        lista.classList.remove('show');
        botao.textContent = 'Ver Exercícios';
        icon.className = 'fas fa-eye';
    } else {
        lista.classList.add('show');
        botao.textContent = 'Ocultar Exercícios';
        icon.className = 'fas fa-eye-slash';
    }
    
    // Efeito sonoro (opcional)
    playClickSound();
}

// Animações de entrada
function iniciarAnimacoes() {
    const cards = document.querySelectorAll('.card-treino');
    
    cards.forEach((card, index) => {
        card.style.animationDelay = `${index * 0.1}s`;
    });
}

// Interações e efeitos
function iniciarInteracoes() {
    // Efeitos nos botões
    const botoes = document.querySelectorAll('.btn-acao, .btn');
    
    botoes.forEach(botao => {
        botao.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-3px) scale(1.02)';
        });
        
        botao.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
        });
        
        botao.addEventListener('click', function(e) {
            // Efeito de clique
            this.style.transform = 'scale(0.95)';
            setTimeout(() => {
                this.style.transform = 'scale(1)';
            }, 150);
            
            // Loading para PDF
            if (this.classList.contains('btn-pdf')) {
                mostrarCarregamento(this);
            }
        });
    });
    
    // Efeitos nos cards
    const cards = document.querySelectorAll('.card-treino');
    cards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-15px) scale(1.02)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
        });
    });
}

// Loading nos botões
function mostrarCarregamento(botao) {
    const textoOriginal = botao.innerHTML;
    botao.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Gerando PDF...';
    botao.style.pointerEvents = 'none';
    botao.style.opacity = '0.7';
    
    setTimeout(() => {
        botao.innerHTML = textoOriginal;
        botao.style.pointerEvents = 'auto';
        botao.style.opacity = '1';
    }, 3000);
}

// Efeito sonoro (opcional)
function playClickSound() {
    // Você pode adicionar um som de clique aqui se quiser
    // const audio = new Audio('/static/sounds/click.mp3');
    // audio.volume = 0.1;
    // audio.play();
}

// Scroll suave para o topo
function scrollToTop() {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
}

console.log('✅ JavaScript dos treinos carregado com sucesso!');