(function($) {
    var HL_BLOCKS_SELECTOR = '.highlight-block',
        HL_CONTAINER_SELECTOR = '.highlights',
        HL_AREA_SELECTOR = '.highlight-area';

    $(document).ready(function() {
        var $highlights = $(HL_CONTAINER_SELECTOR),
            $areas = $(HL_AREA_SELECTOR),
            watchFields = [];

        $areas.hide();

        setTimeout(function() {
            var topOffset = $highlights.offset().top;

            $areas.each(function() {
                var $area = $(this),
                    $field,
                    parts = $area.data('linked-to').split(','),
                    link = parts[0];

                if (link) {
                    $field = $('#id_' + link);
                    //console.log($area.offset().top - topOffset);
                    //console.log($field, $field.offset().top - topOffset);

                    $area
                    .css({
                        position: 'absolute',
                        left: 0,
                        right: 30,
                        top: $field.offset().top - topOffset,
                        opacity: 0
                    })
                    .show()

                    watchFields.push({
                        $el: $field,
                        $area: $area,
                        top: $field.offset().top,
                        height: $field.outerHeight()
                    });
                }

                $field.on('focus', function() {
                    $("html,body").animate({
                        scrollTop: ($(this).offset().top + $(this).outerHeight() / 2) - (window.innerHeight / 2)
                    }, 300);
                    $field.attr('focused', 1);
                });

                if (parts.length == 5) {
                    var $hover = $(),
                        focusFlag = false;

                    $field
                    .on('mouseenter', function(e) {
                        $hover = $area.find('.highlight-zone');
                        if (! $hover.length) {
                            $hover = $(document.createElement('div'));
                            $hover
                            .addClass('highlight-zone')
                            .appendTo($area);
                        }

                        $hover
                        .css({
                            top: parts[2] + "%",
                            left: parts[1] + "%",
                            width: parts[3] + "%",
                            height: parts[4] + "%"
                        })
                        setTimeout(function() {
                            $hover.addClass('active');
                        }, 0)
                    })
                    .on('mouseleave', function(e) {
                        if (! $field.attr('focused')) {
                            $hover.removeClass('active');
                            $field.removeAttr('focused');
                        }
                    })
                    .on('blur', function() {
                        $hover.removeClass('active');
                        $field.removeAttr('focused');
                    });
                }
            })
        }, 1000);

        var minVisiblePercentage = 25,
            totallyVisiblePercentage = 15,
            maxPositionDelta = 200

        $(window).scroll(function() {
            var scrollTop = $(window).scrollTop(),
                height = window.innerHeight,
                i, field, fieldCenter, o, pos, percentage;

            for (i in watchFields) {
                field = watchFields[i];
                fieldCenter = (field.top + field.height / 2);
                percentage = (fieldCenter - scrollTop) / height * 100;
                centerDistance = percentage - 50;
                absCenterDistance = Math.abs(centerDistance);
                interval = (minVisiblePercentage - totallyVisiblePercentage);

                if (absCenterDistance < totallyVisiblePercentage) {
                    field.$area.css({
                        opacity: 1,
                        marginTop: 0
                    });
                } else if (absCenterDistance < minVisiblePercentage) {
                    if (centerDistance > 0) {
                        o = (interval - (centerDistance - totallyVisiblePercentage)) / interval;
                        pos = maxPositionDelta * (1 - o);
                    } else {
                        o = (interval + centerDistance + totallyVisiblePercentage) / interval;
                        pos = maxPositionDelta * -1 * (1 - o);
                    }
                    field.$area.css({
                        opacity: o,
                        marginTop: pos
                    });
                } else {
                    field.$area.css({
                        opacity: 0
                    });
                }
            }
        })
    })
})(window.$)
