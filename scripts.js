// Smooth scrolling for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Mobile menu toggle with logging and force close
const hamburger = document.getElementById('hamburger');
const navLinks = document.querySelector('.nav-links');

hamburger.addEventListener('click', () => {
    console.log('Hamburger clicked'); // For debugging
    navLinks.classList.toggle('active');
    console.log('Menu active:', navLinks.classList.contains('active')); // Check if active class is added/removed
});

// Simple form submission (logs to console for demo)
document.getElementById('contact-form').addEventListener('submit', function(e) {
    e.preventDefault();
    alert('Thank you for your message! (This is a demo - in a real app, send to server)');
    this.reset();
});


// Simple image slider for projects
document.querySelectorAll('.project-image').forEach(container => {
    const images = container.querySelectorAll('img');
    if (images.length > 1) {
        let currentIndex = 0;
        // Create prev/next buttons
        const prevBtn = document.createElement('button');
        prevBtn.textContent = '<';
        prevBtn.className = 'slider-btn prev';
        const nextBtn = document.createElement('button');
        nextBtn.textContent = '>';
        nextBtn.className = 'slider-btn next';
        container.appendChild(prevBtn);
        container.appendChild(nextBtn);
        
        // Show only first image initially
        images.forEach((img, index) => img.style.display = index === 0 ? 'block' : 'none');
        
        // Button events
        prevBtn.addEventListener('click', () => {
            images[currentIndex].style.display = 'none';
            currentIndex = (currentIndex - 1 + images.length) % images.length;
            images[currentIndex].style.display = 'block';
        });
        nextBtn.addEventListener('click', () => {
            images[currentIndex].style.display = 'none';
            currentIndex = (currentIndex + 1) % images.length;
            images[currentIndex].style.display = 'block';
        });
    }
});


// Typing effect for hero heading
const heading = document.querySelector('.hero-content h1');
const text = "Hi, I'm [Your Name]";
let index = 0;

function typeWriter() {
    if (index < text.length) {
        heading.textContent += text.charAt(index);
        index++;
        setTimeout(typeWriter, 100); // Speed of typing
    }
}

// Trigger on page load
window.addEventListener('load', () => {
    heading.textContent = ''; // Clear initial text
    typeWriter();
});

// Close mobile menu when a link is clicked
document.querySelectorAll('.nav-links a').forEach(link => {
    link.addEventListener('click', () => {
        navLinks.classList.remove('active');
    });
});
