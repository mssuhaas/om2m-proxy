# OM2M Proxy Server
This is a simple Flask application designed to act as a proxy server for interacting with OM2M platforms. It allows you to make requests to both a production OM2M server and a development OM2M server, providing a seamless interface for managing your IoT applications.

## Features
**Proxying Requests**: The server forwards requests made to its endpoints to the corresponding OM2M server, abstracting away the complexity of direct communication.

**Cross-Origin Resource Sharing (CORS)**: CORS headers are implemented to allow cross-origin requests, ensuring compatibility with web applications.

## Usage
**Installation** : Clone this repository to your local machine.

**Configuration** : Make sure to set the environment variables OM2M_ORIGIN and DEV_OM2M_ORIGIN to the URLs of your production and development OM2M servers respectively.

**Install Dependencies** : Install the required Python dependencies by running:

```bash
pip install -r requirements.txt```

Build and Run with Docker Compose: Use Docker Compose to build and run the server.

Build the Docker image and start the container:

```bash
docker-compose up --build
```
To run in detached mode:

```bash
docker-compose up -d```

Access Endpoints: Once the server is running, you can access the endpoints to interact with the OM2M servers. The endpoints are:

Production Server: http://localhost:9898/
Development Server: http://localhost:9898/dev/
Append the desired path to these URLs to make requests.

## Dependencies
Python 3.10
Flask
Flask-CORS
## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or create a pull request.


