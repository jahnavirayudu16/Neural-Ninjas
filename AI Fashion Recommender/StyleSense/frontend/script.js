// Theme Toggle
const themeToggle = document.getElementById('themeToggle');

// Check for saved theme preference or default to light
const currentTheme = localStorage.getItem('theme') || 'light';
document.documentElement.setAttribute('data-theme', currentTheme);
if (currentTheme === 'dark') {
    document.body.classList.add('dark-theme');
    themeToggle.textContent = '☀️';
}

themeToggle.addEventListener('click', () => {
    const isDark = document.body.classList.toggle('dark-theme');
    const theme = isDark ? 'dark' : 'light';
    localStorage.setItem('theme', theme);
    themeToggle.textContent = isDark ? '☀️' : '🌙';
});

// Close modal when clicking outside
window.addEventListener('click', (event) => {
    const modal = document.getElementById('outfitModal');
    if (event.target === modal) {
        modal.style.display = 'none';
    }
});

// Smooth scroll for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({ behavior: 'smooth' });
        }
    });
});

console.log('✨ StyleSense AI Fashion Recommender loaded successfully!');
