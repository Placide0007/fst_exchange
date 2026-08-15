document.addEventListener('submit', async (e) => {
    const form = e.target;
    if (!form.matches('.react-form')) return;

    e.preventDefault();

    const formData = new FormData(form);
    try {
        const response = await fetch(form.action, {
            method: 'POST',
            body: formData,
            headers: { 'X-Requested-With': 'XMLHttpRequest' },
        });

        if (!response.ok) throw new Error('Request failed');

        const data = await response.json();

        form.querySelector('.reaction-count').textContent = data.count;
        const icon = form.querySelector('.icon-liked');
        icon.src = data.liked ? data.liked_icon_url : data.unliked_icon_url;

    } catch (err) {
        // En cas d'échec réseau, on retombe sur le comportement natif
        form.submit();
    }
});