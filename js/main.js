document.addEventListener('DOMContentLoaded', () => {
const track = document.getElementById('carouselTrack');
  const btnPrev = document.getElementById('btnPrev');
  const btnNext = document.getElementById('btnNext');
  const cards = track.querySelectorAll('.carousel-card');

  // Update active card based on scroll position
  function updateCenterCard() {
    // center of the visible track relative to the document
    const trackRect = track.getBoundingClientRect();
    const trackCenter = trackRect.left + trackRect.width / 2;
    
    let closestCard = null;
    let minDistance = Infinity;

    cards.forEach(card => {
      const cardRect = card.getBoundingClientRect();
      const cardCenter = cardRect.left + cardRect.width / 2;
      const distance = Math.abs(trackCenter - cardCenter);

      if (distance < minDistance) {
        minDistance = distance;
        closestCard = card;
      }
      
      card.classList.remove('is-active');
    });

    if (closestCard) {
      closestCard.classList.add('is-active');
    }
  }

  // Scroll logic
  if(btnPrev && btnNext && track) {
    btnNext.addEventListener('click', () => {
      const cardWidth = track.querySelector('.carousel-card').offsetWidth;
      track.scrollBy({ left: cardWidth + 24, behavior: 'smooth' });
    });
    btnPrev.addEventListener('click', () => {
      const cardWidth = track.querySelector('.carousel-card').offsetWidth;
      track.scrollBy({ left: -(cardWidth + 24), behavior: 'smooth' });
    });
  }

  track.addEventListener('scroll', updateCenterCard);
  window.addEventListener('resize', updateCenterCard);
  
  // Initialize
  setTimeout(updateCenterCard, 100);

  // Mobile Menu Toggle
  const menuToggle = document.getElementById('menuToggle');
  const mobileMenu = document.getElementById('mobileMenu');
  if (menuToggle && mobileMenu) {
    menuToggle.addEventListener('click', () => {
      const isHidden = mobileMenu.classList.toggle('hidden');
      const icon = menuToggle.querySelector('.material-symbols-outlined');
      if (icon) icon.textContent = isHidden ? 'menu' : 'close';
    });
  }
});