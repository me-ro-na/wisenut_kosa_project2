$(document).ready(function(){
    $("#sec1-err").hide()
    let output = [];
    $("input:checkbox[name='cats']:checked").each(function(index, item) {
        output.push($(this).val())
    });
    chg_img(output);

    $("input[name='cats']").click(function(e){
        let now = $(this).attr("id");
        if($(this).is(":checked")) {
            $("input:checkbox[id=" + now + "]").attr("checked", true)
        } else {
            $("input:checkbox[id=" + now + "]").attr("checked", false)
        }
        output = [];
        $("input:checkbox[name='cats']:checked").each(function(index, item) {
                output.push($(this).val())
        });
        chg_img(output);
    });
});

function chg_img(cats) {
    url = "/chart3_sec1?cats=" + [cats];
    if(cats.length == 0) {
        $("#sec1-err").show()
        $("#sec1").attr("src", "");
    } else {
        $("#sec1").attr("src", url);
        $("#sec1-err").hide();
    }
}