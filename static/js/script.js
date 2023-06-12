document.body.style.zoom = "75%";

const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        if (entry.isIntersecting){
            entry.target.classList.add('slide');
        }
    });
})

const hidden = document.querySelectorAll('.hide')
console.log(hidden.length)

hidden.forEach((el) =>  {
    console.log(el);
    observer.observe(el);
})

var darkmode = false;

function dark() {
    if (darkmode==false){
        var body = document.getElementById("background-animation");
        body.className = "dark-body";
        var icon = document.getElementsByClassName("moon");
        icon.className = "light-logo";
        var text = document.getElementById("texts");
        text.className = "dark-text";
        var text2 = document.getElementById("text2");
        text2.className = "dark-text";
        var button = document.getElementById("button");
        button.className = "dark-button";
        var divv = document.getElementById("divv");
        divv.classList.remove("divv");
        divv.className = "dark-div";
        var moon = document.getElementById("moon");
        moon.className = "moon-black"
        var profile = document.getElementById("profile");
        profile.className = "dark-profile"
        var baymax = document.getElementById("baymax");
        baymax.className = "baymax hide";
        setTimeout(() => {
            baymax.classList.add("slide")
        }, 10);
        particlesJS.load('background-animation', 'static/particlesjs-config.json');
        darkmode =true;
    }else{
        var body = document.getElementById("background-animation");
        body.className = "light-body"
        var text = document.getElementById("texts");
        text.classList.remove("dark-text");
        var text2 = document.getElementById("text2");
        text2.classList.remove("dark-text");
        var button = document.getElementById("button");
        button.className = "light-button button";
        var divv = document.getElementById("divv");
        divv.className = "divv";
        var moon = document.getElementById("moon");
        moon.className = "moon"
        var profile = document.getElementById("profile");
        profile.className = "profile-icon"
        var baymax = document.getElementById("baymax");
        baymax.className = "baymax hide";
        setTimeout(() => {
            baymax.classList.add("slide")
        }, 10);
        particlesJS.load('background-animation', '/static/particles.json');
        darkmode = false;
    }
}