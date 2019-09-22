document.addEventListener('DOMContentLoaded', () => {
    const contactForm = document.getElementById('contact-form');
    const envelope = document.getElementById('envelope');
    const formInputs = document.getElementById('form-inputs');

    function togglePlaystate(element) {
        if (element.style.animationPlayState === 'running') {
            element.style.animationPlayState = 'paused'
        } else {
            element.style.animationPlayState = 'running';
        }

    }

    contactForm.addEventListener('submit', e => {
        e.preventDefault()
        
        contactForm.addEventListener('animationend', (e) => {
            console.log(e.animationName);
            // Collapse the form height when the send-envelope animation ends
            if (e.animationName === 'send-envelope') {
                // formInputs.classList.add('collapsed');
                formInputs.style.maxHeight = 0;
            }
        });
        // Start drawing the envelope and fade the form inputs away
        envelope.classList.add('send-envelope');
        formInputs.classList.add('hide-form');
        
        
        
    })

})