/* Portfolio interactions: mobile menu, carousels, lightbox, gallery filters. No dependencies. */
(function () {
  'use strict';

  // Mobile menu
  var btn = document.querySelector('.menu-btn');
  var nav = document.getElementById('nav');
  if (btn && nav) {
    btn.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    nav.addEventListener('click', function (e) {
      if (e.target.tagName === 'A') { nav.classList.remove('open'); btn.setAttribute('aria-expanded', 'false'); }
    });
  }

  // Carousels
  document.querySelectorAll('[data-carousel]').forEach(function (set) {
    var track = set.querySelector('.track');
    var prev = set.querySelector('[data-dir="-1"]');
    var next = set.querySelector('[data-dir="1"]');
    if (!track || !prev || !next) return;
    function step() { var s = track.querySelector('.slide'); return s ? s.getBoundingClientRect().width + 14 : 300; }
    function update() {
      prev.disabled = track.scrollLeft < 4;
      next.disabled = track.scrollLeft + track.clientWidth >= track.scrollWidth - 4;
    }
    prev.addEventListener('click', function () { track.scrollBy({ left: -step() * 2, behavior: 'smooth' }); });
    next.addEventListener('click', function () { track.scrollBy({ left: step() * 2, behavior: 'smooth' }); });
    track.addEventListener('scroll', update, { passive: true });
    window.addEventListener('resize', update);
    update();
  });

  // Lightbox
  var dlg = document.getElementById('lightbox');
  if (dlg) {
    var img = dlg.querySelector('img');
    var cap = dlg.querySelector('.lb-cap');
    var count = dlg.querySelector('.lb-count');
    var items = [], idx = 0, opener = null;

    function groupFor(el) {
      var g = el.getAttribute('data-group');
      var all = Array.prototype.slice.call(document.querySelectorAll('[data-lb][data-group="' + g + '"]'));
      return all.filter(function (b) { var f = b.closest('figure'); return !(f && f.hidden); });
    }
    function show(i) {
      idx = (i + items.length) % items.length;
      var b = items[idx];
      img.src = b.getAttribute('data-full');
      img.alt = b.querySelector('img').alt;
      cap.textContent = b.getAttribute('data-caption') || '';
      count.textContent = (idx + 1) + ' / ' + items.length;
      var n = items[(idx + 1) % items.length];
      if (n) { var pre = new Image(); pre.src = n.getAttribute('data-full'); }
    }
    function open(b) {
      opener = b; items = groupFor(b); show(items.indexOf(b));
      document.body.classList.add('lb-open');
      if (dlg.showModal) dlg.showModal(); else dlg.setAttribute('open', '');
      dlg.querySelector('.close').focus();
    }
    function close() {
      if (dlg.close) dlg.close(); else dlg.removeAttribute('open');
    }
    dlg.addEventListener('close', function () {
      document.body.classList.remove('lb-open');
      img.removeAttribute('src');
      if (opener) opener.focus();
    });
    document.addEventListener('click', function (e) {
      var b = e.target.closest('[data-lb]');
      if (b) { e.preventDefault(); open(b); }
    });
    dlg.querySelector('.close').addEventListener('click', close);
    dlg.querySelector('.prev').addEventListener('click', function () { show(idx - 1); });
    dlg.querySelector('.next').addEventListener('click', function () { show(idx + 1); });
    dlg.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowLeft') show(idx - 1);
      if (e.key === 'ArrowRight') show(idx + 1);
    });
    dlg.addEventListener('click', function (e) { if (e.target === dlg || e.target.classList.contains('lb-stage')) close(); });
    var x0 = null;
    dlg.addEventListener('touchstart', function (e) { x0 = e.touches[0].clientX; }, { passive: true });
    dlg.addEventListener('touchend', function (e) {
      if (x0 === null) return;
      var dx = e.changedTouches[0].clientX - x0;
      if (Math.abs(dx) > 45) show(idx + (dx < 0 ? 1 : -1));
      x0 = null;
    });
  }

  // Gallery filters
  var filters = document.querySelector('.filters');
  if (filters) {
    filters.addEventListener('click', function (e) {
      var b = e.target.closest('button'); if (!b) return;
      filters.querySelectorAll('button').forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
      var f = b.getAttribute('data-filter'), shown = 0;
      document.querySelectorAll('.masonry figure').forEach(function (fig) {
        var ok = f === 'all' || fig.getAttribute('data-brand') === f;
        fig.hidden = !ok; if (ok) shown++;
      });
      var live = document.getElementById('filter-status');
      if (live) live.textContent = shown + ' pieces shown';
    });
  }
})();
