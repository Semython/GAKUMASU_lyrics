const checkboxes = document.querySelectorAll('.part-toggle');
const spans = document.querySelectorAll('.line');

function updateDisplay() {
  const selected = Array.from(checkboxes)
    .filter(cb => cb.checked)
    .map(cb => cb.value);

  spans.forEach(span => {
    const dataPart = span.dataset.part;
    if (!dataPart) return;  

    const parts = span.dataset.part.split(' ');
    const match = parts.some(p => selected.includes(p));
    span.classList.toggle('active', match);
  });
}

checkboxes.forEach(cb => cb.addEventListener('change', updateDisplay));
updateDisplay();