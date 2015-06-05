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
    Cl.CheckOut = new Class({


        initialize: function (wrapper, stripe) {
            var that = this;
            this.stripe = stripe;

            $("input[name='amount']", wrapper).TouchSpin({
                postfix: "checkout",
                postfix_extraclass: "btn btn-primary js-checkout",
                min: 1,
                max: 10
            });

            this.blocks = {
                            amount: $("input[name='amount']", wrapper),
                            pay: $(".js-checkout", wrapper),
                            stripe: $('.stripe-button', wrapper),
                            stripeTriggerButton: $('.js-aldryn-stripe'),
                            touchspinUp: $('.bootstrap-touchspin-up', wrapper),
                            touchspinDown: $('.bootstrap-touchspin-down', wrapper),
                            priceShown: $('.js-aldryn-stripe-price', wrapper),
                            productName: $('.js-aldryn-stripe-title', wrapper),
                            productImage: $('.js-aldryn-stripe-image', wrapper),
                            productDescription: $('.js-aldryn-stripe-description', wrapper)
                        };

            var basicPrice = this.blocks.priceShown.text();
            //counter of the amount of specific product

            that.blocks.touchspinUp.on('click', function () {
                var number = that.blocks.touchspinUp.parent().siblings('input').val();
                var displayPrice = parseInt(basicPrice, 10) * parseInt(number, 10);
                var price = String(displayPrice);

                that.blocks.priceShown.text(price);
            });

            that.blocks.touchspinDown.on('click', function () {
                var number = that.blocks.touchspinDown.parent().siblings('input').val();
                var displayPrice = parseInt(basicPrice, 10) * parseInt(number, 10);
                var price = String(displayPrice);

                that.blocks.priceShown.text(price);
            });

            that.blocks.pay.on('click', function() {
                var price = that.blocks.priceShown.text();
                var priceToCents = price + "00";
                var getProductName = that.blocks.productName.text();
                var getProductImage = that.blocks.productImage.src;
                var getProductDescription = that.blocks.productDescription.text();
                that.stripe.setData({
                    amount: priceToCents,
                    name: getProductName,
                    image: getProductImage,
                    description: getProductDescription
                    });
                that.triggerStripe();
            });
        },

        triggerStripe: function () {
            this.stripe.checkoutStripe();
        }
    });

})(jQuery);
