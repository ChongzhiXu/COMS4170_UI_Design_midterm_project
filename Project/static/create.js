function check_spaces(id) {
    var val = $("#" + id).val()
    
    if (val.replace(/\s+/g, "").length == 0) {
        return false
    } else {
        return true
    }
}

function get_feedback(feedback) {
    var template = $("<div class='invalid-feedback'></div>")
    template.html(feedback)
    return template
}

function validate_string(input_s, parent_s, name) {
    var val = $(input_s).val().trim()
    var valid = true
    // console.log(val)

    if (val.length == 0) {
        $(input_s).addClass("is-invalid")
        $(parent_s).append(get_feedback("Please insert a " + name + "."))
        // console.log(1)
        valid = false;
    } else if (val.replace(/\s+/g, "").length == 0) {
        $(input_s).addClass("is-invalid")
        $(parent_s).append(get_feedback("Invalid spaces."))
        // console.log(2)
        valid = false
    }
    return valid
}

function validate_int(input_s, parent_s, name) {
    var val = $(input_s).val()
    var valid = true
    // console.log(val)
    if (val.length == 0) {
        $(input_s).addClass("is-invalid")
        // console.log(1)
        $(parent_s).append(get_feedback("Please insert a " + name + " value."))
        // console.log(2)
        valid = false;
    } else {
        var val = Number(val)        
        
        if (val==NaN || (!Number.isInteger(val))) {
            
            $(input_s).addClass("is-invalid")
            $(parent_s).append(get_feedback("Please use integer."))
            valid = false;
        } else if (val<1 || val>99) {

            $(input_s).addClass("is-invalid")
            $(parent_s).append(get_feedback("Please use number between 1 and 99."))
            valid = false;
        }
    }
    return valid
}

function validate_image_url(input_s, parent_s) {

    var val = $(input_s).val().trim()
    var valid = true

    if (val.length == 0) {
        $(input_s).addClass("is-invalid")
        $(parent_s).append(get_feedback("Please provide a url."))
       
        valid = false;
    } else if (val.replace(/\s+/g, "").length == 0) {
        $(input_s).addClass("is-invalid")
        $(parent_s).append(get_feedback("Invalid spaces."))
        // console.log("url check")
        valid = false
    }
    return valid
}

function validate_inputs() {
    
    var valid = true

    // validate name
    name = $("#input-name").val().trim()
    var included = false
    $.each(names, function (index, name_used) {
        name_used = name_used.toLowerCase()
        if (name.toLowerCase()==name_used) {
            included = true
        }
    });
    if (included) {
        $("#input-name").addClass("is-invalid")
        $("#form-name").append(get_feedback("Name have already been used. Please type a different name."))
        valid = false;
    } else if (!validate_string("#input-name", "#form-name", "name")) {
        valid = false
    }

    // validate attack text box
    if (!validate_int("#input-attack", "#form-attack", "attack")) {
        valid = false
    }

    // validate durability text box
    if (!validate_int("#input-durability", "#form-durability", "durability")) {
        valid = false
    }

    // validate location text box
    if (!validate_string("#input-location", "#form-location", "location")) {
        valid = false
    }

    // validate image url text box
    if (!validate_image_url("#input-image", "#form-image")) {
        valid = false
    }

    // validate summary text box
    if (!validate_string("#input-summary", "#form-summary", "summary")) {
        valid = false
    }
    // console.log("validate summary")
    
    // validate description text box
    if (!validate_string("#input-description", "#form-description", "description")) {
        valid = false
    }

    // validate user name text box
    if (!validate_string("#input-username", "#form-username", "username")) {
        valid = false
    }

    // validate comment text box
    if (!validate_string("#input-comment", "#form-comment", "comment")) {
        valid = false
    }

    return valid
}

$(document).ready(function () {

    $('.alert').hide()

    $("#new-form").submit(function(event) {
        
        event.preventDefault()

        console.log("submit");
        
        $(".form-control").removeClass("is-invalid")
        $(".invalid-feedback").remove()
        var valid = validate_inputs()
        console.log(valid);

        if (valid) {
            var item = {
                "name": $("#input-name").val().trim(),
                "img": $("#input-image").val(),
                "attack": $("#input-attack").val().trim(),
                "durability": $("#input-durability").val().trim(),
                "summary": $("#input-summary").val().trim(),
                "description":$("#input-description").val().trim(),
                "reviews": [
                    {
                        "marked_as deleted": false,
                        "player": $("#input-username").val().trim(),
                        "comment": $("#input-comment").val().trim()
                    }
                ],
                "location":$("#input-location").val().trim()
            }

            $.ajax({
                type: "POST",
                url: "add_item",
                dataType : "json",
                contentType: "application/json; charset=utf-8",
                data: JSON.stringify(item),
                success: function (response) {
                    console.log("success");
                    $('.alert').show()
                    $("#success-notification").empty()
                    $("#success-notification").html("New weapon successfully created. <a href='" + response["url"] + "'>Go to weapon page you just created!!<\a>")
                    $(".form-control").val("")
                    $("#input-name").focus();
                },
                error: function(request, status, error){
                    console.log("Error");
                    console.log(request)
                    console.log(status)
                    console.log(error)
                }
            });
        } 
    })
    $("#discard-button").click(function () { 
        
        // The function below will start the confirmation dialog
        let confirmAction = confirm("Are you sure to discard editing?");
        if (confirmAction) {
            window.location.href = "http://127.0.0.1:5000/";
        } 
    });
});