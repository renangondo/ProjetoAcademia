document.addEventListener('DOMContentLoaded', function() {
    // Animação suave para as linhas da tabela
    const rows = document.querySelectorAll('tbody tr');
    rows.forEach((row, index) => {
        row.style.animationDelay = `${index * 0.1}s`;
        row.classList.add('fade-in');
    });
    
    // Confirmação de exclusão melhorada
    const deleteButtons = document.querySelectorAll('.btn-delete');
    deleteButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            const alunoNome = this.closest('tr').querySelector('.aluno-nome').textContent.trim();
            
            // Modal de confirmação personalizado
            showConfirmDialog(
                'Confirmar Exclusão',
                `⚠️ Tem certeza que deseja excluir o aluno "${alunoNome}"?\n\nEsta ação não pode ser desfeita e todos os dados relacionados serão perdidos.`,
                () => {
                    window.location.href = this.href;
                }
            );
        });
    });
    
    // Tooltip para os botões
    const actionButtons = document.querySelectorAll('.btn-action');
    actionButtons.forEach(button => {
        button.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-2px) scale(1.05)';
        });
        
        button.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
        });
    });
    
    // Adicionar CSS para animações
    addAnimationStyles();
});

// Função para criar modal de confirmação personalizado
function showConfirmDialog(title, message, onConfirm) {
    // Criar overlay
    const overlay = document.createElement('div');
    overlay.style.cssText = `
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0,0,0,0.5);
        z-index: 9999;
        display: flex;
        align-items: center;
        justify-content: center;
    `;
    
    // Criar modal
    const modal = document.createElement('div');
    modal.style.cssText = `
        background: white;
        border-radius: 12px;
        padding: 2rem;
        max-width: 400px;
        width: 90%;
        box-shadow: 0 20px 60px rgba(0,0,0,0.3);
        animation: modalSlideIn 0.3s ease;
    `;
    
    modal.innerHTML = `
        <h3 style="margin: 0 0 1rem 0; color: #2c3e50; font-size: 1.25rem;">
            <i class="fas fa-exclamation-triangle" style="color: #f39c12; margin-right: 0.5rem;"></i>
            ${title}
        </h3>
        <p style="margin: 0 0 2rem 0; color: #6c757d; line-height: 1.5;">
            ${message}
        </p>
        <div style="display: flex; gap: 1rem; justify-content: flex-end;">
            <button class="cancel-confirm-btn" style="
                background: #6c757d;
                color: white;
                border: none;
                padding: 0.75rem 1.5rem;
                border-radius: 6px;
                cursor: pointer;
                font-weight: 600;
                transition: all 0.2s;
            ">Cancelar</button>
            <button class="confirm-btn" style="
                background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%);
                color: white;
                border: none;
                padding: 0.75rem 1.5rem;
                border-radius: 6px;
                cursor: pointer;
                font-weight: 600;
                transition: all 0.2s;
            ">Excluir</button>
        </div>
    `;
    
    // Adicionar event listeners
    modal.querySelector('.cancel-confirm-btn').addEventListener('click', () => {
        document.body.removeChild(overlay);
    });
    
    modal.querySelector('.confirm-btn').addEventListener('click', () => {
        document.body.removeChild(overlay);
        onConfirm();
    });
    
    // Fechar ao clicar no overlay
    overlay.addEventListener('click', (e) => {
        if (e.target === overlay) {
            document.body.removeChild(overlay);
        }
    });
    
    overlay.appendChild(modal);
    document.body.appendChild(overlay);
}

// Função para adicionar estilos de animação
function addAnimationStyles() {
    const style = document.createElement('style');
    style.textContent = `
        @keyframes fade-in {
            from {
                opacity: 0;
                transform: translateY(10px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        @keyframes modalSlideIn {
            from {
                opacity: 0;
                transform: scale(0.8) translateY(-20px);
            }
            to {
                opacity: 1;
                transform: scale(1) translateY(0);
            }
        }
        
        .fade-in {
            animation: fade-in 0.5s ease forwards;
        }
        
        .cancel-confirm-btn:hover {
            background: #545b62 !important;
        }
        
        .confirm-btn:hover {
            background: linear-gradient(135deg, #ff5252 0%, #d63031 100%) !important;
            transform: translateY(-1px);
        }
    `;
    document.head.appendChild(style);
}