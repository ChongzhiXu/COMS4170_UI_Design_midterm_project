function make_card(index, item) {
    
    //define the image bubble in columns
    var block = $("<div class='col-md-4 result-item'></div>")
    //make the card with view block
    var card = $("<div class='card-example card bg-light'></div>")
    //display the image of weapon in the card and link
    var image_link = $("<a href='/view/" + item["id"] + "'></a>")
    var card_img = $("<img class='card-img-top' src='" + item["img"] + "' alt='" + item["name"] + "'>")
    image_link.html(card_img)
    card.append(image_link)

    var card_body = $("<div class='card-body'>")
    var title = $("<h4 class='card-title'></h4>")
    title.html(item["name"])
    card_body.append(title)

    var card_summary = $("<p class='card-text block-with-text'></p>")
    card_summary.html(item["summary"])
    card_body.append(card_summary)
    card.append(card_body)

    var card_location = $("<p class='card-text block-with-text'></p>")
    card_location.html("Location: " + item["location"])
    card_body.append(card_location)
    card.append(card_body)

    block.append(card)
    return block
}

$(document).ready(function () {
    
    $("#example").empty();
    data = data.reverse()

    $.each(data, function (index, item) { 

        var result = make_card(index, item)        
        
        $("#example").append(result)
    });

});