// function console_log(event){
//     event.preventDefault();

//     const textPromptInput = document.getElementById("text_prompt").value;
//     console.log(textPromptInput);

// }
document.addEventListener("DOMContentLoaded", function() {
    // Get a reference to the form and button elements
    const form = document.querySelector("form");
    const textPromptInput = document.getElementById("text_prompt").value;
    const generateVideoButton = document.querySelector("button[type='submit']");
    
    // Add an event listener for form submission
    form.addEventListener("submit", function(event) {
        event.preventDefault(); // Prevent the default form submission
        
        // Get the value of the text input
        const textPromptValue = textPromptInput;
        console.log(textPromptValue);

        // Perform client-side validation 
        if (textPromptValue.trim() === "") {
            alert("Please enter a text prompt.");
            return; // Exit the function early if validation fails
        }

        // Make an AJAX request to the server
        fetch("/generate_video", {
            method: "POST",
            headers: {
                "Content-Type": "text/plain" 
            },
            body: textPromptValue
        })
        .then(response => response.json())
        .then(data => {
            // Handle the response from the server
            // For demonstration purposes, we'll just log the response to the console
            console.log(data);
            // Display a message or perform other actions
            // alert("Video generation request submitted successfully!");
            // // UI with the generated video URL or other information
            // // display the video in the video container
            // const videoContainer = document.getElementById("video_container");
            // videoContainer.innerHTML = `<video controls src="${data.video_url}" width="320" height="240">Your browser does not support the video tag.</video>`;
        })
        .catch(error => {
            // Handle errors
            console.error("Error:", error);
            // Display an error message
            alert("An error occurred while generating the video. Please try again later.");
        });
    });
});
