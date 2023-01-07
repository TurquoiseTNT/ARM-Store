function install(app) {
    customprompt("Installing "+ app, "<iframe src='" + ip + ":5000/installapp/" + app + "'>", lightgrey)
}
function remove(app) {
    location.href = ip + ':5000/removeapp/' + app;
}