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

function validate_inputs() {

    var valid = true

    // validate name
    if (!validate_string("#input-username", "#form-username", "username")) {
        valid = false
    }

    // validate comment
    if (!validate_string("#input-comment", "#form-comment", "comment")) {
        valid = false
    }

    return valid
}


$(document).ready(function () {

    var id_1 = id
    var name = item["name"]
    // var location_link = $("<a href='search" + id + "'></a>")
    // var image = $("<img src='" + item["img"] + "' alt='" + name + "'>")
    $("#image").append("<img src='" + item["img"] + "' class='weapon-image rounded mx-auto d-block img-thumbnail' alt='" + name + "'>");

    $("#title").html(name)

    $("#attack").children().append(item["attack"]);
    $("#durability").children().append(item["durability"]);
    $("#location").children().append(item["location"]);

    $('#locationSearch').click(function(e){
        window.location.href = "http://127.0.0.1:5000/search/" + item["location"]
    })
    $("#locationSearch").hover(
        function() {
            $(this).addClass("when_hover")
        },
        function() {
            $(this).removeClass("when_hover")
        }
    )
    // $("#location").children().append("<a href:'/search/" + item["location"] + "'>" + item["location"] + "</a>");
    $("#edit-button").append("<a class='col-md-12' href='/edit/" + id_1 + "'>Edit this pedia, click here!</a>")
    // $("#jump-button").append("<a class='col-md-12' href='/search/" + item["location"] + "'>Search weapons in same location, click here!</a>")


    $("#summary").append(item["summary"]);
    $("#description").append(item["description"]);

    $.each(item["reviews"], function (index, item) { 
        console.log(item);
        
        if (!item["marked_as_deleted"]) {
            console.log("logged");
            
            $("#review-section" + index).removeClass("d-none")
            $("#user" + index).append(item["player"])
            $("#comment" + index).append(item["comment"])
        }
    });

    $(".delete-button").click(function(e) {
        var comment_id = $(this).parent().prop("id")
        data = {
            "weapon_id": item["id"],
            "comment_id": comment_id
        }
        
        $.ajax({
            type: "POST",
            url: "/delete_review",
            dataType : "json",
            contentType: "application/json; charset=utf-8",
            data: JSON.stringify(data),
            success: function (response) {
                console.log("deleted");
                
                $("#" + comment_id).children().eq(0).children().addClass("d-none")
                $("#" + comment_id).children().eq(1).removeClass("d-none")
                
                $(".user-name").eq(comment_id).addClass("deleted")
                $(".user-comment").eq(comment_id).addClass("deleted")

                $("#" + comment_id).children().eq(1).click(function(e) {
                    $.ajax({
                        type: "POST",
                        url: "/recover_review",
                        dataType : "json",
                        contentType: "application/json; charset=utf-8",
                        data: JSON.stringify(data),
                        success: function (response) {
                            console.log("recovered");
                            $("#" + comment_id).children().eq(0).children().removeClass("d-none")
                            $("#" + comment_id).children().eq(1).addClass("d-none")
                            $(".user-name").eq(comment_id).removeClass("deleted")
                            $(".user-comment").eq(comment_id).removeClass("deleted")
                        }
                    });
                })
            }
        });
    })

    $("#add-button").click(function (e) { 
        $("#add-button").addClass("d-none")
        $("form").removeClass("d-none")
        $("#input-username").focus()

        $("#discard-button").click(function(e) {
            let confirmAction = confirm("Are you sure to execute this action?");
            if (confirmAction) {
                $("#form-username").val("");
                $("#form-comment").val("");
                $("#add-button").removeClass("d-none");
                $("form").addClass("d-none");
            }
        })

        $("#comment-form").submit(function(event) {
            
            event.preventDefault()

            console.log("submit");

            $(".invalid-feedback").remove()
            var valid = validate_inputs()
            console.log(valid);

            if (valid) {
                var new_review = {
                    "id": item["id"],
                    "player": $("#input-username").val().trim(),
                    "comment": $("#input-comment").val().trim()
                }
                console.log(new_review);
                

                $.ajax({
                    type: "POST",
                    url: "/add_review",
                    dataType : "json",
                    contentType: "application/json; charset=utf-8",
                    data: JSON.stringify(new_review),
                    success: function (response) {
                        window.location.href = "http://127.0.0.1:5000/view/" + item["id"]
                    }
                });
            }
        })

    });
});