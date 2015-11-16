(function($) {
    var HL_BLOCKS_SELECTOR = '.highlight-block',
        HL_CONTAINER_SELECTOR = '.highlights',
        HL_AREA_SELECTOR = '.highlight-area';

    $(document).ready(function() {
        $highlights = $(HL_CONTAINER_SELECTOR);
        $areas = $(HL_AREA_SELECTOR);
        $areas.hide();

        setTimeout(function() {
            var topOffset = $highlights.offset().top;
            $areas.each(function() {
                var $area = $(this),
                    link = $area.data('linked-to');
                if (link) {
                    var $field = $('#id_' + link);
                    console.log($area.offset().top - topOffset);
                    console.log($field, $field.offset().top - topOffset);
                    $area
                    .css({
                        position: 'absolute',
                        left: 0,
                        right: 30,
                        top: $field.offset().top - topOffset
                    })
                    .show();
                }
            })
        }, 1000);


        $(HL_BLOCKS_SELECTOR).each(function() {
            var $el = $(this);
            var $hover = $();
            $(this)
            .on('mouseenter', function(e) {
                //console.log($el.data('hl-img'));
                var zone = $el.data('hl-region').split(',');
                $('.highlight-zone').remove();
                $hover = $(document.createElement('div'));

                $hover
                .addClass('highlight-zone')
                .css({
                    top: zone[1] + "%",
                    left: zone[0] + "%",
                    width: zone[2] + "%",
                    height: zone[3] + "%"
                })
                .appendTo($($el.data('hl-img')));
                setTimeout(function() {
                    $hover.addClass('active');
                    $highlights.addClass('active');
                }, 0)
            })
            .on('mouseleave', function(e) {
                $hover.removeClass('active');
                $highlights.removeClass('active');
            });
        })
    })
})(window.$)
