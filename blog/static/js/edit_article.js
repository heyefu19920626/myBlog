function add_tag(){
    $('.span-tag').each(function(){
        $(this).text() || $(this).parent().remove();
    });
    var div_tag = '<div class="div-flex mar-r-5"><span class="span-tag" contenteditable="true"></span><i class="icon-close"></i></div>';
    $('#addTag').before(div_tag);

    $('.span-tag').click(function(event){
        event.stopPropagation();
    })

    $('.icon-close').click(function(event){
        $(this).parent('div').remove()
    });
}

$(document).click(function(){
    var span_tag = $('.span-tag');
    span_tag.length > 4 ? $('#addTag').hide() : $('#addTag').show();
    var tag_value = "";
    $('.span-tag').each(function(){
        $(this).text() ? (tag_value += $(this).text() + ";") : $(this).parent().hide();
    });
    $('#hideTags').attr('value', tag_value.substring(0,tag_value.length-1).replace(/;/g, '/'));
});

$('#addTag').click(function(event){
        event.stopPropagation();
});

$('#preview-aritcle-tab').click(function(event){
        event.stopPropagation();
});

$('.icon-close').click(function(event){
    $(this).parent('div').remove()
});

