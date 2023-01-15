function calculate() {
    var distance = document.getElementById('distance').value;
    var product = distance * 110 + 2000
    var round = Math.round(product)
    document.getElementById("product").innerHTML = round;
}


//Header mobile


const body = document.querySelector('body')
const headerMenuOpen = document.querySelector('.header__menu__open')
const mobileHeader = document.querySelector('.mobile-header')
const mobileHeaderClose = document.querySelector('.mobile-header-close')

headerMenuOpen.addEventListener("click", () => addCloseFunc("open"))
mobileHeaderClose.addEventListener("click", () => addCloseFunc("close"))

function addCloseFunc(event) {
    if (event === 'open') {
        mobileHeader.classList.add('mobile-header-open')
        body.classList.add('body_hidden')
    } else if (event === 'close') {
        mobileHeader.classList.remove('mobile-header-open')
        body.classList.remove('body_hidden')
    }
}

//Header mobile end