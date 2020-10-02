$(function () {

    var saveForm = function () {

        var form = $(this);
        var formData = new FormData(this);

        $('#modal-include button[type="submit"]').attr('disabled', true);

        $.ajax({
            url: form.attr("action"),
            data: formData,
            type: form.attr("method"),
            success: function (data) {
                if (data.form_is_valid) {
                    $("#table").DataTable().ajax.reload();
                    $("#modal-include .modal-content").html('');
                    $("#modal-include").modal("hide");
                } else {
                    $("#modal-include .modal-content").html(data.html_form);
                }
            },
            error: function (error) {
                console.log(error);
            },
            cache: false,
            contentType: false,
            processData: false
        });
        return false;
    };

    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
            },
            success: function (data) {
                $("#modal-include .modal-content").html(data.html_form);
                $("#modal-include").modal("show");
            }
        });
    };

    // Open Modal and Save - Company
    $(".js-new").click(loadForm);
    $("#modal-include").on('submit', '.js-new-form', saveForm);

    // Open Modal and Edit - Company
    $("#table").on("click", ".js-edit", loadForm);
    $("#modal-include").on('submit', '.js-edit-form', saveForm);

/*
            // Deletar
            $("#tabela-curso").on("click", ".js-deletar-curso", loadForm);
            $("#modal-curso").on('submit', '.js-curso-deletar-form', saveForm);*/


});


$(document).ready(function () {
    $('#table').DataTable({
        "scrollX": true,
        "language": {
            "url": "/static/vendor/datatable/Portuguese-Brasil.json"
        },
        "ajax": {
            "processing": true,
            "url": $("#table").attr('data-url'),
            "dataSrc": ""
        },
        order: [[0, "asc"]],
        columns: [
            {data: "name"},
            {data: "legal_number"},
        ],
        columnDefs: [
            {
                className: "dt-center", targets: []
            }
        ],
        //Edit company on click
        createdRow: function (row, data, dataIndex) {
            $(row).css({'cursor': 'pointer'});
            $(row).attr({'data-url': '/company/' + data.id});
            $(row).addClass('js-edit');
        }
    });
});