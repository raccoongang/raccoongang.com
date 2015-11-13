(function($) {
    var HL_BLOCKS_SELECTOR = '.highlight-block',
        HL_CONTAINER_SELECTOR = '.highlights';

    $(document).ready(function() {
        $highlights = $(HL_CONTAINER_SELECTOR);

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
