const quizData = [
  {
    question: "Are you self-employed?",
    a: "yes",
    b: "No",
  },
  {
    question: "Do you have a family history of mental illness?",
    a: "yes",
    b: "No",
  },
  {
    question: "Have you sought treatment for a mental health condition?",
    a: "yes",
    b: "No",
  },
  {
    question:
      " If you have a mental health condition, do you feel that it interferes with your work?",
    a: "often",
    b: "Sometimes",
    c: "Rarely",
    d: "Never",
    e: "Don't know",
  },
  {
    question: "How many employees does your company or organization have?",
    a: "1-5",
    b: "6-25",
    c: "26-100",
    d: "100-500",
    e: "500-1000",
    f: "1000<",
  },
  {
    question: "Do you work remotely (outside of an office) at least 50% of the time?",
    a: "yes",
    b: "No",
  },
  {
    question: "Is your employer primarily a tech company/organization?",
    a: "yes",
    b: "No"
  },
  {
    question: "Does your employer provide mental health benefits?",
    a: "yes",
    b: "No",
    c:"Don't Know"
  },
  {
    question:
      "Do you know the options for mental health care your employer provides?",
      a: "yes",
      b: "No",
      c:"Not sure"
  },
  {
    question:
      "Has your employer ever discussed mental health as part of an employee wellness program?",
      a: "yes",
      b: "No",
      c:"Don't Know"
  },
  {
    question:
      "Does your employer provide resources to learn more about mental health issues and how to seek help?",
      a: "yes",
      b: "No",
      c:"Don't Know"
  },
  {
    question:
      "Is your anonymity protected if you choose to take advantage of mental health or substance abuse treatment resources?",
      a: "yes",
      b: "No",
      c:"Don't Know"
  },
  {
    question:
      "How easy is it for you to take medical leave for a mental health condition?",
    a: "Very easy",
    b: "Some what easy",
    c: "Some what difficult",
    d: "Very Difficult",
    e: "Dont Know"
  },
  {
    question:
      "Do you think that discussing a mental health issue with your employer would have negative consequences?",
      a: "yes",
      b: "No",
      c:"Maybe"
  },
  {
    question:
      ":Do you think that discussing a physical health issue with your employer would have negative consequences?",
      a: "yes",
      b: "No",
      c:"Maybe"
  },
  {
    question:
      "Do you think that discussing a physical health issue with your employer would have negative consequences?",
      a: "yes",
      b: "No",
      c:"Maybe"
  },
  {
    question:
      "Would you be willing to discuss a mental health issue with your coworkers??",
      a: "yes",
      b: "No",
      c:"some of them"
  },
  {
    question:
      "Would you be willing to discuss a mental health issue with your direct supervisor(s)?",
      a: "yes",
      b: "No",
      c:"some of them"
  },
  {
    question:
      "Would you bring up a mental health issue with a potential employer in an interview?",
      a: "yes",
      b: "No",
      c:"Maybe"
  },
  {
    question:
      "Would you bring up a physical health issue with a potential employer in an interview?",
      a: "yes",
      b: "No",
      c:"Maybe"
  },
 
  {
    question:
      "Do you feel that your employer takes mental health as seriously as physical health?",
      a: "yes",
      b: "No",
      c:"Don't know"
  },
  {
    question:
      "Have you heard of or observed negative consequences for coworkers with mental health conditions in your workplace?",
      a: "yes",
      b: "No",
  },
 
];

const quiz = document.getElementById("quiz");
const answerEls = document.querySelectorAll(".answer");
const questionEl = document.getElementById("question");
const a_text = document.getElementById("a_text");
const b_text = document.getElementById("b_text");
const c_text = document.getElementById("c_text");
const d_text = document.getElementById("d_text");
const submitBtn = document.getElementById("submit");

const answers= {}

loadQuiz();

function loadQuiz() {
  deselectAnswers();

  const currentQuizData = quizData[currentQuiz];

  questionEl.innerText = currentQuizData.question;
  a_text.innerText = currentQuizData.a;
  b_text.innerText = currentQuizData.b;
  c_text.innerText = currentQuizData.c;
  d_text.innerText = currentQuizData.d;
}

function deselectAnswers() {
  answerEls.forEach((answerEl) => (answerEl.checked = false));
}

function getSelected() {
  let answer;
  answerEls.forEach((answerEl) => {
    if (answerEl.checked) {
      answer = answerEl.id;
    }
  });
  return answer;
}

submitBtn.addEventListener("click", () => {
  const answer = getSelected();
  if (answer) {
    if (answer === quizData[currentQuiz].correct) {
      score++;
    }

    currentQuiz++;

    if (currentQuiz < quizData.length) {
      loadQuiz();
    } else {
      quiz.innerHTML = `
         <h2>You answered ${score}/${quizData.length} questions correctly</h2>

         <button onclick="location.reload()">Reload</button>
         `;
    }
  }
});


//
