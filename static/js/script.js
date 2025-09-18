// Gestion du modal de suppression universel (toutes entités)
document.addEventListener('DOMContentLoaded', function() {
    const deleteModal = document.getElementById('deleteModal');
    const modalMessage = document.getElementById('modal-delete-message');
    const confirmBtn = document.getElementById('modal-confirm-btn');
    const cancelBtn = document.getElementById('modal-cancel-btn');
    let deleteType = null;
    let deleteId = null;

    // Ouvre le modal quand on clique sur un bouton supprimer
    document.querySelectorAll('.btn-delete[data-type][data-id]').forEach(btn => {
        btn.addEventListener('click', function() {
            deleteType = this.getAttribute('data-type');
            deleteId = this.getAttribute('data-id');
            const name = this.getAttribute('data-name') || '';
            let label = '';
            switch (deleteType) {
                case 'experience': label = "l'expérience : '" + name + "'"; break;
                case 'education': label = "la formation : '" + name + "'"; break;
                case 'skill': label = "la compétence : '" + name + "'"; break;
                case 'project': label = "le projet : '" + name + "'"; break;
                case 'language': label = "la langue : '" + name + "'"; break;
                case 'certification': label = "la certification : '" + name + "'"; break;
                default: label = name;
            }
            if (modalMessage) {
                modalMessage.textContent = "Voulez-vous vraiment supprimer " + label + " ? Toutes les données associées seront perdues.";
            }
            if (deleteModal) {
                deleteModal.style.display = 'flex';
            }
            if (confirmBtn) confirmBtn.focus();
        });
    });

    // Ferme le modal
    function closeDeleteModal() {
        if (deleteModal) deleteModal.style.display = 'none';
        deleteType = null;
        deleteId = null;
    }
    if (cancelBtn) cancelBtn.addEventListener('click', closeDeleteModal);

    // Confirme la suppression
    if (confirmBtn) {
        confirmBtn.onclick = function() {
            if (deleteType && deleteId) {
                const form = document.getElementById('delete-' + deleteType + '-form-' + deleteId);
                if (form) form.submit();
                closeDeleteModal();
            }
        };
    }

    // Ferme le modal avec la touche Escape
    window.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && deleteModal && deleteModal.style.display === 'flex') closeDeleteModal();
    });
});
// Theme Management
const themeToggle = document.getElementById('themeToggle');
const body = document.body;

function setTheme(theme) {
    body.setAttribute('data-theme', theme);
    localStorage.setItem('theme', theme);
    if (themeToggle) {
        const icon = themeToggle.querySelector('i');
        if (icon) {
            icon.classList.remove('fa-moon', 'fa-sun');
            icon.classList.add(theme === 'dark' ? 'fa-sun' : 'fa-moon');
        }
    }
}

// Load saved theme
const savedTheme = localStorage.getItem('theme') || 'light';
setTheme(savedTheme);

if (themeToggle) {
    themeToggle.addEventListener('click', () => {
        const currentTheme = body.getAttribute('data-theme');
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
        setTheme(newTheme);
    });
}

// Mobile Navigation
const hamburger = document.getElementById('hamburger');
const navLinksContainer = document.getElementById('navLinks');

if (hamburger && navLinksContainer) {
    hamburger.addEventListener('click', () => {
        navLinksContainer.classList.toggle('active');
        hamburger.classList.toggle('active');
    });
}

// Close mobile menu when clicking on a link
const navLinks = document.querySelectorAll('.nav-link');
navLinks.forEach(link => {
    link.addEventListener('click', () => {
        if (navLinksContainer) {
            navLinksContainer.classList.remove('active');
        }
        if (hamburger) {
            hamburger.classList.remove('active');
        }
    });
});

// Form validation and enhancement
document.addEventListener('DOMContentLoaded', function() {
    // Add fade-in animation to form containers
    const formContainers = document.querySelectorAll('.form-container');
    formContainers.forEach(container => {
        container.style.opacity = '0';
        container.style.transform = 'translateY(20px)';
        setTimeout(() => {
            container.style.transition = 'all 0.6s ease';
            container.style.opacity = '1';
            container.style.transform = 'translateY(0)';
        }, 100);
    });

    // Add fade-in animation to feature cards
    const featureCards = document.querySelectorAll('.feature-card');
    featureCards.forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(30px)';
        setTimeout(() => {
            card.style.transition = 'all 0.6s ease';
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        }, 200 + (index * 100));
    });

    // Form validation
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const requiredFields = form.querySelectorAll('[required]');
            let isValid = true;

            requiredFields.forEach(field => {
                if (!field.value.trim()) {
                    isValid = false;
                    field.style.borderColor = '#ef4444';
                } else {
                    field.style.borderColor = '';
                }
            });

            if (!isValid) {
                e.preventDefault();
                alert('Veuillez remplir tous les champs obligatoires.');
            }
        });
    });

    // Password confirmation validation
    const passwordField = document.getElementById('password');
    const confirmPasswordField = document.getElementById('confirm_password');
    
    if (passwordField && confirmPasswordField) {
        confirmPasswordField.addEventListener('input', function() {
            if (this.value !== passwordField.value) {
                this.style.borderColor = '#ef4444';
            } else {
                this.style.borderColor = '';
            }
        });
    }
});

// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Auto-hide alerts after 5 seconds
const alerts = document.querySelectorAll('.alert');
alerts.forEach(alert => {
    setTimeout(() => {
        alert.style.transition = 'opacity 0.5s ease';
        alert.style.opacity = '0';
        setTimeout(() => {
            alert.remove();
        }, 500);
    }, 5000);
});