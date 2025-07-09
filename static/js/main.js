// Mobile menu toggle functionality
document.addEventListener('DOMContentLoaded', function() {
    const mobileMenuButton = document.getElementById('mobile-menu-button');
    const mobileMenu = document.getElementById('mobile-menu');

    if (mobileMenuButton && mobileMenu) {
        mobileMenuButton.addEventListener('click', () => {
            const isOpen = !mobileMenu.classList.contains('hidden');
            mobileMenu.classList.toggle('hidden');
            
            // Toggle hamburger/cross icon
            const icons = mobileMenuButton.querySelectorAll('svg');
            if (isOpen) {
                icons[0].classList.remove('hidden');
                icons[1].classList.add('hidden');
            } else {
                icons[0].classList.add('hidden');
                icons[1].classList.remove('hidden');
            }
        });
    }

    // Dark mode functionality
    const themeToggle = document.getElementById('theme-toggle');
    const mobileThemeToggle = document.getElementById('mobile-theme-toggle');
    const html = document.documentElement;

    // Check for saved theme preference or default to light mode
    const currentTheme = localStorage.getItem('theme') || 'light';
    
    // Apply the current theme
    if (currentTheme === 'dark') {
        html.classList.add('dark');
        updateToggleState(true);
    } else {
        html.classList.remove('dark');
        updateToggleState(false);
    }

    // Function to update toggle button states
    function updateToggleState(isDark) {
        // Update desktop toggle
        if (themeToggle) {
            const dot = themeToggle.querySelector('#theme-toggle-dot');
            const sunIcon = themeToggle.querySelector('#sun-icon');
            const moonIcon = themeToggle.querySelector('#moon-icon');
            
            if (isDark) {
                dot?.classList.add('translate-x-3');
                dot?.classList.remove('-translate-x-3');
                sunIcon?.classList.add('hidden');
                moonIcon?.classList.remove('hidden');
            } else {
                dot?.classList.add('-translate-x-3');
                dot?.classList.remove('translate-x-3');
                sunIcon?.classList.remove('hidden');
                moonIcon?.classList.add('hidden');
            }
        }

        // Update mobile toggle
        if (mobileThemeToggle) {
            const mobileDot = mobileThemeToggle.querySelector('#mobile-theme-toggle-dot');
            const mobileSunIcon = mobileThemeToggle.querySelector('#mobile-sun-icon');
            const mobileMoonIcon = mobileThemeToggle.querySelector('#mobile-moon-icon');
            
            if (isDark) {
                mobileDot?.classList.add('translate-x-3');
                mobileDot?.classList.remove('-translate-x-3');
                mobileSunIcon?.classList.add('hidden');
                mobileMoonIcon?.classList.remove('hidden');
            } else {
                mobileDot?.classList.add('-translate-x-3');
                mobileDot?.classList.remove('translate-x-3');
                mobileSunIcon?.classList.remove('hidden');
                mobileMoonIcon?.classList.add('hidden');
            }
        }
    }

    // Function to toggle theme
    function toggleTheme() {
        const isDark = html.classList.contains('dark');
        
        if (isDark) {
            html.classList.remove('dark');
            localStorage.setItem('theme', 'light');
            updateToggleState(false);
        } else {
            html.classList.add('dark');
            localStorage.setItem('theme', 'dark');
            updateToggleState(true);
        }
    }

    // Add event listeners to both toggle buttons
    if (themeToggle) {
        themeToggle.addEventListener('click', toggleTheme);
    }
    
    if (mobileThemeToggle) {
        mobileThemeToggle.addEventListener('click', toggleTheme);
    }
});
