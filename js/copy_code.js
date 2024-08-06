document.addEventListener('DOMContentLoaded', (event) => {
    document.querySelectorAll('.code-container').forEach((codeContainer) => {
        const copyButton = document.createElement('button');
        copyButton.textContent = 'Copy Code';
        copyButton.className = 'copy-button';

        copyButton.addEventListener('click', () => {
            const code = codeContainer.querySelector('pre code').textContent;
            navigator.clipboard.writeText(code).then(() => {
                copyButton.textContent = 'Copied!';
                setTimeout(() => {
                    copyButton.textContent = 'Copy Code';
                }, 2000);
            }).catch(err => {
                console.error('Failed to copy: ', err);
            });
        });

        codeContainer.appendChild(copyButton);
    });
});
