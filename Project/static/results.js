function make_card_marked(index, item) {

    var block = $("<div class='col-md-4 result-item'></div>")

    var card = $("<div class='card bg-light'></div>")

    //make the card image with link
    var id = item["id"]
    var image_link = $("<a href='/view/" + id + "'></a>")
    var card_img = $("<img class='card-img-top' src='" + item["img"] + "' alt='Card image'>")
    image_link.html(card_img)
    card.append(image_link)

    //make title
    var card_body = $("<div class='card-body'>")
    var title = $("<h4 class='card-title'></h5>")
    var card_summary = $("<p class='card-text'></p>")
    var card_location = $("<p class='card-text'></p>")

    //make the matched parts
    var st = item["position_st"]
    var en = item["position_en"]
    if (item["matched"]=="name") {
        var name = item["name"]
        var title_highlight = [name.slice(0, st), "<span class='highlight-result border-secondary'>", name.slice(st, en), "</span>", name.slice(en)].join('')
        title.html(title_highlight)
        card_summary.html(item["summary"])
        card_location.html("Location: " + item["location"])
    } 

    if (item["matched"]=="summary"){
        title.html(item["name"])
        var summary = item["summary"]
        var summary_highlight = [summary.slice(0, st), "<span class='highlight-result border-secondary'>", summary.slice(st, en), "</span>", summary.slice(en)].join('')
        card_summary.html(summary_highlight)
        card_location.html("Location: " + item["location"])
    } 

    if (item["matched"]=="location"){
        title.html(item["name"])
        card_summary.html(item["summary"])
        var location = item["location"]
        var location_highlight = [location.slice(0, st), "<span class='highlight-result border-secondary'>", location.slice(st, en), "</span>", location.slice(en)].join('')
        card_location.html("Location: " + location_highlight)
    }
    
    card_body.append(title)
    card_body.append(card_summary)
    card_body.append(card_location)
    
    card.append(card_body)

    block.append(card)
    return block
}

function display_results_marked(data) {
    $("#content").empty();

    var n_items = data.length
    var row1 = $("<div class='row'></div>")
    var col = $("<div class='col-md-12'></div>")
    col.html(n_items + " results found.")
    row1.append(col)
    $("#content").append(row1)

    var row2 = $("<div id='results' class='row'></div>")
    $("#content").append(row2)

    $.each(data, function (index, item) { 
        console.log(data);
        
        var result = make_card_marked(index, item)
        
        $("#results").append(result)
    });
}

$(document).ready(function () {
    if (n_items == 0) {
        $("#content").html("No results found.")
    } else {
        display_results_marked(results)
    }
})