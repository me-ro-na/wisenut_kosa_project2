$(document).ready(function(){
    chg_img();
    $("input[name='wants']").click(function(){
        chg_img();
    })
})

function chg_img() { 
    want = new Array();
    url = "/chart1_sec1?wants={";
    $("input[name='wants']:checked").each(function(i) {
        want.push("");
        url += $(this).val();
        url += ","
    });
    url += "}";
    if(want.length == 0) {
        $("#sec1-err").show()
        $("#sec1").attr("src", "");
    } else {
        $("#sec1").attr("src", url);
        $("#sec1-err").hide()
    }
}