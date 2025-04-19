document.addEventListener("DOMContentLoaded", () => {
    const formContato = document.getElementById("form-contato");

    formContato.addEventListener("submit", (event) => {
        event.preventDefault();

        const nome = document.getElementById("nome").value.trim();
        const email = document.getElementById("email").value.trim();
        const mensagem = document.getElementById("mensagem").value.trim();

        if (!nome || !email || !mensagem) {
            alert("Por favor, preencha todos os campos.");
            return;
        }

        if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
            alert("Por favor, insira um e-mail válido.");
            return;
        }

        alert(`Obrigado pelo contato, ${nome}! Entraremos em contato em breve.`);
        formContato.reset();
    });
});
