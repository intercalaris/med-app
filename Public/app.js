const diagnosisButton = document.querySelector('.diagnosis-button');
const treatmentButton = document.querySelector('.treatment-button');
const researchButton = document.querySelector('.research-button');

diagnosisButton.addEventListener('click', () => {
    window.location.href = 'diagnosis.html';
});

treatmentButton.addEventListener('click', () => {
    window.location.href = 'treatment.html';
});

researchButton.addEventListener('click', () => {
    window.location.href = 'research.html';
});
