# Flask Application with Geospatial Data and Pollen Information

This is a Python Flask application that serves geospatial data and pollen information. The application utilizes GeoPandas for geospatial data handling and interacts with an external API for pollen information.
The API was made for a weather app for the school project IN2000

## Features

- Flask web application serving geospatial data
- Integration with external pollen information API
- Geospatial data loading and caching
- Simple API to fetch pollen data based on coordinates

## Prerequisites

- Python 3.10
- GitHub repository for CI/CD pipeline
- Environment variables configured for geospatial data URL and API key

## Setup

1. Clone the repository:

   ```sh
   git clone https://github.com/GransMango/IN2000-regionAndPollen
   cd IN2000-regionAndPollen
   ```
2. Create a virtual environment and activate it:

   ```sh
   python -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   
   ```sh
   pip install -r requirements.txt
   ```
4. Create a `.env` file and set the required environment variables:
   
   ```env
   REGION_DATA_URL=your_region_data_url
   POLLENVARSEL_API_KEY=your_api_key
   ```
5. Run the application:

   ```sh
   python app.py
   ```

## Endpoints

- `GET /` - Renders the main page.
- `GET /pollen` - Fetches pollen data based on `lat` and `lon` query parameters.
- `GET /pollen/regions` - Fetches available pollen regions.
- `GET /find_region` - Returns norwegian city for `lat` and `lon` query parameters.

## Deployment

This project uses GitHub Actions to build and deploy the application.

### GitHub Actions Workflow

The GitHub Actions workflow is defined in `.github/workflows/main.yml`. It includes two jobs:

- `build`: Checks out the code, sets up Python, creates a virtual environment, installs dependencies, and uploads a zipped artifact for deployment.
- `deploy`: Downloads the artifact, unzips it, and deploys the application to the specified environment.

### Setup Enviornment Variables

Add the following variables to your environment:

- `REGION_DATA_URL`: The URL for the geospatial data. Can be obtained from https://www.kartverket.no/api-og-data
- `POLLENVARSEL_API_KEY`: The API key for accessing pollen information.

### Triggering Deployment

The deployment workflow triggers on push to the `main` branch or can be manually triggered via the GitHub Actions UI.
