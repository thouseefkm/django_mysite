$(function () {

  $(".notes").click(function () {
    console.log("Hello")
    $.ajax({
      url: 'vocabs:results_update',
      type: 'post',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-book").modal("show");
      },
      success: function (data) {
        $("#modal-book .modal-content").html(data.html_form);
      }
    });
  });

});