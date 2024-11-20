document.addEventListener('DOMContentLoaded', function() {
    const header = document.querySelector('.header');
    const loginForm = document.querySelector('.login-form');

    function adjustLayout() {
        if (window.innerWidth < 768) {
            header.style.flexDirection = 'column';
            header.style.padding = '10px';
            Array.from(header.children).forEach(link => {
                link.style.margin = '10px 0';
            });

        
            loginForm.style.width = '90%';
            loginForm.style.padding = '20px';
        } else {
            header.style.flexDirection = 'row';
            header.style.padding = '20px';
            Array.from(header.children).forEach(link => {
                link.style.margin = '0 20px';
            });
            loginForm.style.width = '400px';
            loginForm.style.padding = '40px';
        }
    }
    adjustLayout();
    window.addEventListener('resize', adjustLayout);
});
