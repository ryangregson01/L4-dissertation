/* For resizing form input boxes height */
$('.resizeForm').on('keydown input', function() {
    this.style.removeProperty('height');
    this.style.height = (this.scrollHeight+2) + 'px';
}).on('mousedown focus', function() {
    this.style.removeProperty('height');
    this.style.height = (this.scrollHeight+2) + 'px';
});