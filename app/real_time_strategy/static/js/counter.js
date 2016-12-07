$(document).ready(function() {
    setInterval(function() {
        $counter = $('#1');
        var current = parseInt($counter.html());
        $('#1').html((current + 1).toString());
    }, 1000);
});