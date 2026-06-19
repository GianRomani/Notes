/**
 * Custom micro-interactions for Gianfranco's Second Brain
 */
document.addEventListener('DOMContentLoaded', () => {
  // Create mouse-glow element
  const glow = document.createElement('div');
  glow.id = 'glow-pointer';
  document.body.appendChild(glow);

  // Follow cursor
  document.addEventListener('mousemove', (e) => {
    glow.style.left = e.clientX + 'px';
    glow.style.top = e.clientY + 'px';
  });
});
