window.onload = function() {

    document.querySelector('body').classList.remove('preload');

    document.getElementById("nav_toogle_bt").addEventListener("click", function(){
        window.alert("tes1t");
        var nav_list = document.getElementById("nav_list");
        nav_list.classList.toogle("unrolled");
    });
}
