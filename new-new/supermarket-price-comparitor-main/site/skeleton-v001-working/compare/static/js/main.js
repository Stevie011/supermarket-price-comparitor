// (A1 & A2) Get all the related HTML elements, initialize the “add item” form.
// (A3) Load the previously saved shopping cart from localstorage.items and restore it into slist.items.
// (A4) Finally, draw the HTML shopping list.


var list_vals = document.getElementsByName("grocery_item")
//this gives us a list of the item names
var item_checklist = []
for(let i of list_vals.values()){
  item_checklist.push(i.value)
}

//list of checkers prices
var item_prices_checkers = document.getElementsByName("grocery_item_price_checkers")
var price_list_checkers = []
for(let i of item_prices_checkers.values()){
  price_list_checkers.push(i.value)
}

//list of pnp prices
var item_prices_pnp = document.getElementsByName("grocery_item_price_pnp")
var price_list_pnp = []
for(let i of item_prices_pnp.values()){
  price_list_pnp.push(i.value)
}

//list of woolworths prices
var item_prices_woolworths = document.getElementsByName("grocery_item_price_woolworths")
var price_list_woolworths = []
for(let i of item_prices_woolworths.values()){
  price_list_woolworths.push(i.value)
}

var slist = {
  
    
    // (A) INITIALIZE SHOPPING LIST
    items : [],   // current shopping list
    hform : null, // html add item <form>
    hitem : null, // html add item <input> field
    hadd : null,  // html add item submit button
    hlist : null, // html <div> shopping list
    init : () => {
      
      // (A1) GET HTML ELEMENTS
      slist.hform = document.getElementById("shop-form");
      slist.hitem = document.getElementById("shop-item");
      slist.hadd = document.getElementById("shop-add");
      slist.hlist = document.getElementById("shop-list");
  
      // (A2) "ACTIVATE" HTML ADD ITEM FORM
      slist.hitem.setAttribute("autocomplete", "off");
      slist.hform.onsubmit = slist.add;
      slist.hitem.disabled = false;
      slist.hadd.disabled = false;
  
      // (A3) RESTORE PREVIOUS SHOPPING LIST
      if (localStorage.items == undefined) { localStorage.items = "[]"; }
      slist.items = JSON.parse(localStorage.items);
  
      // (A4) DRAW HTML SHOPPING LIST
      slist.draw();
    },

//     (C1) Captain Obvious, to stop the HTML form from submitting and reloading the entire page.
// (C2) Take note of how the new item is being pushed as an object into the slist.items array – { name:"ITEM NAME", done:true/false }
// (B & C2) Update the localstorage.
// (C3) Lastly, redraw the updated list.

    // (B) SAVE SHOPPING LIST INTO LOCAL STORAGE
    save : () => {
      if (localStorage.items == undefined) { localStorage.items = "[]"; }
      localStorage.items = JSON.stringify(slist.items);
    },
  
    // (C) ADD NEW ITEM TO THE LIST
    add : (evt) => {
      // (C1) PREVENT FORM SUBMIT
      evt.preventDefault();
      var item_prices_checkers = document.getElementsByName("grocery_item_price_checkers")
      var price_list_checkers = []
      for(let i of item_prices_checkers.values()){
        price_list_checkers.push(i.value)
      }
      if (item_checklist.includes(slist.hitem.value)){
          // (C2) ADD NEW ITEM TO LIST
        slist.items.push({
          name : slist.hitem.value, // item name
          done : false // true for "got it", false for "not yet"
        });
        slist.hitem.value = "";
        slist.save();
    
        // (C3) REDRAW HTML SHOPPING LIST
        slist.draw();}
        //***************** */
        //if item not in list, send error msg
    },

    //this one is quite self-explanatory
  
    // (D) DELETE SELECTED ITEM
    delete : (id) => { if (confirm("Remove this item?")) {
      slist.items.splice(id, 1);
      slist.save();
      slist.draw();
    }},
    //E is skipped here haha

    // (F) DRAW THE HTML SHOPPING LIST
    draw : () => {
      // (F1) RESET HTML LIST
      slist.hlist.innerHTML = "";
  
      // (F2) NO ITEMS
      if (slist.items.length == 0) {
        slist.hlist.innerHTML = "<div class='item-row item-name'>No items found.</div>";
      }
  
      // (F3) DRAW ITEMS
      
      else {
        var current_checkers_price_total= 0
        var current_pnp_price_total= 0
        var current_woolworths_price_total= 0
        var current_list =[]
        for(let i in slist.items){
          //console.log(slist.items[i].name);
          current_list.push(slist.items[i].name);
        }
        //console.log(current_list)
        //console.log(item_checklist)
        for(let i in current_list){
          //find index of current item 
          _index = item_checklist.indexOf(current_list[i])

          //find price in list and add to total
          checkers_price = Number(item_prices_checkers[_index].value)
          current_checkers_price_total += checkers_price

          //repeat above for pnp
          pnp_price = Number(item_prices_pnp[_index].value)
          current_pnp_price_total += pnp_price

          //repeat above for woolworths
          woolworths_price = Number(item_prices_woolworths[_index].value)
          current_woolworths_price_total += woolworths_price
          //console.log(_price)
        }
        current_checkers_price_total = Number(current_checkers_price_total.toFixed(2))
        current_pnp_price_total = Number(current_pnp_price_total.toFixed(2))
        current_woolworths_price_total = Number(current_woolworths_price_total.toFixed(2))
        //console.log(current_checkers_price)

        //whip it into the DOM
        var checkers_display_price = document.getElementById("checkers-display-price")
        checkers_display_price.innerHTML = current_checkers_price_total

        //repeat for pnp
        var pnp_display_price = document.getElementById("pnp-display-price")
        pnp_display_price.innerHTML = current_pnp_price_total

        //repeat for woolworths
        var woolworths_display_price = document.getElementById("woolworths-display-price")
        woolworths_display_price.innerHTML = current_woolworths_price_total

        //console.log(current_list)
        for (let i in slist.items) {
          // ITEM ROW
          let row = document.createElement("div");
          row.className = "item-row";
          slist.hlist.appendChild(row);
  
          // ITEM NAME
          let name = document.createElement("div");
          name.innerHTML = slist.items[i].name;
          name.className = "item-name";
          if (slist.items[i].done) { name.classList.add("item-got"); }
          row.appendChild(name);
  
          // DELETE BUTTON
          let del = document.createElement("input");
          del.className = "item-del";
          del.type = "button";
          del.value = "Delete";;
          del.onclick = () => { slist.delete(i); };
          row.appendChild(del);
        }
      }
    }
  };
  window.addEventListener("load", slist.init);


  
  