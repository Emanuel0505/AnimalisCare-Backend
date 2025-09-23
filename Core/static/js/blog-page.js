
// Funcionalidade para mostrar o menu de filtragem
const filterBtn = document.getElementById('filter-button');
const filterMenu = document.getElementById('menu-filter');

filterBtn.addEventListener("click", () => {
    filterMenu.style.display = filterMenu.style.display === "block" ? "none" : "block";
});

document.addEventListener("click", (e) => {
    if (!filterBtn.contains(e.target) && !filterMenu.contains(e.target)) {
        filterMenu.style.display = "none";
    }
});

// Funcionalidade para mostrar o menu de ordenação
const orderBtn = document.getElementById('order-button');
const orderMenu = document.getElementById('menu-order');

orderBtn.addEventListener("click", () => {
    orderMenu.style.display = orderMenu.style.display === "block" ? "none" : "block";
});

document.addEventListener("click", (e) => {
    if (!orderBtn.contains(e.target) && !orderMenu.contains(e.target)) {
        orderMenu.style.display = "none";
    }
});

// Funcionalidade avançar e voltar do carrossel
document.addEventListener("DOMContentLoaded", function () {
    const carousel = document.getElementById("carousel");
    const prevButton = document.getElementById("prev-button");
    const nextButton = document.getElementById("next-button");

    function getCardWidth() {
        const card = carousel.querySelector(".card-container");
        if (!card) return 0;
        const style = getComputedStyle(card);
        const marginRight = parseFloat(style.marginRight) || 0;
        return card.offsetWidth + marginRight;
    }

    let step = getCardWidth();

    window.addEventListener("resize", () => {
        step = getCardWidth();
    }); 

    // Avançar 
    nextButton.addEventListener("click", () => {
        carousel.scrollBy({ left: step, behavior: "smooth" });
    });

    // Voltar
    prevButton.addEventListener("click", () => {
        carousel.scrollBy({ left: -step, behavior: "smooth" });
    });
});

// Funcionalidade para mudar a paginação
document.addEventListener("DOMContentLoaded", () => {
  const links = document.querySelectorAll(".page-link");

  links.forEach(link => {
    link.addEventListener("click", (e) => {
      e.preventDefault(); // evita recarregar a página
      links.forEach(l => l.classList.remove("active"));
      link.classList.add("active");
    });
  });
});