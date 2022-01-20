$(document).ready(function(){
    let addr1 = $('#addr1').val();
    $("#sec1").attr("src", "/chart5_sec1?addr=" + addr1);

    $('#addr1').on('select2:selecting', function(e) {
        addr1 = e.params.args.data.text;
        $("#sec1").attr("src", "/chart5_sec1?addr=" + addr1);
    });
});