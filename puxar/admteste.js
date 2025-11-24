// Adicione esta função para validar URLs
function validarUrl(url) {
    try {
        new URL(url);
        return true;
    } catch {
        return false;
    }
}

// Modifique a função buscarCursos para incluir validação
async function buscarCursos() {
    const areaPredefinida = document.getElementById('areaPredefinida').value;
    const urlPersonalizada = document.getElementById('url').value;
    const filtroUrl = document.getElementById('filtroUrl').value;
    const areaConhecimento = document.getElementById('areaConhecimento').value;

    // Validar entrada
    if (!areaPredefinida && !urlPersonalizada) {
        showError('Por favor, selecione uma área predefinida ou informe uma URL personalizada.');
        return;
    }

    // Validar URL personalizada se fornecida
    if (urlPersonalizada && !validarUrl(urlPersonalizada)) {
        showError('Por favor, informe uma URL válida.');
        return;
    }

    // Resto do código permanece igual...
    showLoading(true);
    hideMessages();
    hideResults();

    try {
        const response = await fetch('/buscar', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                url: areaPredefinida === 'personalizada' ? urlPersonalizada : areaPredefinida,
                filtro_url: filtroUrl,
                area_conhecimento: areaConhecimento
            })
        });

        const data = await response.json();

        if (data.success) {
            showResults(data);
            showSuccess(`Busca concluída! Encontrados ${data.total} cursos.`);
        } else {
            showError(data.error || 'Erro ao buscar cursos.');
        }
    } catch (error) {
        showError('Erro de conexão: ' + error.message);
    } finally {
        showLoading(false);
    }
}