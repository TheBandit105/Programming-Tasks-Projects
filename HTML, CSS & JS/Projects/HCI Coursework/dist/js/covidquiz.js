
window.onload = function() {
    show(0)
}

let questions = [
    {
        id: 1,
        question: " How is COVID-19 transmitted from person to person?",
        answer: "Via the droplets that come from your mouth and nose when you cough or breathe out",
        options: [
            "Via the droplets that come from your mouth and nose when you cough or breathe out",
            "In sexual fluids, such as semen",
            "By drinking unclean water",
            "All of the above"
        ]
    },
    {
        id: 2,
        question: " What are the common symptoms of COVID-19?",
        answer: "All of the above",
        options: [
            "A new and continuous cough",
            "Fever",
            "Tiredness",
            "All of the above"
        ]
    },
    {
        id: 3,
        question: " Is it always possible to know if someone has COVID-19?",
        answer: "No - not everyone with COVID-19 has symptoms",
        options: [
            "No - not everyone with COVID-19 has symptoms",
            "Yes - it's obvious, a person with COVID-19 coughs a lot",
            "Yes - you can tell just by where a person comes from, their race and ethnicity",
            "All of the above"
        ]
    },
    {
        id: 4,
        question: " Which of the following can help protect you from catching COVID-19?",
        answer: "All of the above",
        options: [
            "Soap and water",
            "Hand sanitizer",
            "Cover your mouth and nose with a tissue or your sleeve (not your hands)",
            "All of the above"
        ]
    },
    {
        id: 5,
        question: " Which of the following groups of people are more vunerable to COVID-19?",
        answer: "Older people (70+ yrs) and people with certain underlying conditions",
        options: [
            "Children",
            "Older people (70+ yrs) and people with certain underlying conditions",
            "European people",
            "All of the above"
        ]
    },
    {
        id: 6,
        question: " Where did COVID-19 originate from?",
        answer: "Wuhan, China",
        options: [
            "Mexico City, Mexico",
            "Tokyo, Japan",
            "Wuhan, China",
            "Colombo, Sri Lanka"
        ]
    },
    {
        id: 7,
        question: " Currently, is there a cure for COVID-19?",
        answer: "No - However, most people eventually recover",
        options: [
            "No - Vaccine currently being developed",
            "No - Will take ages before one is developed",
            "Yes - Widely available",
            "No - However, most people eventually recover"
        ]
    },
    {
        id: 8,
        question: " When should face masks be worn?",
        answer: "All of the above",
        options: [
            "When on public transport",
            "When in confined or crowded areas",
            "In small shops",
            "All of the above"
        ]
    },
    {
        id: 9,
        question: " When going out, what is the minimum distance you should be from someone?",
        answer: "2 meters",
        options: [
            "1 meter",
            "2 meters",
            "3 meters",
            "You can be right next to the person"
        ]
    },
    {
        id: 10,
        question: " How can those with HIV protect themselves from COVID-19?",
        answer: "All of the above",
        options: [
            "Wash their hands regularly and follow social distancing advice",
            "Exercise regularly, eat well and look after their mental health",
            "Keep taking their antiretroviral treatment",
            "All of the above"
        ]
    },
]


function submitForm(e){
    e.preventDefault();
    let name = document.forms["welcome_form"]["name"].value;

    sessionStorage.setItem("name", name);

    if(name == false){
        location.href ="quizstart.html";
    } else {
        location.href ="quizmain.html";
    }
    
}

let question_count = 0;
let point = 0;

function next() {

    let user_answer = document.querySelector("li.option.active").innerHTML;

    if(user_answer == questions[question_count].answer) {
        point += 1;
        sessionStorage.setItem("points", point);
       }
    
    if(question_count == questions.length - 1){
        sessionStorage.setItem("time", `${minutes} minutes and ${seconds} seconds`);
        clearInterval(mytime);
        if (point > 5){
            location.href = "end.html";
        } else {
            location.href = "end2.html";
        }
        return;
    }
    
    question_count++;
    show(question_count);
}

function previous() {
}

function show(count) {
    let question = document.getElementById("questions");

    // question.innerHTML = "<h2>" + questions[count].question + "</h2>";
    question.innerHTML = `
    <h2>Q${question_count+1}.${questions[count].question}</h2>
    <ul class="option_group">
    <li class="option">${questions[count].options[0]}</li>
    <li class="option">${questions[count].options[1]}</li>
    <li class="option">${questions[count].options[2]}</li>
     <li class="option">${questions[count].options[3]}</li>
    </ul>
    `;

    toggleActive();
}

function toggleActive() {
    let option = document.querySelectorAll("li.option");

    for(let i = 0; i < option.length; i++) {
        option[i].onclick = function(){
            for(let j = 0; j < option.length; j++) {
                if(option[j].classList.contains("active")) {
                    option[j].classList.remove("active");
                } 
            }
            option[i].classList.add("active");
        }
    }
}
