function closeNavSaga () {
    document.getElementById("hidden-saga").style.width="0";
    document.getElementById("hidden-saga").style.zIndex="0"
    document.getElementById("main").style.marginLeft="0";
}

function closeNavYear () {
    document.getElementById("hidden-year").style.width="0";
    document.getElementById("hidden-year").style.zIndex="0"
    document.getElementById("main").style.marginLeft="0";
}

function openNavYear () {
    document.getElementById("hidden-year").style.width="250px";
    document.getElementById("hidden-year").style.zIndex="1"
    document.getElementById("main").style.marginLeft="250px";
}

function openNavSaga () {
    document.getElementById("hidden-saga").style.width="250px";
    document.getElementById("hidden-saga").style.zIndex="1"
    document.getElementById("main").style.marginLeft="250px";
}