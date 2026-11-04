const checkboxes = document.querySelectorAll('.part-toggle');
const spans = document.querySelectorAll('.line');
const groupRadios = document.querySelectorAll('input[name="group"]');
const groupElements = document.querySelectorAll('[data-group]');

function updateDisplay() {
  const selected = Array.from(checkboxes)
    .filter(cb => cb.checked)
    .map(cb => cb.value);

  spans.forEach(span => {
    const dataPart = span.dataset.part;
    if (!dataPart) return;

    const parts = dataPart.split(' ');
    const match = parts.some(p => selected.includes(p));
    const soloMatch = selected.includes(dataPart);

    span.classList.toggle('active', match);
    span.classList.toggle('active-solo', soloMatch);
  });
}

function updateGroup() {
  const selected = document.querySelector(
    'input[name="group"]:checked'
  ).value;

  groupElements.forEach(element => {
    element.hidden = element.dataset.group !== selected;
  });

  // チェックボックスをすべて解除
  checkboxes.forEach(cb => {
    cb.checked = false;
  });

  updateDisplay();
}

groupRadios.forEach(radio => {
  radio.addEventListener('change', updateGroup);
});


checkboxes.forEach(cb => cb.addEventListener('change', updateDisplay));
updateGroup();