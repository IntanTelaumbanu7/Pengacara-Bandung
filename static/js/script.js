// ====================================
// Initialization
// ====================================
document.addEventListener("DOMContentLoaded", function () {
    initializeAOS();
    initializeNavbar();
    initializeParticles();
    initializeBackToTop();
    initializeSmoothScrolling();
    initializeCardHover();
    initializeActiveNavLink();
    initializeMinimumConsultationDate();

    console.log("✨ Website Loaded Successfully");
});

// ====================================
// AOS Animation
// ====================================
function initializeAOS() {
    if (typeof AOS !== "undefined") {
        AOS.init({
            duration: 700,
            easing: "ease-in-out",
            once: true,
            offset: 80,
            disable: window.innerWidth < 768
        });
    }
}

// ====================================
// Navbar
// ====================================
function initializeNavbar() {
    const navbar = document.getElementById("navbar");
    const navbarCollapse = document.querySelector(".navbar-collapse");
    const navbarToggler = document.querySelector(".navbar-toggler");
    const navLinks = document.querySelectorAll(".navbar-nav .nav-link");

    if (!navbar) return;

    function updateNavbarOnScroll() {
        if (window.scrollY > 50) {
            navbar.classList.add("scrolled");
        } else {
            navbar.classList.remove("scrolled");
        }
    }

    updateNavbarOnScroll();

    window.addEventListener("scroll", updateNavbarOnScroll, { passive: true });

    navLinks.forEach(link => {
        link.addEventListener("click", function () {
            if (navbarCollapse && navbarCollapse.classList.contains("show")) {
                bootstrap.Collapse.getOrCreateInstance(navbarCollapse).hide();
            }
        });
    });

    if (navbarToggler) {
        navbarToggler.addEventListener("click", function () {
            this.classList.toggle("active");
        });
    }
}

// ====================================
// Particle Canvas Background
// Dibuat ringan, dan otomatis mati di HP
// ====================================
function initializeParticles() {
    const canvas = document.getElementById("particle-canvas");

    if (!canvas) return;

    if (window.innerWidth < 768) {
        canvas.style.display = "none";
        return;
    }

    const ctx = canvas.getContext("2d");
    let particles = [];
    const particleCount = 45;
    let animationFrameId;

    function resizeCanvas() {
        canvas.width = canvas.offsetWidth;
        canvas.height = canvas.offsetHeight;
    }

    resizeCanvas();
    window.addEventListener("resize", resizeCanvas, { passive: true });

    class Particle {
        constructor() {
            this.x = Math.random() * canvas.width;
            this.y = Math.random() * canvas.height;
            this.size = Math.random() * 2 + 0.5;
            this.speedX = (Math.random() - 0.5) * 0.4;
            this.speedY = (Math.random() - 0.5) * 0.4;
            this.opacity = Math.random() * 0.4 + 0.2;
            this.color = "#d4af37";
        }

        update() {
            this.x += this.speedX;
            this.y += this.speedY;

            if (this.x > canvas.width) this.x = 0;
            if (this.x < 0) this.x = canvas.width;
            if (this.y > canvas.height) this.y = 0;
            if (this.y < 0) this.y = canvas.height;
        }

        draw() {
            ctx.fillStyle = this.color;
            ctx.globalAlpha = this.opacity;
            ctx.fillRect(this.x, this.y, this.size, this.size);
            ctx.globalAlpha = 1;
        }
    }

    for (let i = 0; i < particleCount; i++) {
        particles.push(new Particle());
    }

    function connectParticles() {
        for (let i = 0; i < particles.length; i++) {
            for (let j = i + 1; j < particles.length; j++) {
                const dx = particles[i].x - particles[j].x;
                const dy = particles[i].y - particles[j].y;
                const distance = Math.sqrt(dx * dx + dy * dy);

                if (distance < 90) {
                    ctx.strokeStyle = `rgba(212, 175, 55, ${0.16 * (1 - distance / 90)})`;
                    ctx.lineWidth = 0.5;
                    ctx.beginPath();
                    ctx.moveTo(particles[i].x, particles[i].y);
                    ctx.lineTo(particles[j].x, particles[j].y);
                    ctx.stroke();
                }
            }
        }
    }

    function animate() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        particles.forEach(particle => {
            particle.update();
            particle.draw();
        });

        connectParticles();

        animationFrameId = requestAnimationFrame(animate);
    }

    animate();

    document.addEventListener("visibilitychange", function () {
        if (document.hidden) {
            cancelAnimationFrame(animationFrameId);
        } else {
            animate();
        }
    });
}

