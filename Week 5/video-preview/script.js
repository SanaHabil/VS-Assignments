console.log("page loaded...");




function video_mute(){
    document.getElementById("myVideo").defaultMuted = true;
    document.getElementById("myVideo").muted = true;
    document.getElementById("myVideo").play();
}

function video_unmute(){
    document.getElementById("myVideo").muted = false;
    document.getElementById("myVideo").pause();
}