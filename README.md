# Agentic Research Assistant and Writer

## Overview
This Streamlit application utilizes CrewAI to generate well-researched and engaging blog posts based on user-provided topics. The app employs AI-driven agents to perform research and content writing, ensuring high-quality and fact-based content generation.

## Features
- **AI-Powered Research & Writing**: Uses multiple AI agents to research and synthesize information.
- **User-Defined Topics**: Accepts custom topics for content generation.
- **Temperature Control**: Allows fine-tuning of the LLM's creativity.
- **Markdown Formatting**: Generates well-structured blog posts in markdown format.
- **Downloadable Output**: Enables users to download the generated content.
- **Interactive UI**: Simple and user-friendly interface with intuitive controls.

## How It Works
The application follows a multi-agent workflow:
1. **User Input**: Users enter a topic in the text area and adjust the LLM temperature setting if needed.
2. **Agent Execution**:
   - The **Senior Research Analyst** gathers relevant and reliable information.
   - The **Content Writer** transforms the research into a well-structured blog post.
3. **Output Display**: The generated content is displayed in the main content area.
4. **Download Option**: Users can download the output in markdown format.

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- Streamlit
- CrewAI
- OpenAI API Key (or compatible LLM API key)

### Setup Steps
1. **Clone the Repository**
```bash
 git clone <repository-url>
 cd <project-directory>
```
2. **Create a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
```
3. **Install Dependencies**
```bash
pip install -r requirements.txt
```
4. **Set Up Environment Variables**
Create a `.env` file in the root directory and add:
```ini
GEMINI_API_KEY=your_api_key_here
```
5. **Run the Application**
```bash
streamlit run app.py
```

## Application Workflow
### **1. Sidebar Controls**
- **Enter Topic**: Users input a topic for content generation.
- **Temperature Slider**: Adjusts the creativity level of the LLM.
- **Generate Content Button**: Starts the content creation process.
- **Help Section**: A step-by-step guide on how to use the app.

### **2. AI Agents**
- **Senior Research Analyst**
  - Conducts in-depth research.
  - Evaluates sources for credibility.
  - Summarizes findings with references.

- **Content Writer**
  - Converts research into a structured blog post.
  - Ensures readability and engagement.
  - Uses proper markdown formatting.

### **3. Output and Download**
- Generated content is displayed in markdown format.
- Users can download the article for further use.

## File Structure
```
project-directory/
│── app.py               # Main Streamlit application
│── requirements.txt     # List of dependencies
│── .env                 # Environment variables (not tracked in Git)
│── README.md            # Documentation
```

## Troubleshooting
- **Invalid API Key**: Ensure the `.env` file contains a valid LLM API key.
- **No Output Generated**: Check the entered topic and try again.
- **Error Messages**: Check logs and Streamlit console output for debugging.

## Future Enhancements
- **Add an Editing Agent**: To refine the generated content.
- **SEO Optimization**: Improve blog posts for better search engine visibility.
- **Customizable Formatting**: Allow users to adjust structure and tone settings.

## Credits
Built using **Streamlit, CrewAI, and OpenAI’s LLMs**.

## License
This project is licensed under the [MIT License](LICENSE).

