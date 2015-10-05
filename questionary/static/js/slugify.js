django.jQuery(document).ready(function(){
    django.jQuery('.dynamic-attribute_set .field-slug input').each(function(i){
        initSlugify(django.jQuery(this).attr('id'));
    });

});

function initSlugify(slug_id){
    var field;
    field = {
        id: '#'+slug_id,
        dependency_ids: [],
        dependency_list: [],
        maxLength: 50
    };

    $('.empty-form .form-row .field-slug, .empty-form.form-row .field-slug').addClass('prepopulated_field');
    field['dependency_ids'].push('#'+slug_id.replace('-slug','-name'));
    field['dependency_list'].push('name');

    django.jQuery(field.id).data('dependency_list', field['dependency_list'])
               .prepopulate(field['dependency_ids'], field.maxLength);
}