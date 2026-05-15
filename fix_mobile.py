import os
import re

html_files = [
    'index.html',
    'screens/cart.html',
    'screens/bulk.html',
    'screens/contact.html',
    'screens/flavors.html'
]

def get_rel_prefix(filepath):
    return '../' if 'screens/' in filepath else ''

for filepath in html_files:
    if not os.path.exists(filepath):
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    prefix = get_rel_prefix(filepath)
    
    # 1. Update the Header Structure (Premium Mobile-Responsive)
    header_regex = re.compile(r'<header[^>]*>.*?</header>', re.DOTALL)
    
    is_home = 'index.html' in filepath and 'screens/' not in filepath
    is_products = 'flavors.html' in filepath or 'bulk.html' in filepath
    is_contact = 'contact.html' in filepath

    new_header = f'''    <header class="bg-surface/90 backdrop-blur-md sticky top-0 w-full z-50 border-b border-outline-variant shadow-sm">
      <div class="flex justify-between items-center px-4 md:px-margin h-20 max-w-container-width mx-auto relative">
        <!-- Logo -->
        <a class="flex items-center shrink-0" href="{prefix}index.html">
          <img src="{prefix}pictures/Poprush-logo.png" alt="POPRUSH" class="h-12 md:h-14 object-contain" />
          <span class="font-display-lg text-2xl md:text-3xl font-black tracking-tighter text-secondary ml-2">POPRUSH</span>
        </a>

        <!-- Desktop Navigation -->
        <nav class="hidden md:flex gap-8 absolute left-1/2 -translate-x-1/2 items-center font-label-md text-label-md">
          <a class="{"text-secondary font-bold border-b-2 border-secondary pb-1" if is_home else "text-on-surface-variant hover:text-secondary"} transition-all" href="{prefix}index.html">Home</a>
          <a class="{"text-secondary font-bold border-b-2 border-secondary pb-1" if is_products else "text-on-surface-variant hover:text-secondary"} transition-all" href="{prefix}screens/flavors.html">Products</a>
          <a class="text-on-surface-variant hover:text-secondary transition-all" href="{prefix}index.html#about">About</a>
          <a class="{"text-secondary font-bold border-b-2 border-secondary pb-1" if is_contact else "text-on-surface-variant hover:text-secondary"} transition-all" href="{prefix}screens/contact.html">Contact</a>
        </nav>

        <!-- Action Buttons -->
        <div class="flex items-center gap-1 md:gap-2">
          <button onclick="window.location.href = '{prefix}screens/cart.html'" class="relative p-2 text-secondary hover:bg-secondary/10 rounded-full transition-all group" aria-label="Cart">
            <span class="material-symbols-outlined text-[28px] md:text-[30px]" style="font-variation-settings: 'FILL' 1">shopping_cart</span>
            <span id="globalCartCount" class="absolute top-1 right-1 bg-secondary text-white text-[10px] font-black px-1.5 py-0.5 rounded-full border-2 border-surface shadow-sm min-w-[18px] text-center">0</span>
          </button>
          
          <button id="menuToggle" class="md:hidden p-2 text-on-surface hover:bg-surface-container rounded-full transition-all" aria-label="Menu">
            <span class="material-symbols-outlined text-[30px]">menu</span>
          </button>
        </div>
      </div>

      <!-- Mobile Menu Dropdown -->
      <div id="mobileMenu" class="hidden md:hidden absolute top-20 left-0 w-full bg-surface border-b border-outline-variant z-40 p-6 flex flex-col gap-5 shadow-2xl transition-all duration-300 transform origin-top">
         <a class="font-headline-md text-headline-md {"text-secondary" if is_home else "text-on-surface"}" href="{prefix}index.html">Home</a>
         <a class="font-headline-md text-headline-md {"text-secondary" if is_products else "text-on-surface"}" href="{prefix}screens/flavors.html">Products</a>
         <a class="font-headline-md text-headline-md text-on-surface" href="{prefix}index.html#about">About</a>
         <a class="font-headline-md text-headline-md {"text-secondary" if is_contact else "text-on-surface"}" href="{prefix}screens/contact.html">Contact</a>
         <hr class="border-outline-variant my-2">
         <button onclick="window.location.href = '{prefix}screens/cart.html'" class="bg-secondary text-white w-full py-4 rounded-xl font-headline-md text-headline-md shadow-lg shadow-secondary/20">Order Now</button>
      </div>
    </header>'''

    content = header_regex.sub(new_header, content)

    # 2. Fix Carousel Arrows for Mobile
    content = content.replace(
        'class="carousel-btn absolute left-8 top-[45%] -translate-y-1/2 z-20 hidden md:flex"',
        'class="carousel-btn absolute left-2 md:left-8 top-[45%] -translate-y-1/2 z-20 flex"'
    )
    content = content.replace(
        'class="carousel-btn absolute right-8 top-[45%] -translate-y-1/2 z-20 hidden md:flex"',
        'class="carousel-btn absolute right-2 md:left-8 top-[45%] -translate-y-1/2 z-20 flex"' # wait I made a typo md:right-8
    )
    # Correction for previous line
    content = content.replace('md:left-8 top-[45%] -translate-y-1/2 z-20 flex" id="btnNext"', 'md:right-8 top-[45%] -translate-y-1/2 z-20 flex" id="btnNext"')

    # 3. Add Mobile Menu JS if not present
    if 'menuToggle' not in content:
        js_code = '''
    <script>
      // Mobile Menu Toggle
      (function() {
        const menuToggle = document.getElementById('menuToggle');
        const mobileMenu = document.getElementById('mobileMenu');
        if (menuToggle && mobileMenu) {
          menuToggle.addEventListener('click', () => {
            const isHidden = mobileMenu.classList.toggle('hidden');
            const icon = menuToggle.querySelector('.material-symbols-outlined');
            if (icon) icon.textContent = isHidden ? 'menu' : 'close';
          });
        }

        // Update Global Cart Count
        function updateGlobalCartCount() {
          try {
            const cart = JSON.parse(localStorage.getItem('poprushCart') || '[]');
            const count = cart.reduce((sum, item) => sum + item.qty, 0);
            const badge = document.getElementById('globalCartCount');
            if (badge) {
              badge.textContent = count;
              badge.style.display = count > 0 ? 'block' : 'none';
            }
          } catch(e) { console.error("Cart error", e); }
        }
        updateGlobalCartCount();
        window.addEventListener('storage', updateGlobalCartCount);
        // Interval as fallback for local updates
        setInterval(updateGlobalCartCount, 1000);
      })();
    </script>
'''
        content = content.replace('</body>', js_code + '  </body>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Responsive header, mobile menu, and carousel arrows applied successfully.")
