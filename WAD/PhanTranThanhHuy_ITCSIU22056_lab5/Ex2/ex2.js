document.querySelector('.box')
    .addEventListener('click', () => {

        let new_content = `The remainning time: 0:<span id="timer">60</span> [mm:ss]`;
        document.querySelector('.box').innerHTML = new_content;

        document.querySelector('.test').innerHTML = `
            <h3>These are test questions.</h3>
            <div class="input">
                <p>Question 1: How many people are there in your class?</p>
                <input type="number">
            </div>
            <div class="input">
                <p>Question 2: How do you feel now?</p>
                <input type="radio" id="good" name="feeling" value="GOOD">
                <label for="good-feeling">Good</label>
                <input type="radio" id="bad" name="feeling" value="BAD">
                <label for="bad-feeling">Bad</label>
            </div>
        `;

        let count = 60;
        let timerElement = document.getElementById("timer");
    
        let interval = setInterval(() => {
            count--; 
            timerElement.textContent = count; 
            
            if (count === 0) {
                clearInterval(interval); 
                document.querySelector('.time').innerHTML = '';
                document.querySelector('.test').innerHTML = `
            <div class="time-up">
                <h3>Time is up!!!</h3>
                <button class="box">Submit your answers</button>
            </div>`;
            }
        }, 1000);

    });

