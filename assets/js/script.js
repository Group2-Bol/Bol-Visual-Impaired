function enableLoadingScreen()
{
    var loadingScreenDiv = document.getElementById("loading-screen");
    if(loadingScreenDiv.style.display !== 'none')
    {
        loadingScreenDiv.style.display = 'none';
    }
    else
    {
        loadingScreenDiv.style.display = 'block';
    }
}

// button.onclick = function() 
// {
//     var div = document.getElementById("loading-screen");
//     if(div.style.screen !== 'none')
//     {
//         div.style.display = 'none';
//     }
//     else
//     {
//         div.style.display = 'block';
//     }
// }