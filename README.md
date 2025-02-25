# AI Chat Application

A modern chat application powered by AI that allows users to interact with various AI models through a clean and intuitive interface.

## Features

- Interactive chat interface
- Support for multiple AI models
- Real-time responses
- Message history tracking
- Environment variable configuration
- User-friendly Streamlit interface

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## Installation

1. Clone the repository:

bash
git clone <repository-url>
cd <repository-name>

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install required dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
   - Copy `.env.example` to `.env`
   - Fill in your API keys and other required variables

## Configuration

Create a `.env` file in the root directory with the following variables:
```
API_KEY=your_api_key_here
# Add other required environment variables
```

## Usage

1. Start the application:
```bash
streamlit run streamlit_app.py
```

2. Open your web browser and navigate to the URL shown in the terminal (typically `http://localhost:8501`)

3. Begin chatting with the AI by typing your message in the input field and pressing Enter

## Project Structure

```
.
├── README.md
├── requirements.txt
├── .env.example
├── .env
├── streamlit_app.py
└── app.py
```

<!-- ## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Create a Pull Request -->

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Thanks to the Streamlit team for their excellent framework
- All contributors and users of this project

## Support

For support, please open an issue in the GitHub repository or contact the maintainers.