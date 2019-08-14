function check () {

  var question1 = document.quiz.question1.value;
  var question2 = document.quiz.question2.value;
  var question3 = document.quiz.question3.value;
  var question4 = document.quiz.question4.value;
  var question5 = document.quiz.question5.value;
  var question6 = document.quiz.question6.value;
  var question7 = document.quiz.question7.value;
  var question8 = document.quiz.question8.value;
  var question9 = document.quiz.question9.value;
  var question10 = document.quiz.question10.value;
  var question11 = document.quiz.question11.value;
  var question12 = document.quiz.question12.value;
  var question13 = document.quiz.question13.value;
  var question14 = document.quiz.question14.value;
  var question15 = document.quiz.question15.value;
  var question16 = document.quiz.question16.value;
  var question17 = document.quiz.question17.value;
  var question18 = document.quiz.question18.value;
  var question19 = document.quiz.question19.value;
  var question20 = document.quiz.question20.value;
  var score = 0;

    if (question1 == "0"){
      score+=2;
    }
    else if (question1 == "1-2"){
      score++;
    }
    if (question2 == "Walk"){
      score+=2;
    }
    else if (question2 == "Bike"){
      score++;
    }
    if (question3 == "I don't consume meat"){
      score+=2;
    }
    else if (question3 == "1 time"){
      score++;
    }
    if (question4 == "Dishwasher"){
      score+=2;
    }
    else if (question4 == "Both"){
      score++;
    }
    if (question5 == "5 minutes or less"){
      score+=2;
    }
    else if (question5 == "6-15 minutes"){
      score++;
    }
    if (question6 == "Few times a year"){
      score+=2;
    }
    else if (question6 == "Once a month"){
      score++;
    }
    if (question7 == "Always"){
      score+=2;
    }
    else if (question7 == "Sometimes"){
      score++;
    }
    if (question8 == "Always"){
      score+=2;
    }
    else if (question8 == "Sometimes"){
      score++;
    }
    if (question9 == "I drive an electric car"){
      score+=2;
    }
    else if (question9 == "40+"){
      score++;
    }
    if (question10 == "Once a month"){
      score+=2;
    }
    else if (question10 == "Once a week"){
      score++;
    }
    if (question11 == "I bring it to Advanced Auto Parts for recycling"){
      score+=2;
    }
    else if (question11 == "I recycle it myself"){
      score++;
    }
    if (question12 == "Yes, I bring my own reusable bag each time"){
      score+=2;
    }
    else if (question12 == "I sometimes bring my own bags"){
      score++;
    }
    if (question13 == "Never"){
      score+=2;
    }
    else if (question13 == "Few times a year"){
      score++;
    }
    if (question14 == "Yes"){
      score+=2;
    }
    else if (question14 == "I used to"){
      score++;
    }
    if (question15 == "No, I always use them in my compost"){
      score+=2;
    }
    else if (question15 == "I sometimes add them to my compost"){
      score++;
    }
    if (question16 == "Always"){
      score+=2;
    }
    else if (question16 == "Sometimes"){
      score++;
    }
    if (question17 == "Never"){
      score+=2;
    }
    else if (question17 == "Rarely"){
      score++;
    }
    if (question18 == "Always"){
      score+=2;
    }
    else if (question18 == "Sometimes"){
      score++;
    }
    if (question19 == "Always"){
      score+=2;
    }
    else if (question19 == "Sometimes"){
      score++;
    }
    if (question20 == "LED bulbs"){
      score+=2;
    }
    else if (question20 == "Fluorescent bulbs"){
      score++;
    }

var fScore = (score/40) * 100;
var finalScore = fScore.toFixed(0);

var results = ["Awesome! You've proven yourself to be an environmentally-conscious person, so keep up the good work!",
  "Overall, you're doing a good job in preserving our environment, but there's always room for improvement:",
  "While this low score means you're not helping the state of our planet, there are always ways to improve."
];

var range;

  if (score >= 20){
    range = 0;
  }
  else if (score >= 10 && score < 20){
    range = 1;
  }
  else {
    range = 2;
  }

  document.getElementById("after_submit").style.visibility = "visible";

  document.getElementById("message").innerHTML = results[range];
  document.getElementById("score").innerHTML = "You are "+finalScore+"% eco-friendly!";
}
