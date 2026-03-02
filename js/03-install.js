let deferredPrompt;
window.addEventListener('beforeinstallprompt', (e) => {
    e.preventDefault();
    deferredPrompt = e;
    document.getElementById('installPrompt').style.display = 'flex';
});

document.getElementById('installConfirm').addEventListener('click', async () => {
    if (!deferredPrompt) return;
    await deferredPrompt.prompt();
    deferredPrompt = null;
    document.getElementById('installPrompt').style.display = 'none';
});

document.getElementById('installClose').addEventListener('click', () => {
    document.getElementById('installPrompt').style.display = 'none';
});

document.getElementById('installBtn').addEventListener('click', (e) => {
    e.preventDefault();
    document.getElementById('installPrompt').style.display = 'flex';
});

document.getElementById('mobileInstallBtn').addEventListener('click', (e) => {
    e.preventDefault();
    document.getElementById('installPrompt').style.display = 'flex';
    mobileMenu.classList.remove('active');
    menuIcon.className = 'fas fa-bars';
});
