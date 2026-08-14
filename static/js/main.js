// EDR Portfolio — main.js
document.addEventListener('DOMContentLoaded', () => {

  // Active nav link on scroll
  const sections = document.querySelectorAll('section[id]');
  const navLinks = document.querySelectorAll('.nav-link');

  if (sections.length && navLinks.length) {
    const observer = new IntersectionObserver(entries => {
      entries.forEach(e => {
        if (e.isIntersecting) {
          navLinks.forEach(l => l.classList.remove('active'));
          const link = document.querySelector(`.nav-link[href="#${e.target.id}"]`);
          if (link) link.classList.add('active');
        }
      });
    }, { threshold: 0.4 });
    sections.forEach(s => observer.observe(s));
  }

  // Subtle scroll-fade for project sections
  const fadels = document.querySelectorAll('.proj-section, .kpi-card, .skill-card, .project-card, .reflect-card, .ana-card');
  if ('IntersectionObserver' in window) {
    fadels.forEach(el => { el.style.opacity = '0'; el.style.transform = 'translateY(14px)'; el.style.transition = 'opacity .4s ease, transform .4s ease'; });
    const fadeObs = new IntersectionObserver(entries => {
      entries.forEach(e => {
        if (e.isIntersecting) {
          e.target.style.opacity = '1';
          e.target.style.transform = 'translateY(0)';
          fadeObs.unobserve(e.target);
        }
      });
    }, { threshold: 0.1 });
    fadels.forEach(el => fadeObs.observe(el));
  }

  // Lightbox Modal Logic
  const lightbox = document.getElementById('lightboxModal');
  const lightboxImg = document.getElementById('lightboxImg');
  const lightboxCap = document.getElementById('lightboxCaption');
  const lightboxOpenTab = document.getElementById('lightboxOpenTab');
  const galleryWraps = document.querySelectorAll('.gallery-wrap');

  if (lightbox && lightboxImg && galleryWraps.length) {
    galleryWraps.forEach(wrap => {
      wrap.addEventListener('click', () => {
        const img = wrap.querySelector('.gallery-img');
        const cap = wrap.querySelector('.gallery-cap');
        if (img) {
          lightboxImg.src = img.src;
          lightboxImg.alt = img.alt;
          if (lightboxOpenTab) {
            lightboxOpenTab.href = img.src;
          }
          if (cap) {
            lightboxCap.textContent = cap.textContent;
          } else {
            lightboxCap.textContent = img.alt;
          }
          lightbox.style.display = 'flex';
          setTimeout(() => {
            lightbox.classList.add('show');
          }, 10);
        }
      });
    });

    const closeLightbox = () => {
      lightbox.classList.remove('show');
      setTimeout(() => {
        lightbox.style.display = 'none';
      }, 300);
    };

    lightbox.addEventListener('click', (e) => {
      if (e.target !== lightboxImg && e.target !== lightboxCap && e.target !== lightboxOpenTab) {
        closeLightbox();
      }
    });

    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && lightbox.classList.contains('show')) {
        closeLightbox();
      }
    });
  }

});
