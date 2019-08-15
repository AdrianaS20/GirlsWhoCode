function check () {

  var question1 = document.quizLeft.question1.value;
  var question2 = document.quizLeft.question2.value;
  var question3 = document.quizLeft.question3.value;
  var question4 = document.quizLeft.question4.value;
  var question5 = document.quizLeft.question5.value;
  var question6 = document.quizLeft.question6.value;
  var question7 = document.quizLeft.question7.value;
  var question8 = document.quizLeft.question8.value;
  var question9 = document.quizLeft.question9.value;
  var question10 = document.quizLeft.question10.value;
  var question11 = document.quizRight.question11.value;
  var question12 = document.quizRight.question12.value;
  var question13 = document.quizRight.question13.value;
  var question14 = document.quizRight.question14.value;
  var question15 = document.quizRight.question15.value;
  var question16 = document.quizRight.question16.value;
  var question17 = document.quizRight.question17.value;
  var question18 = document.quizRight.question18.value;
  var question19 = document.quizRight.question19.value;
  var question20 = document.quizRight.question20.value;
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
    if (question11 == "Always"){
      score+=2;
    }
    else if (question11 == "Sometimes"){
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
    if (question15 == "I use rechargable batteries"){
      score+=2;
    }
    else if (question15 == "I put them in my freezer"){
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

var fScore = (score/30) * 100;
var finalScore = fScore.toFixed(0);

var results = [
  "Awesome! You've proven yourself to be an environmentally-conscious person, so keep up the good work! Meanwhile, check out our page 'How You Can Help' to read about other ways you could continue benefitting the environment.",
  "Overall, you're doing a good job in preserving our environment, but there's always room for improvement. To read about other ways you can be more eco-friendly check out our page 'How You Can Help'",
  "Sadly, your habits are not doing any favors to the state of our planet, so it's best to check out our page 'How You Can Help' to learn about eco-friendly living before it's too late."
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
