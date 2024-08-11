$(document).ready(function() {
    $("#toggle_header").click(function() {
        // Check if <header> element has class 'red'
        if ($("header").hasClass("red")) {
            // Toggle class from 'red' to 'green'
            $("header").removeClass("red").addClass("green");
        } else if ($("header").hasClass("green")) {
            // Toggle class from 'green' to 'red'
            $("header").removeClass("green").addClass("red");
        } else {
            // If <header> has no class, default to 'red'
            $("header").addClass("red");
        }
    });
});
