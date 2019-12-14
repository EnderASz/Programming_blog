window.onload = function(){
    document.getElementById("nav_toogle_bt").addEventListener("click", function(){
        var nav_list = document.getElementById("nav_list");
        nav_list.classList.toogle("unrolled");
    });
};
