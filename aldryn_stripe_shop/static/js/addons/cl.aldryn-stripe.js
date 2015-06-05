'use strict';
// #####################################################################################################################
// #NAMESPACES#
/**
 * @module Cl
 */
// istanbul ignore next
var Cl = window.Cl || {};

// #####################################################################################################################
// #UTILS#
(function ($) {
    'use strict';

    /**
     * Contains various helpers, feel free to extend and adapt
     *
     * @class Utils
     * @namespace Cl
     */
    Cl.AldrynStripe = new Class({


        initialize: function (options) {

            this.handler = StripeCheckout.configure(options)
            this.options = options

        },

        setData: function (options) {
            $.extend(true, this.options, options);
        },

        checkoutStripe: function () {
            this.handler.open(this.options);
        }
    });

})(jQuery);
