# AI-Powered Cold Email Generator

This project is an AI-powered cold email generator designed for service companies. It utilizes Groq's language model, LangChain, and Streamlit to create personalized cold emails based on job listings and user information.

## Features

- Interactive user input for personal and company information
- Job listing extraction from company career pages
- Personalized cold email generation
- Integration with a vector database for relevant portfolio links
- User-friendly interface built with Streamlit

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7+
- Groq API key (obtain from https://console.groq.com/keys)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/cold-email-generator.git
   cd cold-email-generator
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up your Groq API key:
   - Create a `.env` file in the `app` directory
   - Add your Groq API key to the file:
     ```
     GROQ_API_KEY=your_api_key_here
     ```

## Usage

To run the Streamlit app:

```
streamlit run app/main.py
```

Then, follow these steps in the app:

1. Enter your personal information
2. Provide the URL of the company's careers page
3. The app will extract job listings from the given URL
4. Select a job listing to generate a personalized cold email
5. Review and customize the generated email as needed

## Project Structure

```
cold-email-generator/
├── app/
│   ├── main.py
│   └── .env
├── requirements.txt
└── README.md
```

## Contributing

Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Groq for providing the language model API
- LangChain for the AI framework
- Streamlit for the user interface

## Contact

If you have any questions or feedback, please open an issue in the GitHub repository.
