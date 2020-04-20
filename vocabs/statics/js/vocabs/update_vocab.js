function saveEdits(elem_id, vocab_id) {

    var elem = document.getElementById(elem_id);
    var elem_edit = document.getElementById(elem_id + "_edit");
    var elem_sync = document.getElementById(elem_id + "_sync");

    if (elem_sync.style.display == "none") {
        elem_sync.style.display = "block";
        elem_edit.style.display = "none";
        elem.contentEditable = "true";
    } else {
        elem_sync.style.display = "none";
        elem_edit.style.display = "block";
        elem.contentEditable = "false";

        var url = "{% url 'vocabs:results_update' 0 %}".replace(/0/, vocab_id);
        console.log(url);
        window.location = url;

    }
}