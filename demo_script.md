# Weather Dashboard Demo Video Script

**Target Length:** 3-5 Minutes

## [0:00 - 0:30] Introduction & Setup
- **Visuals:** Title card, transitioning to the main login screen.
- **Narration:** "Hello! Welcome to the Weather Dashboard project. This is a full-stack Python Django application that allows users to create a personalized dashboard of their favorite cities and view real-time weather data. The UI is built using a modern glassmorphism design with Vanilla CSS."

## [0:30 - 1:15] Registration & Authentication
- **Visuals:** Click "Register", fill in the form with a new user (e.g., testuser1), and submit.
- **Narration:** "Let's start by creating a new account. The application uses Django's built-in authentication system to ensure all user data is secure. Once registered, we are automatically logged in and redirected to our empty dashboard."

## [1:15 - 2:00] Adding a Location (CRUD: Create)
- **Visuals:** Click "Add City". Enter a valid city like 'London' and a nickname 'Work Trip'. Click Save.
- **Narration:** "To build our dashboard, we can add a new city. Behind the scenes, a dedicated service layer validates the city name by making a request to the OpenWeatherMap API. If successful, the city is saved to our personalized list, and the UI displays a success message using the Django messages framework."

## [2:00 - 2:45] Viewing Real-Time Weather (CRUD: Read)
- **Visuals:** Dashboard showing the newly added city with its current temperature, weather icon, and conditions. Click on the city name to view details.
- **Narration:** "On the dashboard, we see the real-time weather conditions for our saved locations. By clicking on a city, we navigate to the Detail View, where we can see extended current conditions like Humidity and Wind Speed, alongside a 5-day forecast layout."

## [2:45 - 3:30] Error Handling & Validation
- **Visuals:** Go back to "Add City". Enter an invalid city name like "XYZNonExistentCity123". Hit save. Show the error message.
- **Narration:** "Robust exception handling is a core feature. If we try to add a non-existent city, the API returns a 404 error. Our service layer catches this exception and translates it into a user-friendly error message, preventing application crashes."

## [3:30 - 4:15] Editing and Deleting (CRUD: Update & Delete)
- **Visuals:** From the dashboard, click 'Edit' on the London card. Change nickname to 'Holiday'. Save. Then click 'Delete' and confirm removal.
- **Narration:** "We can easily edit the custom nickname of any saved location. Finally, if we no longer want to track a city, we can remove it. All these actions are protected by authorization logic, ensuring users can only modify their own data."

## [4:15 - 4:30] Conclusion
- **Visuals:** Log out of the application. Show the GitHub repository link and Project Report PDF briefly on screen.
- **Narration:** "The project source code, database schema, and detailed architectural report are available in the public GitHub repository. Thank you for watching!"
