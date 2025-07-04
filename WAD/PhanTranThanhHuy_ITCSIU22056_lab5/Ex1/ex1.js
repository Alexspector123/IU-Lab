document.querySelector('.register')
            .addEventListener('click', () => {
                const email = document.querySelector('.email');
                const phone = document.querySelector('.phone');
                const country = document.querySelector('.country').value;
                const terms = document.querySelector('.terms');

                let box = document.querySelector('.notify');

                let notify = '';
                if (!email.value || !phone.value || country === '' || !terms.checked) {
                    notify += '<ul>';
                    if (!email.value) {
                        notify += '<li>Please enter a valid email address.</li>';
                        document.querySelector('.email-dot').innerHTML = '*';
                    }
                    else if(!email.checkValidity()){
                        notify += '<li>Please enter correct email</li>'
                        document.querySelector('.email-dot').innerHTML = '*';
                    }
                    if (!phone.value) {
                        notify += '<li>Please enter a valid phone number.</li>';
                        document.querySelector('.phone-dot').innerHTML = '*';
                    } else if(!phone.checkValidity()){
                        notify += '<li>Please enter correct phone number</li>'
                        document.querySelector('.phone-dot').innerHTML = '*';
                    }
                    if (country === '') {
                        notify += '<li>Please select a country.</li>';
                        document.querySelector('.country-dot').innerHTML = '*';
                    }
                    if (!terms.checked) {
                        notify += '<li>You must agree to the terms of service.</li>';
                        document.querySelector('.terms-dot').innerHTML = '*';
                    }
                    notify += '</ul>';
                    box.classList.add('invalid-box');
                }
                if(notify === '') {
                    notify = 'Registration successful!';
                    box.classList.add('valid-box');
                }
                box.innerHTML = notify;
            });

document.querySelector('.reset')
            .addEventListener('click', () => {
                document.querySelector('.email').value = '';
                document.querySelector('.phone').value = '';
                document.querySelector('.country').value = '';
                document.querySelector('.terms').checked = '';
            });