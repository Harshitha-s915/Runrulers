# Runrulers

# “FoodLink: Bridging Surplus Food to Hungry Communities”

## Overview

This platform connects surplus food donors (hostels, restaurants, events) with NGOs to help minimize food waste and feed those in need. Built in Python using Flask, it supports secure authentication, live donation/status tracking, safety checks, and comprehensive logging—all with a friendly web UI.

## Features

- **Easy food donation registration**  
  Donors can quickly enter surplus food available for pickup.

- **NGO/Recipient dashboard**  
  View, claim, and track donations in real-time.

- **Status workflow**  
  Donations move from Available → Picked Up → Delivered.

- **Safety checks**  
  Mark items as “passed” before pickup/delivery.

- **Authentication**  
  Simple user login/logout; only logged-in users can access features.

- **Donation logs**  
  Track all donation actions for transparency.


## Tech Stack

- Backend: Python 3.x, Flask
- Frontend: HTML, CSS, JavaScript
- Session management for authentication
- Can be extended with PostgreSQL, React, Docker for production


## How To Run

1. **Clone or download this repository**

2. **Install Python dependencies**  
   ```
   pip install flask
   ```

3. **Start the server**  
   ```
   python app.py
   ```

4. **Open your browser at:**  
   ```
   http://127.0.0.1:5000/
   ```

5. **Login credentials (demo):**  
   ```
   admin / password123
   ngo   / ngo123
   ```


## API Endpoints

- **POST /add_food**  
  Add surplus food donation

- **GET /list_food**  
  View all food donations

- **POST /update_status**  
  Change status to picked up/delivered

- **POST /safety_check**  
  Mark safety as passed

- **GET /donation_logs**  
  View donation history


## Project Structure

```
├── app.py
├── templates/
│   ├── index.html
│   └── login.html
├── README.md
```


## Future Extensions

- Role-based access for donors vs NGOs
- Mobile app interface
- Analytics dashboard: food rescued, impact, etc
- City-wide/country-wide scaling

