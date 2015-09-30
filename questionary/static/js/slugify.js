(function($) {
    var field;


    field = {
        id: '#id_attribute_set-0-slug',
        dependency_ids: [],
        dependency_list: [],
        maxLength: 50
    };

    
    field['dependency_ids'].push('#id_attribute_set-0-name');
    field['dependency_list'].push('name');
    

    console.log(field);
    $('.form-row.field-slug').addClass('prepopulated_field');
    $(field.id).data('dependency_list', field['dependency_list'])
               .prepopulate(field['dependency_ids'], field.maxLength);

})(django.jQuery);