document.addEventListener('DOMContentLoaded', () => {
    const excluirBtns = document.querySelectorAll('.excluir-btn');
    const editarBtns = document.querySelectorAll('.editar-btn');
    const inserirBtn = document.getElementById('inserir-btn');
    const inserirCampos = document.getElementById('inserir-campos');
    const editarCampos = document.getElementById('editar-campos');
    const editarForm = document.getElementById('editar-form');

    // Evento para excluir uma empresa:

    excluirBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const despejoId = btn.dataset.id;
            if (confirm('Tem certeza que deseja excluir?')) {
                fetch(`/excluirDes/${despejoId}`, { method: 'DELETE' })
                    .then(response => response.json())
                    .then(data => {
                        alert(data.message);
                        location.reload(); 
                    })
                    .catch(error => {
                        console.error('Erro ao excluir:', error);
                        alert('Ocorreu um erro ao excluir.');
                    });
            }
        });
    });

    // Evento para editar uma empresa: //

    editarBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const despejoId = btn.dataset.id;
            fetch(`/editarDes/${despejoId}`, {
                method: 'GET'
            })
            .then(response => response.json())
            .then(data => {
                document.getElementById('editar-id').value = data.id;
                document.getElementById('editar-entidade').value = data.entidade;
                document.getElementById('editar-codigo').value = data.codigo;
                document.getElementById('editar-ano').value = data.ano;
                document.getElementById('editar-participacao').value = data.participacao;

                editarCampos.classList.remove('hidden');
            })
            .catch(error => console.error('Erro ao buscar dados:', error));
        });
    });
    
    editarForm.addEventListener('submit', (event) => {
        event.preventDefault(); 
    
        const formData = new FormData(editarForm);
    
        // Adicione o ID à FormData usando JavaScript
        const producaoId = document.getElementById('editar-id').value;
        formData.append('id', producaoId);
    
        fetch('/editarDes', {
            method: 'POST',
            body: formData
        })        
        
        .then(response => {
            if (response.ok) {
                location.reload();
            } else {
                alert('Erro ao editar empresa.');
            }
        })
        .catch(error => console.error('Erro ao editar empresa:', error));
    });

    inserirBtn.addEventListener('click', () => {
        inserirCampos.classList.toggle('hidden');
    });

    editarForm.addEventListener('submit', (event) => {
        event.preventDefault(); 

        const formData = new FormData(editarForm);

        fetch('/editarDes', {
            method: 'POST',
            body: formData
        })
        .then(response => {
            if (response.ok) {
                location.reload();
            } else {
                alert('Erro ao editar empresa.');
            }
        })
        .catch(error => console.error('Erro ao editar empresa:', error));
    });
});