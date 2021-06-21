// Product Slider
$(document).ready(function() {
    $('#autoWidth').lightSlider({
        autoWidth: true,
        loop: true,
        onSliderLoad: function() {
            $('#autoWidth').removeClass('cS-hidden');
        }
    });
});

// set flipkart data
function get_flipkart_data() {
    // search query
    query = document.getElementById('search-box').value;
    // set all data
    var info = eel.get_flipkart($`query`)();
    console.log(info);
}

// set flipkart data
function print_data() {
    // Num of items
    var num = 10

    // Number of elements scraped
    for (var i = 0; i < num; i++) {

        ////////// Creating Node elements //////////

        // class="item-a"
        const li = document.createElement('LI');
        // class="box"
        const div1 = document.createElement('DIV');
        // class="slide-img"
        const div2 = document.createElement('DIV');
        // img -> Product Image
        const img = document.createElement('IMG');
        // class="overlay"
        const div3 = document.createElement('DIV');
        // a tag -> Compare hover btn Class="buy-btn"
        const compare = document.createElement('A');
        // class="detail-box"
        const div4 = document.createElement('DIV');
        // class="type"
        const div5 = document.createElement('DIV');
        // a tag -> Product Name
        const name = document.createTextNode('A');
        name.innerHTML = "AYUSH NEGI";
        // span
        const span = document.createElement('SPAN');
        // price
        const price = document.createElement('A');

        // parent ul element
        const ul = document.createElement('UL');

        // top parent element
        const section = document.createElement('SECTION');

        ////////// arranging & appending all elements///////////
        section.appendChild(ul);
        ul.appendChild(li);
        li.appendChild(div1);
        div1.appendChild(div2);
        div2.appendChild(img);
        div2.appendChild(div3);
        div3.appendChild(compare);
        div4.appendChild(div5);
        div5.appendChild(name); 
        div5.appendChild(span);
        div4.appendChild(price);

        // setting className to elements
        // According to HTML Code
        section.setAttribute("id", "slider");
        ul.setAttribute("class", "cs-hidden");
        li.setAttribute("class", "item-a");
        div1.setAttribute("class", "box");
        div2.setAttribute("class", "slide-img");
        div3.setAttribute("class", "overlay");
        compare.setAttribute("class", "buy-btn");
        div4.setAttribute("class", "detail-box");
    }
}

function test() {
    const p = document.getElementById('text');
    const div = document.createElement('LI');
    const text = document.createTextNode('p');
    text.innerHTML = "This is a li";
    p.appendChild(div)
    div.appendChild(text);

}