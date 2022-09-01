// Validação
const inputName = document.querySelector('input#name')

inputName.onfocus = function () {
  error.classList.remove('show')
}

inputName.addEventListener('invalid', function (event) {
  event.preventDefault()

  !event.target.validity.valueMissing
    ? null
    : (error.innerText = 'Fill the Fields'),
    error.classList.add('show')

  !event.target.validity.tooShort
    ? null
    : (error.innerText =
        'Your Username must be at least 4 characters long'),
    error.classList.add('show')
})
