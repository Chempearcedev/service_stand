  $(document).ready(function(){
    $('.sidenav').sidenav();
     $('.tooltipped').tooltip();
     $(".datepicker").datepicker({
        format: "dd mm, yyyy",
        yearRange: 2,
        showClearBtn: true,
        i18n: {
            done: "Select"
        }
    });
  });