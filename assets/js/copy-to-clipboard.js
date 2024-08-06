document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('pre > code').forEach((codeBlock) => {
    const button = document.createElement('button');
    button.className = 'copy-btn';
    button.type = 'button';
    button.innerText = 'Copy';

    button.addEventListener('click', () => {
      const code = codeBlock.innerText.trim();
      navigator.clipboard.writeText(code).then(() => {
        button.innerText = 'Copied!';
        setTimeout(() => {
          button.innerText = 'Copy';
        }, 2000);
      }).catch(() => {
        button.innerText = 'Error';
      });
    });

    const pre = codeBlock.parentNode;
    pre.style.position = 'relative';
    pre.insertBefore(button, codeBlock);
  });
});
