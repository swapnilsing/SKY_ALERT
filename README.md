# 🌩️ Sky Alert | Advanced Weather Intelligence Platform

   

**Sky Alert** is a next-generation weather intelligence dashboard designed to deliver hyper-local forecasting with a cinematic user experience. Built with a dual-mode architecture, it seamlessly bridges high-performance frontend visuals with a robust, caching-enabled backend proxy.

The application features a proprietary **Particle Engine** for real-time atmospheric simulation (rain, snow, thunder), a **Glassmorphism UI** for modern aesthetics, and integrated **Voice Command** capabilities.

-----

## 📑 Table of Contents

  - [✨ Key Features](https://www.google.com/search?q=%23-key-features)
  - [🏗️ Technical Architecture](https://www.google.com/search?q=%23-technical-architecture)
  - [🛠️ Technology Stack](https://www.google.com/search?q=%23-technology-stack)

-----

## IMAGES


FRONT PAGE : <img width="1919" height="866" alt="Screenshot 2025-12-03 230714" src="https://github.com/user-attachments/assets/f604e31a-7d4c-4916-b102-4969efc1100a" />


SIGN UP PAGE: 

<img width="523" height="760" alt="Screenshot 2025-12-03 231102" src="https://github.com/user-attachments/assets/3c429e50-63c9-4a8a-bfaf-28f9fda6f506" />




LOGIN PAGE: 

<img width="523" height="587" alt="Screenshot 2025-12-03 231157" src="https://github.com/user-attachments/assets/aea9dba4-482c-47cc-b07c-37957f5ef187" />


MAIN WEBSITE:

<img width="1918" height="858" alt="Screenshot 2025-12-03 231256" src="https://github.com/user-attachments/assets/a3a97205-fb7b-42cf-975d-023a74db5f43" />

ADVANCED DASHBOARD:

<img width="1570" height="703" alt="Screenshot 2025-12-03 231627" src="https://github.com/user-attachments/assets/db441893-f38f-41f8-ab2a-252813f971d6" />



## ✨ Key Features

### 🎨 Immersive UI/UX

  * **Cinematic "Storm & Reveal" Intro:** A custom CSS animation sequence that transitions from a dark, high-impact loading state to the main dashboard.
  * **Dynamic Background Layering:** An automated "Ken Burns" effect system that fetches and transitions between high-resolution background imagery based on live weather conditions.
  * **HTML5 Canvas Particle Engine:** A custom-written JavaScript engine that renders 60FPS atmospheric effects (Rain, Snow, Stars) directly on the canvas layer.
  * **Glassmorphism Design:** Utilizes `backdrop-filter: blur()` and semi-transparent RGBA layers to create depth and hierarchy.

### 🧠 Intelligent Functionality

  * **Dual-Mode Connectivity:**
      * **Direct Mode:** Client-side API calls for rapid prototyping and serverless deployment.
      * **Proxy Mode:** Routes requests through a Python/Flask backend to secure API keys and implement caching.
  * **Smart Insights Engine:** Algorithms that analyze raw weather data to generate actionable advice (e.g., "Wear Check," "Umbrella Alerts").
  * **Voice Search Integration:** Leveraging the **Web Speech API** for hands-free city searching.
  * **Data Persistence:** Supports Firebase (Cloud Sync) or LocalStorage (Mock Mode) for saving user preferences and favorite locations.

### 📊 Comprehensive Data Visualization

  * **24-Hour Trend Analysis:** Interactive line charts powered by **Chart.js**.
  * **Advanced Metrics:** Real-time monitoring of:
      * US EPA Air Quality Index (AQI) with visual progress bars.
      * UV Index, Pressure (mb), Visibility (km).
      * Sunrise, Sunset, Moon Phase, and Illumination percentage.
  * **Export Capabilities:** Client-side generation of CSV reports using `Blob` objects.

-----

## 🏗️ Technical Architecture

Sky Alert implements a **Client-Server-API** pattern but retains the flexibility to run as a **Single-Page Application (SPA)**.

### Backend (Python/Flask)

  * **Proxy Server:** Acts as a middleware between the client and the WeatherAPI to prevent API Key leakage in production environments.
  * **In-Memory Caching:** Implements a custom caching logic that stores API responses for 15 minutes (`CACHE_DURATION_SECONDS`), significantly reducing API usage quotas and latency for repeated requests.
  * **CORS Handling:** Configured via `flask_cors` to allow secure cross-origin resource sharing.

### Frontend (Vanilla JS + Tailwind)

  * **Component-Less Architecture:** Uses direct DOM manipulation for maximum performance without the overhead of heavy frameworks like React or Vue for this specific use case.
  * **ES6 Modules:** Javascript logic is modularized (imports/exports) for maintainability.
  * **Service Integration:**
      * **Firebase SDK v11.6:** Handles Authentication (Email/Password) and Firestore (NoSQL DB).
      * **Geolocation API:** Native browser API for precise user positioning.
      * **Speech Synthesis:** Browser-native text-to-speech for audio weather reports.

-----

## 🛠️ Technology Stack

| Category | Technology | Usage |
| :--- | :--- | :--- |
| **Frontend** | HTML5, CSS3 | Semantic markup and animations |
| **Styling** | **Tailwind CSS** | Utility-first styling framework |
| **Scripting** | **JavaScript (ES6+)** | Core logic, DOM manipulation, Async/Await |
| **Visuals** | **HTML5 Canvas API** | High-performance particle rendering |
| **Charts** | **Chart.js** | Data visualization libraries |
| **Backend** | **Python 3.x** | Server-side logic |
| **Framework** | **Flask** | Micro-framework for the proxy server |
| **Database** | **Firebase Firestore** | NoSQL cloud database (Optional) |
| **Auth** | **Firebase Auth** | User identity management |
| **API** | **WeatherAPI.com** | Meteorological data provider |

-----

*© 2025 Sky Alert. Distributed under the MIT License.*
