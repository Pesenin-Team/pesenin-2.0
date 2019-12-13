// $(document).ready(() => {
//     $('#searchForm').on('submit', (e) => {
//         let searchText = $('#searchText').val();
//         searchText(searchText);
//         e.preventDefault();
//     });
    
//     $('#submit').on('click', (e) => {
//         let searchText = $('#searchText').val();
//         searchText(searchText);
//         e.preventDefault();
//     })
//     getMerchant();

// })
// function getMerchant(){
//     $.ajax("http://127.0.0.1:8000/restapi/merchant/?format=json")
//         .done(response => {
//             console.log(response);
//             printToSite(response);
//         })
//         .fail((xhr, status) => console.log("error: ", status));
// }

// function searchText(query){
//     $.ajax("http://127.0.0.1:8000/restapi/merchant/?format=json")
//         .done(response => {
//             console.log(response);
//             searchMerchant(response, query);
//         })
//         .fail((xhr, status) => console.log("error: ", status));
// }

// function printToSite(request) {
//     console.log(request)
//     let merchant = request
//     output = ``
//     $.each(merchant, (index, merchant) => {
//         console.log(merchant);
//         output += ` 
//         <div class="penjual mx-5 mt-3" style="width: 250px;">
//             <div class="gambar">
//                 <a href="{% url 'merchant:makanan' %}">
//                     <img class="rounded" src="${merchant.link_gambar}" style="object-fit: contain;"
//                         height="100%" width="100%">
//                 </a>
//             </div>
//         </div>
//         `
//     })
//     $('#toko').html(output)
// }

// function searchMerchant(request, query) {
//     console.log(request)
//     let merchant = request
//     $.each(merchant, (index, merchant) => {
//         console.log(merchant);
//         if(query.toLowerCase() == merchant.nama_merchant.toLowerCase()){

//             output += ` 
//             <div class="penjual mx-5 mt-3" style="width: 250px;">
//                 <div class="gambar">
//                     <a href="{% url 'merchant:makanan' %}">
//                         <img class="rounded" src="${merchant.link_gambar}" style="object-fit: contain;"
//                             height="100%" width="100%">
//                     </a>
//                 </div>
//             </div>
//             `
//         }
//     })
//     $('#toko').html(output)
// }

$(document).ready(function(){
    $('#submit').click(function(){
        console.log($('#searchText').val())
        $.ajax({
            method: "GET",
            url: "https://pesenin2.herokuapp.com/merchant/show_merchant",

            success: function(data){
                console.log(data)
                $('#toko').empty()
                $.each(data, function(i ,item){
                    console.log(item.nama_merchant)
                    if(item.nama_merchant.toLowerCase() == $('#searchText').val().toLowerCase()){
                        $('#toko').append(
                            // "<img class='rounded' src='" + item.link_gambar +"' style='object-fit: contain;' height='100%' width='100%'>"
                            "<div class='penjual mx-5 mt-3' style='width: 250px;'>" +
                                "<div class='gambar' id='gambar'>" +
                                    "<a href='/merchant/makanan' id='img'>"+
                                        "<img class='rounded' src='" +  item.link_gambar +"'style='object-fit: contain;'height='100%' width='100%'>" +
                                    "</a>" +
                                "</div>" +
                            "</div>"
                    )}
                })
            }
        })
    })
})