// ====================================
// Back to Top Button
// ====================================
function initializeBackToTop() {
    const backToTopBtn = document.getElementById("back-to-top");

    if (!backToTopBtn) return;

    window.addEventListener("scroll", function () {
        if (window.scrollY > 300) {
            backToTopBtn.classList.add("show");
        } else {
            backToTopBtn.classList.remove("show");
        }
    }, { passive: true });

    backToTopBtn.addEventListener("click", function () {
        window.scrollTo({
            top: 0,
            behavior: "smooth"
        });
    });
}

// ====================================
// Smooth Scrolling
// ====================================
function initializeSmoothScrolling() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener("click", function (e) {
            const targetId = this.getAttribute("href");

            if (!targetId || targetId === "#") return;

            const target = document.querySelector(targetId);

            if (target) {
                e.preventDefault();
                target.scrollIntoView({
                    behavior: "smooth",
                    block: "start"
                });
            }
        });
    });
}

// ====================================
// Card Hover Effect
// Ringan di laptop, mati di HP
// ====================================
function initializeCardHover() {
    if (window.innerWidth < 768) return;

    const cards = document.querySelectorAll(
        ".service-card, .article-card, .testimonial-card, .value-card, .contact-info-card"
    );

    cards.forEach(card => {
        card.addEventListener("mouseenter", function () {
            this.style.transform = "translateY(-8px)";
            this.style.boxShadow = "0 15px 40px rgba(212, 175, 55, 0.18)";
        });

        card.addEventListener("mouseleave", function () {
            this.style.transform = "";
            this.style.boxShadow = "";
        });
    });
}

// ====================================
// Active Navigation Link
// ====================================
function initializeActiveNavLink() {
    const currentLocation = location.pathname;
    const navLinks = document.querySelectorAll(".navbar-nav .nav-link");

    navLinks.forEach(link => {
        if (link.getAttribute("href") === currentLocation) {
            link.classList.add("active");
        } else {
            link.classList.remove("active");
        }
    });
}

// ====================================
// Minimum Date for Consultation Form
// ====================================
function initializeMinimumConsultationDate() {
    const consultationDateInput = document.getElementById("consultationDate");

    if (!consultationDateInput) return;

    const today = new Date();
    const yyyy = today.getFullYear();
    const mm = String(today.getMonth() + 1).padStart(2, "0");
    const dd = String(today.getDate()).padStart(2, "0");
    const minDate = `${yyyy}-${mm}-${dd}`;

    consultationDateInput.setAttribute("min", minDate);
}

// ====================================
// Toast Messages
// ====================================
function showSuccessMessage(message) {
    showToast(message, "success");
}

function showErrorMessage(message) {
    showToast(message, "error");
}

function showToast(message, type = "success") {
    const toast = document.createElement("div");

    toast.className = `toast-message ${type}`;
    toast.innerHTML = `
        <div class="toast-content">
            <i class="fas ${type === "success" ? "fa-check-circle" : "fa-exclamation-circle"}"></i>
            <span>${message}</span>
        </div>
    `;

    toast.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        max-width: calc(100vw - 40px);
        background: ${type === "success"
            ? "linear-gradient(135deg, #25d366, #128c7e)"
            : "linear-gradient(135deg, #ff6b6b, #ee5a6f)"};
        color: white;
        padding: 1rem 1.2rem;
        border-radius: 12px;
        box-shadow: 0 5px 20px rgba(0, 0, 0, 0.3);
        z-index: 10000;
        animation: slideInRight 0.4s ease-out;
    `;

    document.body.appendChild(toast);

    setTimeout(() => {
        toast.style.animation = "fadeOut 0.4s ease-out forwards";
        setTimeout(() => toast.remove(), 400);
    }, 3000);
}

// ====================================
// Global Styles from JS
// ====================================
const scriptStyle = document.createElement("style");

scriptStyle.textContent = `
    @keyframes slideInRight {
        from {
            opacity: 0;
            transform: translateX(100px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }

    @keyframes fadeOut {
        from {
            opacity: 1;
            transform: translateX(0);
        }
        to {
            opacity: 0;
            transform: translateX(100px);
        }
    }

    .toast-content {
        display: flex;
        align-items: center;
        gap: 0.6rem;
        font-size: 0.95rem;
        line-height: 1.5;
    }

    @media (max-width: 768px) {
        .toast-message {
            top: 15px !important;
            right: 15px !important;
            left: 15px !important;
            max-width: none !important;
        }
    }
`;

document.head.appendChild(scriptStyle);

// ====================================
// Refresh AOS on Resize
// ====================================
window.addEventListener("resize", function () {
    if (typeof AOS !== "undefined") {
        AOS.refresh();
    }
}, { passive: true });
