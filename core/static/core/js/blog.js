const openBtn = document.getElementById("openPostModal");
const closeBtn = document.getElementById("closePostModal");
const modal = document.getElementById("postModal");

openBtn.addEventListener("click", () => {
    modal.classList.remove("hidden");
    modal.classList.add("flex");
});

closeBtn.addEventListener("click", () => {
    modal.classList.remove("flex");
    modal.classList.add("hidden");
});