document.onload = function(){
    document.getElementById("nav_toogle_bt").addEventListener("click", function(){
        print("dupa");
        var nav_list = document.getElementById("nav_list");
        nav_list.classList.toogle("unrolled");
    });
};
