// (A1 & A2) Get all the related HTML elements, initialize the “add item” form.
// (A3) Load the previously saved shopping cart from localstorage.items and restore it into slist.items.
// (A4) Finally, draw the HTML shopping list.

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
  
      // (C2) ADD NEW ITEM TO LIST
      slist.items.push({
        name : slist.hitem.value, // item name
        done : false // true for "got it", false for "not yet"
      });
      slist.hitem.value = "";
      slist.save();
  
      // (C3) REDRAW HTML SHOPPING LIST
      slist.draw();
    },

    //this one is quite self-explanatory
  
    // (D) DELETE SELECTED ITEM
    delete : (id) => { if (confirm("Remove this item?")) {
      slist.items.splice(id, 1);
      slist.save();
      slist.draw();
    }},


    //this could be removed for us
    // (E) TOGGLE ITEM BETWEEN "GOT IT" OR "NOT YET"
    // toggle : (id) => {
    //   slist.items[id].done = !slist.items[id].done;
    //   slist.save();
    //   slist.draw();
    // },
  
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
  
          // COMPLETED/NOT YET BUTTON
        //   let ok = document.createElement("input");
        //   ok.className = "item-ok";
        //   ok.type = "button";
        //   ok.value = slist.items[i].done ? "Not Yet" : "Got It";
        //   ok.onclick = () => { slist.toggle(i); };
        //   row.appendChild(ok);
        }
      }
    }
  };
  window.addEventListener("load", slist.init);
  