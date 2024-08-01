# Technical Documentation

## Introduction

The web application, built with Flask, serves as an educational tool designed to enhance the process of learning English. This site features over 8000 commonly used English words, providing detailed information along with visual aids sourced from Google Images. This documentation outlines the core functionalities, project structure, and essential technical details.

## Functionality

1. **Word Display**
   The site presents users with information about a random word from the database, including:
   - The word itself
   - Phonetic transcription
   - Russian translation

2. **Image Visualization**
   Each word is accompanied by an image retrieved from Google search results. This feature enriches the learning experience by providing visual associations to aid in word retention.

## Project Components

- **`app.py`**: The main Flask script that handles routing and template rendering.
- **`templates/index.html`**: The HTML template that displays the word information and associated image.
- **`static/`**: Directory for storing static files, such as images.

## Technical Details

1. **Flask and Jinja2**
   - Flask is used to develop the web application, while Jinja2 handles HTML templating. Routes are defined in `app.py`, and templates are located in the `templates` directory.

2. **Image Retrieval with icrawler**
   - The `icrawler` library is utilized to fetch images from Google.

3. **Running the Project**
   - Execute the following command:
     ```bash
     python app.py
     ```
   - The site will then be accessible at [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## Conclusion

The developed web application offers a unique educational experience by integrating word information with visual imagery, providing a user-friendly interface for learners. This site is a valuable tool for both beginners and those looking to deepen their language skills.
