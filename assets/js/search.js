(() => {
  const dialog = document.querySelector('[data-search-dialog]');
  const openButtons = document.querySelectorAll('[data-search-open]');
  const closeButton = document.querySelector('[data-search-close]');
  let search;

  function openSearch() {
    if (!dialog) return;
    dialog.hidden = false;
    if (!search && window.PagefindUI) {
      search = new PagefindUI({ element: '#search', showSubResults: true, excerptLength: 24 });
    }
    requestAnimationFrame(() => dialog.querySelector('input')?.focus());
  }

  function closeSearch() {
    if (dialog) dialog.hidden = true;
  }

  openButtons.forEach((button) => button.addEventListener('click', openSearch));
  closeButton?.addEventListener('click', closeSearch);
  dialog?.addEventListener('click', (event) => { if (event.target === dialog) closeSearch(); });
  document.addEventListener('keydown', (event) => {
    if (event.key === '/' && !/input|textarea/i.test(document.activeElement?.tagName || '')) {
      event.preventDefault();
      openSearch();
    }
    if (event.key === 'Escape') closeSearch();
  });
})();

