jQuery(document).ready(function(){
    var p = $("#badge");
    width = parseInt(p.css('width')) + 80;
    p.css('width', width);
    rad = width/2;
    left =  0-(rad*(1-Math.cos(45)))/2 - 40;
    p.css('left',left-10);
    p.css('top',(Math.sqrt((width*width)/2)/2)-35);
});
