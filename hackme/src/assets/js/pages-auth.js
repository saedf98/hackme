"use strict";
const formAuthentication = document.querySelector("#formAuthentication");
const formLogin = document.querySelector("#formLogin");
document.addEventListener("DOMContentLoaded", function (e) {
    var t;
    formAuthentication &&
        FormValidation.formValidation(formAuthentication, {
            fields: {
                username: { validators: { notEmpty: { message: "Please enter username" }, stringLength: { min: 2, message: "Username must be more than 2 characters" } } },
                // first_name: { validators: { notEmpty: { message: "Please enter first name" }, stringLength: { min: 2, message: "First name must be more than 2 characters" } } },
                // last_name: { validators: { notEmpty: { message: "Please enter last name" }, stringLength: { min: 2, message: "Last name must be more than 2 characters" } } },
                email: { validators: { notEmpty: { message: "Please enter your email" }, emailAddress: { message: "Please enter valid email address" } } },
                "email-username": { validators: { notEmpty: { message: "Please enter email / username" }, stringLength: { min: 6, message: "Username must be more than 6 characters" } } },
                password: { validators: { notEmpty: { message: "Please enter your password" }, stringLength: { min: 8, message: "Password must be more than 8 characters" } } },
                studentship_status: { validators:{ notEmpty: { message: "The studentship status is required"} } },
                phone_number_one: { validators:{ notEmpty: { message: "The phone number is required"} } },
                password_confirmation: {
                    validators: {
                        notEmpty: { message: "Please confirm password" },
                        identical: {
                            compare: function () {
                                return formAuthentication.querySelector('[name="password"]').value;
                            },
                            message: "The password and its confirm are not the same",
                        },
                        stringLength: { min: 6, message: "Password must be more than 6 characters" },
                    },
                },
                terms: { validators: { notEmpty: { message: "Please agree terms & conditions" } } },
            },
            plugins: {
                trigger: new FormValidation.plugins.Trigger(),
                bootstrap5: new FormValidation.plugins.Bootstrap5({ eleValidClass: "", rowSelector: ".mb-3" }),
                submitButton: new FormValidation.plugins.SubmitButton(),
                defaultSubmit: new FormValidation.plugins.DefaultSubmit(),
                autoFocus: new FormValidation.plugins.AutoFocus(),
            },
            init: (e) => {
                e.on("plugins.message.placed", function (e) {
                    e.element.parentElement.classList.contains("input-group") && e.element.parentElement.insertAdjacentElement("afterend", e.messageElement);
                });
            },
        }),
        (t = document.querySelectorAll(".numeral-mask")).length &&
            t.forEach((e) => {
                new Cleave(e, { numeral: !0 });
        }),
        formLogin &&
        FormValidation.formValidation(formLogin, {
            fields: {
                username: { validators: { notEmpty: { message: "Please enter your username" }, stringLength: { min: 2, message: "Username must be more than 2 characters" } } },
                password: { validators: { notEmpty: { message: "Please enter your password" }, stringLength: { min: 4, message: "Password must be more than 4 characters" } } },
            },
            plugins: {
                trigger: new FormValidation.plugins.Trigger(),
                bootstrap5: new FormValidation.plugins.Bootstrap5({ eleValidClass: "", rowSelector: ".mb-3" }),
                submitButton: new FormValidation.plugins.SubmitButton(),
                defaultSubmit: new FormValidation.plugins.DefaultSubmit(),
                autoFocus: new FormValidation.plugins.AutoFocus(),
            },
            init: (e) => {
                e.on("plugins.message.placed", function (e) {
                    e.element.parentElement.classList.contains("input-group") && e.element.parentElement.insertAdjacentElement("afterend", e.messageElement);
                });
            },
        });
});
