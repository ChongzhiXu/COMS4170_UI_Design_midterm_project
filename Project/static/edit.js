function displayInfo() {
    // $(".name").append(item["name"]);
    // $("#edit").prop("href", "/edit/" + item["id"])
    $("#title").append(item["name"]);
    $("#image").append("<img src='" + item["img"] + "' width='210' height='200' class='image'/>")

    $("#form-attack").append("<input type='number' min='0' max='99' class='form-control' id='input-attack' placeholder='#attack value 0~99'" + " value='"+ item["attack"]+ "' required></input>");
    $("#form-durability").append("<input type='number' min='0' max='99' class='form-control' id='input-durability' placeholder='#durability value 0~99'" + " value='"+ item["durability"]+ "' required></input>");
    $("#form-location").append("<input type='text' class='form-control' id='input-location' placeholder='#location' value='"+ item["location"]+ "' required></input>");

    // $("#form-image").append("<input type='url' class='form-control' id='input-image' placeholder='#url'" + " value='"+ item["img"]+ "' required></input>")
    $("#form-summary").append("<input class='form-control' id='input-summary' placeholder='#summary'" + " value='"+ item["summary"]+ "' required></input>");
    $("#form-description").append("<textarea class='form-control' id='input-description' rows='3' placeholder='#description' required>"+ item["description"] + "</textarea>");
}

function check_input(name, comment) {
    var valid = true

    if (name == "") {
        var warning = $("<div class='warning'>Please fill name</div>")
        $("#name-warning").append(warning)
        valid = false
    } else if (name.replace(/\s+/g, "").length == 0) {
        var warning = $("<div class='warning'>Invalid spaces</div>")
        $("#name-warning").append(warning)
        valid = false
    }
    if (comment == "") {
        var warning = $("<div class='warning'>Please fill comment</div>")
        $("#comment-warning").append(warning)
        valid = false
    } else if (name.replace(/\s+/g, "").length == 0) {
        var warning = $("<div class='warning'>Invalid spaces</div>")
        $("#comment-warning").append(warning)
        valid = false
    }
    return valid
}

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
    
    if (val.length == 0) {
        $(input_s).addClass("is-invalid")
        $(parent_s).append(get_feedback("Please provide a " + name + "."))
        valid = false;
    } else if (val.replace(/\s+/g, "").length == 0) {
        $(input_s).addClass("is-invalid")
        $(parent_s).append(get_feedback("Invalid spaces."))
        valid = false
    }
    return valid
}

function validate_int(input_s, parent_s, name) {
    var val = $(input_s).val()
    var valid = true
    
    if (val.length == 0) {
        $(input_s).addClass("is-invalid")
        $(parent_s).append(get_feedback("Please provide a " + name + " value."))
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
        valid = false
    }
    return valid
}

function validate_inputs() {
    var valid = true

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

    // validate summary text box
    if (!validate_string("#input-summary", "#form-summary", "summary")) {
        valid = false
    }
    
    // validate description text box
    if (!validate_string("#input-description", "#form-description", "description")) {
        valid = false
    }

    console.log(valid)
    return valid
}

$(document).ready(function () {
    
    displayInfo()
    console.log(item)
    $('.alert').hide()

    $("#new-form").submit(function(event) {
        event.preventDefault()

        console.log("submit");
        
        $(".form-control").removeClass("is-invalid")
        $(".invalid-feedback").remove()
        var valid = validate_inputs()
        console.log(valid);

        if (valid) {
            var item_1 = {
                // The trim() method removes whitespace from both ends of a string and returns a new string, without modifying the original string.
                "name": item["name"],
                "img": item["img"],
                "attack": $("#input-attack").val().trim(),
                "durability": $("#input-durability").val().trim(),
                "summary": $("#input-summary").val().trim(),
                "description":$("#input-description").val().trim(),
                "reviews": [
                    {
                        "marked_as deleted": false,
                        "player": item["reviews"][0]["player"],
                        "comment": item["reviews"][0]["comment"]
                    }
                ],
                "location":$("#input-location").val().trim()
            }

            $.ajax({
                type: "POST",
                url: "/delete",
                dataType : "json",
                contentType: "application/json; charset=utf-8",
                data: JSON.stringify(id),
                success: function (response) {
                    console.log("deleted");
                },
                error: function(request, status, error){
                console.log("Error");
                console.log(request)
                console.log(status)
                console.log(error)
                }
            });

            $.ajax({
                type: "POST",
                url: "/add_item",
                dataType : "json",
                contentType: "application/json; charset=utf-8",
                data: JSON.stringify(item_1),
                success: function (response) {
                    console.log("success");
                    console.log(response)
                    $("#success-notification").empty()
                    // window.location.href = "http://127.0.0.1:5000/edit/" + item["id"]
                    $('.alert').show()

                    $("#success-notification").html("New weapon successfully created. <a href='http://127.0.0.1:5000/" + response["url"] + "'>Go to weapon page you just modified!!</a>")
                    $(".form-control").val("")
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
            window.location.href = "http://127.0.0.1:5000/view/" + item["id"];
        } 
        else{
            window.location.href = "http://127.0.0.1:5000/edit/" + item["id"];
        }
    });
});