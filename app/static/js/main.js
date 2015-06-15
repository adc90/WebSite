$(document).ready(function(){

    /* Drop down menus */
    $('ul').on('mouseover', function(){
        $(this).find('li').css({'display': 'block'});
    });
    $('ul').on('mouseout', function(){
        $(this).find(':not(li:first-child)').css({'display': 'none'});
    });
});
