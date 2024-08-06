document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('pre').forEach((pre) => {
    const button = document.createElement('button');
    button.className = 'copy-btn';
    button.type = 'button';
    button.innerText = 'Copy';

    button.addEventListener('click', () => {
      const code = pre.querySelector('code').innerText.trim();
      navigator.clipboard.writeText(code).then(() => {
        button.innerText = 'Copied!';
        setTimeout(() => {
          button.innerText = 'Copy';
        }, 2000);
      }).catch(() => {
        button.innerText = 'Error';
      });
    });

    pre.style.position = 'relative';
    pre.appendChild(button);
  });
});
