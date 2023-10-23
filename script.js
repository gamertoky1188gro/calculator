let display = document.getElementById('display');
let currentInput = '';

function appendToDisplay(value) {
    currentInput += value;
    display.innerText = currentInput;
}

function clearDisplay() {
    currentInput = '';
    display.innerText = '0';
}

function calculateResult() {
    try {
        currentInput = eval(currentInput);
        display.innerText = currentInput;
    } catch (error) {
        display.innerText = 'Error';
    }
}
