document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('pre').forEach((codeBlock) => {
    const button = document.createElement('button');
    button.className = 'copy-btn';
    button.type = 'button';
    button.innerText = 'Copy';

    button.addEventListener('click', () => {
      const code = codeBlock.querySelector('code').innerText;
      navigator.clipboard.writeText(code).then(() => {
        button.innerText = 'Copied!';
        setTimeout(() => {
          button.innerText = 'Copy';
        }, 2000);
      }).catch(() => {
        button.innerText = 'Error';
      });
    });

    codeBlock.style.position = 'relative';  // Ensure the button is positioned correctly
    codeBlock.appendChild(button);
  });
});
