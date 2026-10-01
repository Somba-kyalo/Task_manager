document.addEventListener("DOMContentLoaded", function () {
    console.log("TaskApp loaded successfully!");

    //simple confirmation prompt on delete buttons
    const deleteLinks = document.querySelectorAll(".actions a.delete");
    
    deleteLinks.forEach(function (link) {
        link.addEventListener("click", function (event) {
            
            const confirmed = confirm("Are you sure you want to proceed with this action?");
            if (!confirmed) {
                event.preventDefault(); // Stop navigation if cancelled
            }
        });
    });
});