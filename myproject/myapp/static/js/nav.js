

document.addEventListener('DOMContentLoaded', () => {
    let navdiv = document.getElementById('navdiv');
    document.addEventListener('scroll', () => {
        if (window.pageYOffset > 70) {
            navdiv.style.position = "fixed";
            navdiv.style.top = "0";
            navdiv.style.backgroundColor="black";
            // navdiv.classList.remove('hidden')


        } else {
            navdiv.style.position = "";
            navdiv.style.top = "";
            navdiv.style.backgroundColor="";
        }
        
    }
    );
});


$(document).ready(function(){
    $(".navbar .nav-link").on('click', function(event) {

        if (this.hash !== "") {

            event.preventDefault();

            var hash = this.hash;

            $('html, body').animate({
                scrollTop: $(hash).offset().top
            }, 700, function(){
                window.location.hash = hash;
            });
        } 
    });
});

let home = document.getElementById('home')
let blogs = document.getElementById('blogs')
let mandi = document.getElementById('mandi')
let forecast = document.getElementById('forecast')

home.addEventListener('click',()=>{
    // document.addEventListener('scroll',()=>{

    // })

    
})
