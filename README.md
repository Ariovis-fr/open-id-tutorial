# OpenID Connect Flask Integration with Keycloak

This repository demonstrates how to integrate OpenID Connect authentication into a Python Flask application using **Keycloak** as the identity provider.

It walks you through:

- Setting up a Keycloak server with Docker
- Registering an OpenID client
- Building and organizing a scalable Flask application
- Implementing a secure OpenID Connect login flow
- Retrieving user information
- Implementing logout and route protection

## 🧰 Prerequisites

- Python 3.11+
- Docker + Docker Compose

## 📦 Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Ariovis-fr/open-id-tutorial.git
   cd open-id-tutorial
   ```

2. Start Keycloak using Docker:

   ```bash
   docker-compose up
   ```

   This launches a Keycloak instance accessible at `http://localhost:8080`.

3. Set up your environment variables:

   Create a `.env` file at the root of the project:

   ```env
   OIDC_CLIENT_ID=your-client-id
   OIDC_CLIENT_SECRET=your-client-secret
   OIDC_AUTHORITY=http://localhost:8080/realms/your-realm
   REDIRECT_URI=http://localhost:8081/auth/signin
   SECRET_KEY=your-secret-key
   ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Running the Application

```bash
flask --app app run --debug --port=8081
```

Visit [http://localhost:8081](http://localhost:8081) in your browser.

## 🧱 Project Structure

```plaintext
.
├── app
│   ├── auth
│   ├── extensions
│   ├── main
│   ├── static
│   └── templates
├── config.py
├── docker-compose.yaml
├── .env
└── README.md
```

## 🔐 Features

-  OpenID Connect authentication using Keycloak
-  Session management with Flask-Session
-  User information display
-  Secure login & logout
-  Route protection with decorators
-  Modular Flask app structure

## 🧪 Test It

1. Navigate to [http://localhost:8081/auth/login](http://localhost:8081/auth/login)
2. Log in via Keycloak
3. Return to your Flask app with authenticated user data

## 📚 Learn More

- [OpenID Connect](https://openid.net/developers/how-connect-works/)
- [Keycloak Docs](https://www.keycloak.org/guides)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Real Python - Decorators](https://realpython.com/primer-on-python-decorators/)

## 📎 Related

This repository accompanies the blog article:  
**[How to Connect a Python Flask App to Keycloak with OpenID Connect](https://github.com/Ariovis-fr/open-id-tutorial)**