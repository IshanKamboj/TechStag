var file = document.getElementById("file");

function check_empty() {
    if (file.files.length == 0) 
    {
        return true;
    } 
    else 
    {
        return false;
    }
}
