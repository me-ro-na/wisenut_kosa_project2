$(document).ready(function(){
    $("#sec1").attr("src", "/chart6_sec1");
    let addr1 = $('#addr1').val();
    $("#sec2").attr("src", "/chart6_sec2?loc=ADDR1&addr=" + addr1);

    $('#addr1').on('select2:selecting', function(e) {
        addr1 = e.params.args.data.text;
        get_addr2(addr1);
        $("#sec2").attr("src", "/chart6_sec2?loc=ADDR1&addr=" + addr1);
    });
    $('#addr2').on('select2:selecting', function(e) {
        addr2 = e.params.args.data.text;
        if(addr2 == "전체") {
            $("#sec2").attr("src", "/chart6_sec2?loc=ADDR1&addr=" + addr1);
        } else {
            $("#sec2").attr("src", "/chart6_sec2?loc=ADDR2&addr=" + addr2);
        }
    });
});

function get_addr2(addr1) {
    $.ajax({
        url: "/get_addr2",
        type: "get",
        data: {"addr1": addr1},
        success: function(data) {
            addr2List = data.addr2;
            optLen = $("#addr2").find("option").length;

            $('#addr2').val(null).trigger('change');
            $('#addr2').html('').select2({data: [{value: '', id: '', text: '전체'}]});

            for(var i=0; i<addr2List.length; i++) {
                if ($('#addr2').find("option[value='" + addr2List[i] + "']").length) {
                    $('#addr2').val(addr2List[i]).trigger('change');
                } else { 
                    var newOption = new Option(addr2List[i], addr2List[i], true, false);
                    $('#addr2').append(newOption).trigger('change');
                } 
            }
        }
    });
}
