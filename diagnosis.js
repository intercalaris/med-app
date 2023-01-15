const py_file = require('./diagnosis.py');
const form = document.querySelector("form");
form.addEventListener('submit', (event) => {
    event.preventDefault();
    const symptoms = document.querySelector('#symptoms').value;
    const diagnosis = py_file.getDiagnosis(symptoms);
    //display diagnosis on the webpage
});

});
