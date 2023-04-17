$(document).ready(function() {
    $(".custom-link.nav-link").click(function(e)
    {
        $(".custom-link.nav-link").removeClass("active");
        $(this).addClass("active");
        $(".tab-pane.container").removeClass("active").addClass("fade");
        var target_tab_selector = $(this).attr('href');
        $(target_tab_selector).addClass('active');
        $(target_tab_selector).addClass('show');
    });
});