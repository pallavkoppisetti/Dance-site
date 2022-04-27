// play video on hover

var video = document.getElementById("video");

function playPause() {
    console.log("hovering")
    //check if mouse is hovering
    if (video.paused) {
        video.play();
    }
    else {
        video.pause();
    }
}
video.addEventListener("hover", playPause);
// video.addEventListener("click", playPause, false);
// video.addEventListener("touchstart", playPause, false);