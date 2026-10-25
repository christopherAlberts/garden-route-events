// Show/hide password toggle for the login & signup pages
document.querySelectorAll('.pw-btn').forEach(function(b){var i=document.getElementById(b.getAttribute('aria-controls'));if(!i)return;
b.addEventListener('click',function(){var show=i.type==='password';i.type=show?'text':'password';b.setAttribute('aria-pressed',show);b.setAttribute('aria-label',show?'Hide password':'Show password');b.title=b.getAttribute('aria-label');i.focus();});});
