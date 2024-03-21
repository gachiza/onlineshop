const dropdown = document.getElementById("dropdown-d")
const dropdownoptions = document.getElementById("dropdown-options")

dropdown.addEventListener('click', function(){
    console.log("clicked")
    dropdownoptions.classList.toggle("active")
    dropdown.classList.toggle("active")

    setTimeout(function (){
        console.log("now timing...")
        dropdownoptions.classList.toggle("active")
        dropdownoptions.classList.toggle("active")
    }, 3000)
})