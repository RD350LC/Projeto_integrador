document.addEventListener("DOMContentLoaded", () => {
    const imoveisLista = document.querySelector(".imoveis-lista");
    const adicionarImovelBtn = document.getElementById("adicionar-imovel");
    const semImoveisMsg = document.getElementById("sem-imoveis");
    const filtroInput = document.getElementById("filtro-imoveis");
    const loadingIndicator = document.getElementById("loading");

    let imoveis = JSON.parse(localStorage.getItem("imoveis")) || [];
    let isCorretor = false;

    // Mensagem de boas-vindas personalizada
    function mostrarMensagemBoasVindas() {
        const mensagem = isCorretor
            ? "Bem-vindo ao painel de gerenciamento de imóveis!"
            : "Bem-vindo! Explore nossos imóveis disponíveis.";
        alert(mensagem);
    }

    // Função para salvar imóveis no localStorage
    function salvarImoveis() {
        try {
            localStorage.setItem("imoveis", JSON.stringify(imoveis));
        } catch (error) {
            console.error("Erro ao salvar imóveis no localStorage:", error);
        }
    }

    // Função para renderizar a lista de imóveis
    function renderizarImoveis(lista = imoveis) {
        imoveisLista.innerHTML = "";
        if (!Array.isArray(lista) || lista.length === 0) {
            semImoveisMsg.style.display = "block";
            return;
        }
        semImoveisMsg.style.display = "none";
        lista.forEach((imovel, index) => {
            const imovelCard = document.createElement("div");
            imovelCard.classList.add("imovel-card", "fade-in");
            imovelCard.innerHTML = `
                <img src="${imovel.imagem}" alt="${imovel.titulo}" class="imovel-imagem">
                <h3>${imovel.titulo}</h3>
                <p>${imovel.descricao}</p>
                ${
                    isCorretor
                        ? `<button class="editar-imovel" data-index="${index}">Editar</button>
                           <button class="remover-imovel" data-index="${index}">Remover</button>`
                        : ""
                }
            `;
            imoveisLista.appendChild(imovelCard);
        });

        if (isCorretor) {
            document.querySelectorAll(".editar-imovel").forEach((btn) =>
                btn.addEventListener("click", editarImovel)
            );
            document.querySelectorAll(".remover-imovel").forEach((btn) =>
                btn.addEventListener("click", removerImovel)
            );
        }
    }

    // Função para filtrar imóveis
    function filtrarImoveis() {
        const termo = filtroInput.value.toLowerCase();
        const imoveisFiltrados = imoveis.filter(imovel =>
            imovel.titulo.toLowerCase().includes(termo)
        );
        renderizarImoveis(imoveisFiltrados);
    }

    // Função para adicionar um novo imóvel
    function adicionarImovel() {
        if (!isCorretor) {
            alert("Apenas corretores podem adicionar imóveis.");
            return;
        }
        const titulo = prompt("Digite o título do imóvel:")?.trim();
        const descricao = prompt("Digite a descrição do imóvel:")?.trim();
        const imagem = prompt("Digite a URL da imagem do imóvel:")?.trim();
        if (titulo && descricao && imagem) {
            imoveis.push({ titulo, descricao, imagem });
            salvarImoveis();
            renderizarImoveis();
        } else {
            alert("Título, descrição e imagem são obrigatórios.");
        }
    }

    // Função para editar um imóvel
    function editarImovel(event) {
        const index = event.target.dataset.index;
        const imovel = imoveis[index];
        if (!imovel) {
            alert("Imóvel não encontrado.");
            return;
        }
        const novoTitulo = prompt("Digite o novo título do imóvel:", imovel.titulo)?.trim();
        const novaDescricao = prompt("Digite a nova descrição do imóvel:", imovel.descricao)?.trim();
        const novaImagem = prompt("Digite a nova URL da imagem do imóvel:", imovel.imagem)?.trim();
        if (novoTitulo && novaDescricao && novaImagem) {
            imoveis[index] = { titulo: novoTitulo, descricao: novaDescricao, imagem: novaImagem };
            salvarImoveis();
            renderizarImoveis();
        } else {
            alert("Título, descrição e imagem são obrigatórios.");
        }
    }

    // Função para remover um imóvel
    function removerImovel(event) {
        const index = event.target.dataset.index;
        if (index === undefined || index < 0 || index >= imoveis.length) {
            alert("Índice inválido.");
            return;
        }
        if (confirm("Tem certeza de que deseja remover este imóvel?")) {
            imoveis.splice(index, 1);
            salvarImoveis();
            renderizarImoveis();
        }
    }

    // Função para mostrar indicador de carregamento
    function showLoading() {
        loadingIndicator.style.display = "block";
    }

    // Função para esconder indicador de carregamento
    function hideLoading() {
        loadingIndicator.style.display = "none";
    }

    // Evento para adicionar imóvel
    adicionarImovelBtn?.addEventListener("click", adicionarImovel);

    // Evento para filtrar imóveis
    filtroInput?.addEventListener("input", filtrarImoveis);

    // Renderizar imóveis iniciais com feedback visual
    showLoading();
    setTimeout(() => {
        renderizarImoveis(); // Simula carregamento
        hideLoading();
    }, 1000);
});
