
let plus_buttons = document.querySelectorAll('.plus_btn');

plus_buttons.forEach((element) =>{
    element.addEventListener('click',() =>{
        const pop_up = document.querySelector('.popup_main')
        pop_up.style.display = 'flex';
        
        const close_btn = document.querySelector('.cancel');
        close_btn.addEventListener('click', () =>{
            pop_up.style.display = 'none';
        })
    })
})


$(document).ready(function(){
    $('.carousel').carousel();
});
