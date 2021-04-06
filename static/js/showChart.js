var myVar;

function displycharts() {
    if (window.location.href.includes('stock-analysis')) {
        document.getElementById('chart2').style.display = "display";
        document.getElementById('chart1').style.display = "none";
        document.getElementById('analysis-btn').style.display = "none";
    }
    else {
        document.getElementById('chart2').style.display = "none";
        document.getElementById('chart1').style.display = "display";
        document.getElementById('analysis-btn').style.display = "display";
    }
}




function loaderhide() {
    document.getElementById("loader").style.display = "none";
}

// function myFunction() {
//     myVar = setTimeout(showPage, 3000);
// }

// function showPage() {
//     document.getElementById("loader").style.display = "none";
//     document.getElementById("analysischart").style.display = "block";
// }