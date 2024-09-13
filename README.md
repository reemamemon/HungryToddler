# Hungry Toddler Candy Tracker

This project simulates a scenario where a toddler interacts with pieces of candy, tracking the time each piece is picked up and eaten. The simulation records these actions and generates a report with timestamps.

## Features
- Tracks candy interactions (e.g., picked up, eaten) with timestamps.
- Allows the user to run a candy simulation and download the event log as a CSV file.
- Provides a user-friendly interface built using **Streamlit**.
- Deployed on Hugging Face Spaces.

## Live Demo
You can access the live demo of the application [here](https://huggingface.co/spaces/reemamemon/HungryToddler).

## Installation

### Local Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/reemamemon/HungryToddler.git
    cd HungryToddler
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

4. Open `http://localhost:8501` in your browser to view the app.

### Deployed Version

The app is deployed on **Hugging Face Spaces**. You can try it out by visiting [this link](https://huggingface.co/spaces/reemamemon/HungryToddler).

## How to Use

- Click on the "Run Candy Simulation" button to start the simulation.
- The app will display a table with the candy interactions and corresponding timestamps.
- You can download the report as a CSV file using the **Download CSV** button.

## Technologies Used
- **Streamlit**: For building the web interface.
- **Pandas**: For data handling and reporting.
- **Hugging Face Spaces**: For deployment.

## Files
- `app.py`: Main application code for Streamlit.
- `requirements.txt`: Python dependencies required for the app.
- `README.md`: Documentation for the project.

## Future Improvements
- Add more interactive features, such as customizable simulations (e.g., the number of candies).
- Visualize the events using graphs or animations.
