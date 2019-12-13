$(document).ready(function(){
    $('#search_button_makanan').click(function(){
        console.log($('#search_makanan').val())
        $.ajax({
            method: "GET",
            url: "https://pesenin2.herokuapp.com/merchant/show_makanan",

            success: function(data){
                console.log(data)
                $("#makanan").empty()
                $.each(data, function(i, item){
                    console.log(item.nama)
                    var nama = item.nama
                    if(nama.toLowerCase() == $('#search_makanan').val().toLowerCase()){
                        $('#makanan').append(
                            '<div class="text-center mt-3 mx-3" style="width: 250px;height: auto;">' +
                                '<a href="/merchant/makanan/'+(i+1)+'">' +
                                    '<img class="rounded-circle" src="' + item.foto + '" style="object-fit: contain;" width="100%" height="100%">' +
                                '</a>' +
                            '</div>'
                        )
                    }
                });
            }
        })
    })
})
