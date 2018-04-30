function add_tag(){
    $('.span-tag').each(function(){
        $(this).text() || $(this).parent().remove();
    });
    if($('.span-tag').length > 4){
        $('#addTag').hide();
        return;
    }
    var div_tag = '<div class="div-flex mar-r-5"><span class="span-tag" contenteditable="true"></span><i class="icon-close"></i></div>';
    var div_tag = $('#addTag').before(div_tag);
    $('#addTag').prev().find('.span-tag').focus();
    $('.icon-close').click(function(event){
        $(this).parent('div').remove()
    });
}

$(document).click(function(){
    var tag_value = "";
    $('.span-tag').each(function(){
        $(this).text() ? (tag_value += $(this).text() + ";") : $(this).parent().remove();
    });
    $('.span-tag').length > 4 ? $('#addTag').hide() : $('#addTag').show();
    $('#hideTags').attr('value', tag_value.substring(0,tag_value.length-1).replace(/;/g, '/'));
});

$('#addTag').click(function(event){
        event.stopPropagation();
});

$('.icon-close').click(function(event){
    $(this).parent('div').remove()
});

