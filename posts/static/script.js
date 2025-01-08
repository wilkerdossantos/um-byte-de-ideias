const headerSize = document.getElementById('header').offsetHeight;
const navbarSize = document.getElementById('navbar').offsetHeight;
const totalSize = headerSize + navbarSize + 150;
const socialMediaButtons = document.getElementById('social-share');
const container = document.querySelector("body > main > div.container.mt-5")
let marginContainer = window.getComputedStyle(container).marginLeft.replace('px', '')
marginContainer = Number(marginContainer) / 2 

socialMediaButtons.style.top = `${totalSize}px`
socialMediaButtons.style.left = `${marginContainer}px`