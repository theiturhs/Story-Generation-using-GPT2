# Story-Generation-using-GPT2

### Objective
Creatify Stories is a Flask application that uses AI to generate short stories based on user inputs. The primary goal of the application is to allow users to creatively express ideas by providing a prompt, which the AI then expands into a narrative. This project showcases how artificial intelligence can be integrated into web applications to enhance user creativity and engagement.

### Features
- User-Friendly Interface: The application has a clean and intuitive UI built with Bootstrap, making it accessible for all users.
- Text Generation: Utilizes the GPT-2 model from Hugging Face's Transformers library to generate coherent stories based on user prompts.
- Loading Animation: Displays a loading spinner while the story is being generated, improving user experience during processing delays.
- Responsive Design: The application is responsive and works seamlessly on various devices.

### UI of the application

![UI](https://github.com/user-attachments/assets/1d52004a-71d0-4584-a088-64a53c0c69e5)

### Demo Video


https://github.com/user-attachments/assets/accd49b9-08ff-4597-9c40-9bf7e4aaac9c



### Technologies Used
- Frontend: HTML, CSS (Bootstrap), JavaScript
- Backend: Flask (Python)
- AI Model: GPT-2 from Hugging Face Transformers

### Installation
Follow these steps to set up the project locally:

1. Clone the Repository:
```
git clone https://github.com/theiturhs/Story-Generation-using-GPT2.git
cd Story-Generation-using-GPT2
```

2. Create a Virtual Environment (optional but recommended)
```
python -m venv venv
venv\Scripts\activate
```

3. Run the Application:
```
python App.py
```

4. Access the Application:
```
Open your web browser and go to http://127.0.0.1:8000.
```

### Usage

1. Input a prompt in the provided text area. For example: "I was wondering what if I..."
2. Click the "Create Story" button.
3. Wait for the AI to generate a story (the loading spinner will indicate that the process is ongoing).
4. Once generated, the story will be displayed below the input form.

### Code Explanation
1. Flask Backend: The backend is powered by Flask, which handles HTTP requests and renders HTML templates.
2. generate_story function: Processes the user input and generates a story using the generate_text function from the textGenerationCode module.
3. Text Generation: The generate_text function uses the Hugging Face Transformers pipeline to generate text based on the user's prompt.
4. HTML Template: The front end is styled using Bootstrap for a modern and responsive design. It includes a form for user input and a section to display the generated story.

### References
- [HuggingFace - GPT2](https://huggingface.co/openai-community/gpt2)

### Contact
For any inquiries or feedback, feel free to reach out:

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/shrutikshrivastava/)
[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:shrutishrivastava22ss@gmail.com)
[![Carrd](https://img.shields.io/badge/carrd-000000?style=for-the-badge&logo=carrd&logoColor=white)]([https://theiturhs.carrd.co/](https://shrutishrivastava.carrd.co/))
[![Kaggle](https://img.shields.io/badge/kaggle-0077B5?style=for-the-badge&logo=kaggle&logoColor=white)](https://www.kaggle.com/theiturhs)
[![GitHub](https://img.shields.io/badge/github-000000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/theiturhs)
