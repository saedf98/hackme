"use strict";
$(function () {
    var e = $(".select2");
    e.length &&
        (e.each(function () {
            var e = $(this);
            e.wrap('<div class="position-relative"></div>').select2({ dropdownParent: e.parent(), placeholder: e.data("placeholder"), dropdownCss: { minWidth: "150px" } });
        }),
        $(".select2-selection__rendered").addClass("w-px-150"));
        e.on('change', function() {
          var selectedOption = $(this).find('option:selected');
          var url = selectedOption.data('url');
          var type = selectedOption.data('type');
          if (url) {
            var search = document.getElementById('search').value
            const level_param = document.getElementById('level_param').value;
            const filter_param = document.getElementById('filter_param').value;
              if(search){
                url = url+`&search=${search}&`
              }
              if(type == "level"){
                if(filter_param){
                  // alert(level_param)
                  url = url+`&filter=${filter_param}`
                }
              }else{
                if(level_param && level_param != 0){
                  url = url+`&level=${level_param}`
                }
              }
              window.location.href = url;
          }
      });
}),
(function () {
  document.addEventListener('DOMContentLoaded', (event) => {
    const level_param = document.getElementById('level_param').value;
    const search_param = document.getElementById('search_param').value;
    const filter_param = document.getElementById('filter_param').value;
    let filter_url = document.getElementById('filter_url').value;

    const completedCards = document.querySelectorAll('.completed');
    const hideCompletedRadio = document.getElementById('hideCompleted');

    hideCompletedRadio.addEventListener('change', () => {
      if (hideCompletedRadio.checked) {
        completedCards.forEach(card => {
          card.classList.add('d-none');
        });
      }else{
        completedCards.forEach(card => {
          card.classList.remove('d-none');
        });
      }
    });

    document.getElementById('search-courses').addEventListener('click', () => {
      var search = document.getElementById('search').value
      if (search) {
        if(search_param || search){
          search = search ?? search_param;
          filter_url = filter_url+`search=${search}&`
        }
        if(filter_param){
          filter_url = filter_url+`filter=${filter_param}&`
        }
        if(level_param && level_param != 0){
          filter_url = filter_url+`level=${level_param}&`
        }
        window.location.href = filter_url;
      }

    })

  })
})(),
(function () {
    new Plyr("#guitar-video-player"), new Plyr("#guitar-video-player-2");
    (document.getElementsByClassName("plyr")[0].style.borderRadius = "4px"),
        (document.getElementsByClassName("plyr")[1].style.borderRadius = "4px"),
        (document.getElementsByClassName("plyr__poster")[0].style.display = "none"),
        (document.getElementsByClassName("plyr__poster")[1].style.display = "none");
})();
