document.addEventListener('DOMContentLoaded', function () {
    var myCarousel = document.querySelector('#carouselExampleCaptions');
    var carousel = new bootstrap.Carousel(myCarousel, {
        interval: 2000, // Tiempo entre transiciones en milisegundos
        wrap: true // Si el carrusel debe volver a empezar después de la última imagen
    });
});