const data = document.currentScript.dataset;
const linkToHere = data.page;

document.getElementById("share").onclick = () =>
    navigator.canShare
        ? navigator.share({ url: linkToHere })
        : alert("Your browser does not support sharing.");

document.getElementById("copy-link").onclick = () =>
    navigator.clipboard.writeText(linkToHere);
