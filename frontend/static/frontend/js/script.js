document.addEventListener('DOMContentLoaded', () => {
    const welcomeMessages = [
        "Bem-vindo à Página Inicial",
        "Explore nossos imóveis incríveis",
        "Encontre o lar dos seus sonhos",
        "Conecte-se com nossos corretores"
    ];
    const welcomeElement = document.getElementById('dynamic-welcome');
    let index = 0;

    setInterval(() => {
        index = (index + 1) % welcomeMessages.length;
        welcomeElement.textContent = welcomeMessages[index];
    }, 4000);
});
