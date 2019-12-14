window.onload += function(){
    window.alert("test");
    document.getElementById("nav_toogle_bt").addEventListener("click", function(){
        window.alert("tes1t");
        var nav_list = document.getElementById("nav_list");
        nav_list.classList.toogle("unrolled");
    });
};
