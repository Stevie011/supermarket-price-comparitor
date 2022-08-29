# supermarket-price-comparitor
This webapp takes your shopping list and compares data from various local supermarkets to determine where the cheapest place is to shop

THANKS TO THESE:
    Leon Noel @ 100 Devs
    
    https://code-boxx.com/shopping-list-vanilla-javascript/#sec-download

main function-
give the user a means to compare prices of different supermarkets in area.

user can input a shopping list (stored locally? what’s the best way?), and the app tells them where the cheapest place to do their shopping will be. option: split into 2 shops: ie. it’ll be cheapest if you buy these things here and those things there

components-

frontend - the page itself

page design- html & css

place to input/view shopping list 

place to view results

page hosting (good free one? can’t remember which one we looked at in class?)


backend


mongo db for all current prices

perhaps create list of common household items

eg. 2  litre full cream milk - and then have price at shop 1, price at shop 2, price at shop 3 etc as entries under that item? will have to experiment to find best way to store data

updated every week? or how often?

way to access user’s shopping list- maybe stored locally in format that makes it easy to compare to prices

simple algo- add up total for shopping list from each shop, give user back the lowest

slightly more complicated algo- once lowest price shop is found(for this example, store 1), 
check if certain number (perhaps if over a certain percentage of total number of items) of items from other stores are cheaper than the same item from original lowest store
(in this example: say the shopping list was 10 items, and we’ve chosen 40%. if at least 4 items in the list are cheaper at store 2, we’ll create a new group with those items from store 2). 
then create a new group with those items (incl total), and remove the items from the original list from store 1. 
we’ll then present the user with 2 lists, 6 items from store 1, and 4 items from store 2, letting the user know how much they could save by visiting 2 stores

ofc this could be expanded to 3 or more stores, it just doesn’t seem likely a person would want to go to more than 2 different grocery stores


constraints-

i think it will be quite tricky to make it a worldwide thing- at least, will have to be changed to be specific to each country
we’ll need to access up to date price data for all supermarkets being compared






current progress-

simple version of page - takes users inputs for shopping list, stores them in local storage, displays them on the screen after they’ve been added

TO DO:
web page
make page look a bit nicer (css)
input validator- check if user input is present in predefined price list
drop down list that auto-completes based on user input
database
where to get current prices 
best way to store them 




