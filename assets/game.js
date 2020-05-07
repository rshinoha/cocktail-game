function buildQuiz() {
    const output = [];

    questions.forEach(
        (currentQuestion, questionNumber) => {
            const answers = [];

            for(choice in currentQuestion.answers){
                // adds checkboxes
                answers.push(
                    `<div class="form-check col-6">\n\t<input class="form-check-input" type="checkbox" name="option${questionNumber}" id="check${questionNumber}" value="">\n\t<label class="form-check-label" for="check${questionNumber}">\n\t${currentQuestion.answers[choice]}\n\t</label>\n</div>\n`
                );
            }

            output.push(
                `<div class="question col-12 p-0"><h2>${currentQuestion.question}</h2></div>\n${answers.join('')}`
            );
    });

    console.log(output.join(''))

    quizContainer.innerHTML = output.join('');
}

// function showResults() {

// }

const quizContainer = document.querySelector('#quiz');
// const resultsContainer = document.querySelector('results');
// const submitButton = document.querySelector('submit');
// const nextCocktainButton = document.querySelector('next');
// Temporary alcohol and ingredients objects for initial setup

let alcohol = {
    0: "Blended whisky",
    1: "Vodka",
    2: "Tequila",
    3: "Bourbon",
    4: "Sake",
    5: "Shochu"
};

let other = {
    0: "Lime",
    1: "Lemon",
    2: "Cherry",
    3: "Coconut",
    4: "Tomato juice",
    5: "Sugar"
};

// Temporary drinks object for initial setup
let drink = {
    strDrink: "Frisco Sour",
    alcoholIDList: [0, 1],
    otherIDList: [0, 1],
    strDrinkThumb: "https://www.thecocktaildb.com/images/media/drink/acuvjz1582482022.jpg",
    link: "https://www.thecocktaildb.com/drink/11382"
};

const questions = [
    {
        question: "Alcohol",
        answers: {
            0: alcohol[0],
            1: alcohol[1],
            2: alcohol[2],
            3: alcohol[3],
            4: alcohol[4],
            5: alcohol[5]
        },
        correctAnswers: drink["alcoholIDList"]
    },
    {
        question: "Other ingredients",
        answers: {
            0: other[0],
            1: other[1],
            2: other[2],
            3: other[3],
            4: other[4],
            5: other[5]
        },
        correctAnswers: drink["otherIDList"]
    }

];

if(quizContainer){
    console.log("ok");
}
else{
    console.log("issue");
}
buildQuiz();

// submitButton.addEventListener('click', showResults);