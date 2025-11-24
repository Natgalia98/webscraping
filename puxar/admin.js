document.addEventListener('DOMContentLoaded', function() {
    carregarUrlsPredefinidas();
            
            // Configurar evento para área predefinida
    document.getElementById('areaPredefinida').addEventListener('change', function() {
        const urlGroup = document.getElementById('urlPersonalizadaGroup');
            if (this.value === 'personalizada') {
                urlGroup.style.display = 'block';
            } else {
                urlGroup.style.display = 'none';
            }
            });
        });

        async function carregarUrlsPredefinidas() {
            try {
                const response = await fetch('/urls-predefinidas');
                const urls = await response.json();
                
                const quickLinks = document.getElementById('quickLinks');
                quickLinks.innerHTML = '';
                
                for (const [key, info] of Object.entries(urls)) {
                    const button = document.createElement('div');
                    button.className = 'quick-link-btn';
                    button.innerHTML = `📖 ${info.nome}`;
                    button.onclick = () => preencherFormulario(key, info);
                    quickLinks.appendChild(button);
                }
            } catch (error) {
                console.error('Erro ao carregar URLs pré-definidas:', error);
            }
        }

        function preencherFormulario(area, info) {
            document.getElementById('areaPredefinida').value = area;
            document.getElementById('filtroUrl').value = info.filtro_sugerido || '';
            document.getElementById('areaConhecimento').value = '';
            document.getElementById('urlPersonalizadaGroup').style.display = 'none';
            
            document.querySelector('.search-section').scrollIntoView({ 
                behavior: 'smooth' 
            });
        }

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

            // Mostrar loading
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
                        url: areaPredefinida || urlPersonalizada,
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

        function showResults(data) {
            const cursosList = document.getElementById('cursosList');
            const totalCursos = document.getElementById('totalCursos');
            const resultsSection = document.getElementById('resultsSection');

            totalCursos.textContent = `${data.total} curso(s) encontrado(s)`;
            
            if (data.total === 0) {
                cursosList.innerHTML = '<p style="text-align: center; padding: 40px; color: #7f8c8d;">Nenhum curso encontrado com os critérios informados.</p>';
            } else {
                cursosList.innerHTML = data.cursos.map(curso => `
                    <div class="course-card">
                        <div class="course-name">${curso.nome}</div>
                        <div class="course-url">
                            <a href="${curso.url}" target="_blank">${curso.url}</a>
                        </div>
                    </div>
                `).join('');
            }

            resultsSection.style.display = 'block';
            resultsSection.scrollIntoView({ behavior: 'smooth' });
        }

        function showLoading(show) {
            document.getElementById('loading').style.display = show ? 'block' : 'none';
        }

        function showError(message) {
            const errorDiv = document.getElementById('errorMessage');
            errorDiv.textContent = message;
            errorDiv.style.display = 'block';
            errorDiv.scrollIntoView({ behavior: 'smooth' });
        }

        function showSuccess(message) {
            const successDiv = document.getElementById('successMessage');
            successDiv.textContent = message;
            successDiv.style.display = 'block';
        }

        function hideMessages() {
            document.getElementById('errorMessage').style.display = 'none';
            document.getElementById('successMessage').style.display = 'none';
        }

        function hideResults() {
            document.getElementById('resultsSection').style.display = 'none';
        }

        function limparBusca() {
            document.getElementById('areaPredefinida').value = '';
            document.getElementById('url').value = '';
            document.getElementById('filtroUrl').value = '';
            document.getElementById('areaConhecimento').value = '';
            document.getElementById('urlPersonalizadaGroup').style.display = 'none';
            hideMessages();
            hideResults();
        }