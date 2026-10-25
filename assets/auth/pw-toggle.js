// Tiny eye icon inside password fields: toggles password/text
document.querySelectorAll('.pw-eye').forEach(function(b){var i=document.getElementById(b.getAttribute('aria-controls'));if(!i)return;
function t(){var show=i.type==='password';i.type=show?'text':'password';b.setAttribute('aria-pressed',show);b.setAttribute('aria-label',show?'Hide password':'Show password');}
b.addEventListener('mousedown',function(e){e.preventDefault();});b.addEventListener('click',t);
b.addEventListener('keydown',function(e){if(e.key==='Enter'||e.key===' '){e.preventDefault();t();}});});
