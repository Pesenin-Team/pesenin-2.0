$(document).ready(() => {

    $('#searchForm').on('submit', (e) => {
        let searchText = $('#searchText').val();
        searchQuery(searchText);
        e.preventDefault();
    });

    $('#submit').on('click', (e) => {
        let searchText = $('#searchText').val();
        searchQuery(searchText);
        e.preventDefault();
    })

    getQueue();
})


function getQueue() {
    $.ajax("https://pesenin2.herokuapp.com/queue/get_queue")
        .done(response => {
            let query = 'default'
            printToSite(response, query);
        })
        .fail((xhr, status) => console.log("error: ", status));
}

function searchQuery(query) {
    $.ajax("https://pesenin2.herokuapp.com/queue/get_queue")
        .done(response => {
            printToSite(response, query);
        })
        .fail((xhr, status) => console.log("error: ", status));
}

function printToSite(request, query) {
    let queue = request
    output = ``
    if (query === 'default') {
        $.each(queue, (index, queue) => {
            console.log(queue);
            output += `
            <div class="card kartu mt-3">
                <div class="card-header">
                    <strong>A60</strong>
                </div>
                <div class="card-body">
                    <div class="row">
                        <div class="col-2">
                            <div class="foodicon">
                                <img src="${queue.foto}" alt="" class="rounded-circle">
                            </div>
                        </div>
                        <div class="col-10 pt-3">
                            <h5 class="card-title">${queue.nama_makanan}</h5>
                            <p class="card-text text-danger">${queue.status}</p>
                        </div>
                    </div>
                </div>
            </div>
            `
        })
    }
    else {
        $.each(queue, (index, queue) => {
            if (query.toLowerCase() === queue.nama_makanan.toLowerCase()) {
                console.log("a")
                output += `
            <div class="card kartu mt-3">
                <div class="card-header">
                    <strong>A60</strong>
                </div>
                <div class="card-body">
                    <div class="row">
                        <div class="col-2">
                            <div class="foodicon">
                                <img src="${queue.foto}" alt="" class="rounded-circle">
                            </div>
                        </div>
                        <div class="col-10 pt-3">
                            <h5 class="card-title">${queue.nama_makanan}</h5>
                            <p class="card-text text-danger">${queue.status}</p>
                        </div>
                    </div>
                </div>
            </div>
            `
            }
        })
        output += `
        <a onClick=getQueue() class="btn btn-danger btn-lg active mt-5" role="button"
            aria-pressed="true">Back</a
        `
    }
    $('#antrian').html(output)
}

function deleteAntrian() {
    $('#antrian').empty()
}