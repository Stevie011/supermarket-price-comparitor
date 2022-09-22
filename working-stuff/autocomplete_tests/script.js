let countries = []

const countryListElement = document.querySelector("#country-list")
const countryInputElement = document.querySelector("#country-input")

//this gets this list of country names from the api
function fetchCountries(){
    //api name
    fetch("https://restcountries.com/v3.1/all")
    .then((response) => response.json())
    .then((data) => {
        //add names to list 
        countries = data.map((x) => x.name.common)
        countries.sort()
        //then call load data function
        loadData(countries, countryListElement)
    });
}

//this adds the data from each li to the list
function loadData(data, element){
    if (data){
        element.innerHTML = ""
        let innerElement = ""
        data.forEach((item) =>{
            innerElement += `
            <li>${item}</li>`
        })

        element.innerHTML = innerElement
    }
}

function filterData(data, searchText){
    return data.filter((x) => x.toLowerCase().includes(searchText.toLowerCase()))

}

fetchCountries();

countryInputElement.addEventListener("input", function(){
    const filteredData = filterData(countries, countryInputElement.value)
    loadData(filteredData, countryListElement)
})
