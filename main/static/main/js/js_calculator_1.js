const calculator_js_buttons = document.getElementsByClassName('calculator_js_button_button')

const calc_inp = document.getElementById('calc_inp')
let set = ''

for (let i = 0; i < calculator_js_buttons.length; i++) {
    calculator_button(calculator_js_buttons[i]) 
}

function calculator_button(button) {
    button.addEventListener('click', calculator_button_addevent);
    function calculator_button_addevent(){
        console.log(4)
        let val = button.getAttribute('data-type');
        if (val === "=") {
            set = eval(set)
        } else if (val === "C") {
            set = ""
        } else {
            set += val
        }
        console.log(val)
        console.log(set)
        calc_inp.innerHTML = set
    }

}

// ---------------------------------------------------------------------
// 22222222222222222222222222222222222222222222222222222222222222222222222

