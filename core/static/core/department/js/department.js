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
            success: function (data) {
                $("#modal-include .modal-content").html(data.html_form);
                $("#modal-include").modal("show");
            }
        });
    };

    var deleteForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            success: function (data) {
                if (data.html_alert) {
                    $("#alert-modal").html(data.html_alert);
                    $("#modal-confirm").modal("show");
                } else {
                    $("#table").DataTable().ajax.reload();
                    $("#modal-include .modal-content").html('');
                    $("#modal-include").modal("hide");
                }
            }
        });
    };

    /**
     *
     * Implementation coming soon
     *
    var current_form;
    var loadConfirm = function () {
        current_form = this;
        $("#modal-confirm .modal-content").html(data.html_form);
        $("#modal-confirm").modal("show");
        return false;
    };
     **/

    // Open Modal and Save - Company
    $(".js-new").click(loadForm);
    $("#modal-include").on('submit', '.js-new-form', saveForm);

    // Open Modal and Edit - Company
    $("#table").on("click", ".js-edit", loadForm);
    $("#modal-include").on('submit', '.js-edit-form', saveForm);

    // Delete - Company
    $("#modal-include").on('click', '.js-delete', deleteForm);

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
            {
                data: "status", searchable: false, orderable: false,
                render: function (data, type, row) {
                    return '<i class="' + (data ? 'text-success': 'text-danger') + ' small fas fa-circle"></i>';
                }
            },
            {data: "name"},
            {data: "admin"},
        ],
        columnDefs: [
            {
                className: "dt-center", targets: [0]
            }
        ],
        //Edit company clicking on roll
        createdRow: function (row, data, dataIndex) {
            $(row).css({'cursor': 'pointer'});
            $(row).attr({'data-url': '/company/department/' + data.id});
            $(row).addClass('js-edit');
        }
    });
});