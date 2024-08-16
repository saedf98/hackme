"use strict";
(function () {
    var e = $(".select2"),
        a = $(".selectpicker"),
        i = document.querySelector("#wizard-validation");
    if (null !== i) {
        var t = i.querySelector("#wizard-validation-form");
        var courseTopicQuizzes = t.querySelectorAll('[id^="course_topic_quiz_"]'),
            r = [].slice.call(t.querySelectorAll(".btn-next")),
            p = [].slice.call(t.querySelectorAll(".btn-prev")),
            validationMessage = document.getElementById("validation-message");
        const l = new Stepper(i, { linear: !0 });

        // Quiz validation
        function validateQuiz(currentIndex) {
            var quizDiv = courseTopicQuizzes[currentIndex];
            var radios = quizDiv.querySelectorAll('input[type="radio"]');
            for (var i = 0; i < radios.length; i++) {
                if (radios[i].checked) {
                    validationMessage.classList.add("d-none");
                    validationMessage.classList.remove("d-block");
                    return true;
                  }
              }
            validationMessage.classList.remove("d-none");
            validationMessage.classList.add("d-block");
            return false;
        }

        r.forEach((btnNext) => {
            btnNext.addEventListener("click", (e) => {
                var currentIndex = l._currentIndex;
                if ((currentIndex + 1) < courseTopicQuizzes.length) {
                    if (validateQuiz(currentIndex)) {
                        l.next();
                    } else {
                        e.preventDefault();
                        e.stopPropagation();
                        // console.log(currentIndex + 1)
                        l.to(currentIndex + 1);
                    }
                } else {
                    // Assuming 's' is the FormValidation instance for the final step
                    s.validate();
                }
            });
        });

        p.forEach((btnPrev) => {
            btnPrev.addEventListener("click", (e) => {
                if (l._currentIndex > 0) {
                    l.previous();
                }
            });
        });

        // Handle form submission
        t.addEventListener("submit", (e) => {
          e.preventDefault();
          var currentIndex = courseTopicQuizzes.length - 1;
          if (!validateQuiz(currentIndex)) {
              return;
          }

          // alert("Submitted..!!");
          var formDataArray = [];
          var formData = new FormData(e.target);

          formData.forEach((value, key) => {
              formDataArray.push({ [key]: value });
          });

          // Here you can send formDataArray to the server
          console.log(formDataArray);

          Swal.fire({
            title: "Are you sure?",
            text: "Validate you've selected all answers!",
            icon: "warning",
            showCancelButton: true,
            confirmButtonColor: "#3085d6",
            cancelButtonColor: "#d33",
            confirmButtonText: "Submit!"
          }).then((result) => {
            if (result.isConfirmed) {

              fetch("/user/course-topic-quiz/submit", {
                  method: "POST",
                  headers: {
                      "Content-Type": "application/json",
                      'X-CSRFToken': getCookie('csrftoken')
                  },
                  body: JSON.stringify(formDataArray)
              })
              .then(response => response.json())
              .then(data => {
                  console.log("Success:", data);
                  Swal.fire({
                    title: "Success!",
                    text: data.message,
                    icon: "success"
                  });

                  setTimeout(() => {
                    location.reload()
                  },5000);
              })
              .catch(error => {
                  console.error("Error:", error);
                  Swal.fire({
                    title: "Oops...!",
                    text: data.message,
                    icon: "error"
                  });
                  // Handle error - maybe show an error message
              });
            }
          })

        });

        function getCookie(name) {
          let cookieValue = null;
          if (document.cookie && document.cookie !== '') {
              const cookies = document.cookie.split(';');
              for (let i = 0; i < cookies.length; i++) {
                  const cookie = cookies[i].trim();
                  if (cookie.substring(0, name.length + 1) === (name + '=')) {
                      cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                      break;
                  }
              }
          }
          return cookieValue;
      }

    }

})();
