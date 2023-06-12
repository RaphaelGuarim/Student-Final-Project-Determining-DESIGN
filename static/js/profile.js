document.body.style.zoom = "95%";

const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        if (entry.isIntersecting){
            entry.target.classList.add('slide');
        }
    });
})

const hidden = document.querySelectorAll('.hide')
console.log(hidden.length)

hidden.forEach((el) =>  {
    console.log(el);
    observer.observe(el);
})
