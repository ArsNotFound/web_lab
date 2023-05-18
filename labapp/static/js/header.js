document.addEventListener("DOMContentLoaded", function () {
    let navlist = document.querySelectorAll(".menu-element");

    console.log(navlist);
    navlist.forEach((elem, index) => {
        if (elem.classList.contains('neuro')) {
            elem.classList.add('select');
        } else if (elem.classList.contains('promt')) {
            elem.classList.add('select');
        } else if (elem.classList.contains('news')) {
            elem.classList.add('select');
        } else if (elem.classList.contains('learnig')) {
            elem.classList.add('select');
        } else if (elem.classList.contains('contacts')) {
            elem.classList.add('select');
        }
    });
});