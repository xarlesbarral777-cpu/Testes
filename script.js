const form = document.getElementById('form-live');
const grid = document.getElementById('grid');
const template = document.getElementById('card-template');

const storageKey = 'multi-stream-lives';

function loadLives() {
  try {
    return JSON.parse(localStorage.getItem(storageKey)) || [];
  } catch {
    return [];
  }
}

function saveLives(lives) {
  localStorage.setItem(storageKey, JSON.stringify(lives));
}

function renderLives() {
  const lives = loadLives();
  grid.innerHTML = '';

  for (const live of lives) {
    const node = template.content.cloneNode(true);
    const title = node.querySelector('h3');
    const iframe = node.querySelector('iframe');
    const removeButton = node.querySelector('.remover');

    title.textContent = live.title || 'Live sem título';
    iframe.src = live.url;
    iframe.title = live.title || 'Live';

    removeButton.addEventListener('click', () => {
      const updated = loadLives().filter((item) => item.id !== live.id);
      saveLives(updated);
      renderLives();
    });

    grid.appendChild(node);
  }
}

form.addEventListener('submit', (event) => {
  event.preventDefault();

  const formData = new FormData(form);
  const title = String(formData.get('titulo') || '').trim();
  const url = String(formData.get('url') || '').trim();

  const newLive = {
    id: crypto.randomUUID(),
    title,
    url,
  };

  const lives = loadLives();
  lives.push(newLive);
  saveLives(lives);
  form.reset();
  renderLives();
});

renderLives();
