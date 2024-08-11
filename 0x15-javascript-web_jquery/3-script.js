$(document).ready(function() {
    // Add class 'red' to <header> element when DIV#red_header is clicked
    $("#red_header").click(function() {
        $("header").addClass("red");
    });
});
