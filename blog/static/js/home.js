const counter = document.querySelector('#user-count');

fetch('/users_count')
  .then(response => response.json())
  .then(data => {
    const count = data.count;
    counter.textContent = 0;

    const step = Math.ceil(count / 100); // increase in steps of 1% of total
    let current = 0;

    function updateCounter() {
      current += step;
      if (current >= count) {
        counter.textContent = count;
        clearInterval(interval);
        counter.classList.remove('active');
      } else {
        counter.textContent = current;
      }
    }

    const interval = setInterval(() => {
      counter.classList.add('active');
      updateCounter();
    }, 150);
  });