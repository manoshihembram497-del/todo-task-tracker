const button = document.querySelector('.toggle');
const nav = document.querySelector('.nav-links');
button.addEventListener("click", ()=>{
    nav.classList.toggle('active');
});