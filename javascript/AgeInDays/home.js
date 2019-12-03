// Age in days

function age() {
    var birthYear = prompt("What year were you born in?");
    var ageInDays = (2019 - birthYear) * 365;
    var h1 = document.createElement('h1');
    var textAnswer = document.createTextNode('You are ' + ageInDays + ' days old');
    h1.setAttribute('id', 'ageInDays');
    h1.appendChild(textAnswer);
    document.getElementById('flex-box-results').appendChild(h1);
    console.log(ageInDays);
}

function reset() {
    document.getElementById('ageInDays').remove();
}