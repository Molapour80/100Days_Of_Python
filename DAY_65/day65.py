import requests
import json
import time
from datetime import datetime
import random
from flask import Flask, render_template_string, jsonify

class TrafficReporter:
    def __init__(self):
        self.cities = ["Tehran", "Mashhad", "Isfahan", "Shiraz", "Tabriz", "Karaj"]
        self.areas = {
            "Tehran": ["Enghelab Square", "Valiasr Square", "Tajrish", "Vanak", "Sadeghieh"],
            "Mashhad": ["Azadi Square", "Ahmad Abad", "Haft Tir", "Kooh Sangi", "Falakhe Ab"],
            "Isfahan": ["Imam Hossein Square", "Chahar Bagh", "Azadi Square", "Pol Felezi", "Naqsh-e Jahan Square"],
            "Shiraz": ["Eram Square", "Molla Sadra", "Quran Gate", "Falakhe Gaz", "Setar Khan"],
            "Tabriz": ["Shahid Beheshti Square", "Baghlestan", "Maralan Square", "Baghmi-sheh", "Abrasan Square"],
            "Karaj": ["Shohada Square", "Gohardasht", "Mehrshahr", "Azimieh", "Falakhe Aval Tehran"]
        }
        self.traffic_levels = ["Light", "Moderate", "Heavy", "Congested"]
        
    def get_traffic_data(self, city=None, area=None):
        """
        Get traffic data for a specific city or area
        In a real implementation, this would connect to a traffic API
        """
        if city and city not in self.cities:
            return {"error": "City not found"}
        
        # Simulate traffic data
        traffic_data = {}
        
        if city and area:
            if area not in self.areas.get(city, []):
                return {"error": "Area not found"}
            
            # Report for a specific area
            traffic_data[area] = {
                "level": random.choice(self.traffic_levels),
                "speed": random.randint(5, 60),
                "update_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
        elif city:
            # Report for all areas in a city
            for area in self.areas[city]:
                traffic_data[area] = {
                    "level": random.choice(self.traffic_levels),
                    "speed": random.randint(5, 60),
                    "update_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
        else:
            # Report for all cities
            for city in self.cities:
                traffic_data[city] = {}
                for area in self.areas[city]:
                    traffic_data[city][area] = {
                        "level": random.choice(self.traffic_levels),
                        "speed": random.randint(5, 60),
                        "update_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    }
        
        return traffic_data
    
    def display_traffic_report(self, traffic_data):
        """Display traffic report in a readable format"""
        if "error" in traffic_data:
            print(f"Error: {traffic_data['error']}")
            return
            
        for location, data in traffic_data.items():
            if isinstance(data, dict) and "level" in data:
                # This is an area
                print(f"{location}: {data['level']} traffic - Average speed: {data['speed']} km/h")
            else:
                # This is a city with multiple areas
                print(f"\n=== Traffic in {location} ===")
                for area, area_data in data.items():
                    print(f"{area}: {area_data['level']} traffic - Average speed: {area_data['speed']} km/h")
    
    def get_traffic_alerts(self, city=None):
        """Get important traffic alerts"""
        alerts = []
        
        # Simulate traffic alerts
        possible_alerts = [
            "Accident on the route",
            "Road closed",
            "Road maintenance in progress",
            "Demonstration taking place",
            "Snowfall and icy conditions"
        ]
        
        if city:
            alerts.append(f"{city}: {random.choice(possible_alerts)}")
        else:
            for city in random.sample(self.cities, 2):
                alerts.append(f"{city}: {random.choice(possible_alerts)}")
                
        return alerts
    
    def get_traffic_from_api(self, city):
        """
        Get real traffic data from an API (example using a hypothetical API)
        You would need to replace with a real traffic API
        """
        try:
            # This is a placeholder for a real API call
            # Example: response = requests.get(f"https://traffic-api.com/{city}")
            # return response.json()
            
            # Simulating API response
            return {
                "level": random.choice(self.traffic_levels),
                "speed": random.randint(5, 60),
                "update_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
        except Exception as e:
            return {"error": f"API request failed: {str(e)}"}

# Web application using Flask
app = Flask(__name__)
traffic_reporter = TrafficReporter()

# HTML template as a string
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Traffic Status Report</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        h1 {
            color: #2c3e50;
            text-align: center;
        }
        .city-selector {
            margin: 20px 0;
            text-align: center;
        }
        select {
            padding: 10px;
            font-size: 16px;
            border-radius: 4px;
            border: 1px solid #ddd;
        }
        .traffic-card {
            background-color: #f9f9f9;
            border-left: 5px solid #3498db;
            padding: 15px;
            margin: 10px 0;
            border-radius: 4px;
        }
        .traffic-light { border-left-color: #2ecc71; }
        .traffic-moderate { border-left-color: #f39c12; }
        .traffic-heavy { border-left-color: #e74c3c; }
        .traffic-congested { border-left-color: #c0392b; }
        .alert {
            background-color: #ffeaa7;
            border-left: 5px solid #fdcb6e;
            padding: 15px;
            margin: 10px 0;
            border-radius: 4px;
        }
        .loading {
            text-align: center;
            padding: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1><i class="fas fa-traffic-light"></i> Traffic Status Report</h1>
        
        <div class="city-selector">
            <select id="citySelector" onchange="loadTrafficData()">
                <option value="all">All Cities</option>
                {% for city in cities %}
                <option value="{{ city }}">{{ city }}</option>
                {% endfor %}
            </select>
        </div>
        
        <div id="trafficData">
            <div class="loading">
                <i class="fas fa-spinner fa-spin"></i> Loading traffic data...
            </div>
        </div>
        <div id="alerts"></div>
    </div>

    <script>
        function loadTrafficData() {
            const city = document.getElementById('citySelector').value;
            document.getElementById('trafficData').innerHTML = '<div class="loading"><i class="fas fa-spinner fa-spin"></i> Loading traffic data...</div>';
            
            fetch(`/api/traffic/${city}`)
                .then(response => response.json())
                .then(data => {
                    displayTrafficData(data, city);
                })
                .catch(error => {
                    document.getElementById('trafficData').innerHTML = `<div class="alert">Error loading data: ${error}</div>`;
                });
            
            fetch('/api/alerts')
                .then(response => response.json())
                .then(alerts => {
                    displayAlerts(alerts);
                })
                .catch(error => {
                    console.error('Error loading alerts:', error);
                });
        }
        
        function displayTrafficData(data, city) {
            const container = document.getElementById('trafficData');
            container.innerHTML = '';
            
            if (data.error) {
                container.innerHTML = `<div class="alert">${data.error}</div>`;
                return;
            }
            
            if (city === 'all') {
                for (const [city, areas] of Object.entries(data)) {
                    const cityHeader = document.createElement('h2');
                    cityHeader.textContent = `Traffic in ${city}`;
                    container.appendChild(cityHeader);
                    
                    for (const [area, info] of Object.entries(areas)) {
                        container.appendChild(createTrafficCard(area, info));
                    }
                }
            } else {
                for (const [area, info] of Object.entries(data)) {
                    container.appendChild(createTrafficCard(area, info));
                }
            }
            
            if (Object.keys(data).length === 0) {
                container.innerHTML = '<div class="alert">No traffic data available</div>';
            }
        }
        
        function createTrafficCard(area, info) {
            const card = document.createElement('div');
            let trafficClass = 'traffic-moderate';
            
            if (info.level === 'Light') trafficClass = 'traffic-light';
            else if (info.level === 'Heavy') trafficClass = 'traffic-heavy';
            else if (info.level === 'Congested') trafficClass = 'traffic-congested';
            
            card.className = `traffic-card ${trafficClass}`;
            card.innerHTML = `
                <h3>${area}</h3>
                <p><strong>Status:</strong> ${info.level} traffic</p>
                <p><strong>Average speed:</strong> ${info.speed} km/h</p>
                <p><strong>Last update:</strong> ${info.update_time}</p>
            `;
            
            return card;
        }
        
        function displayAlerts(alerts) {
            const container = document.getElementById('alerts');
            container.innerHTML = '';
            
            if (alerts.length > 0) {
                const header = document.createElement('h2');
                header.textContent = 'Traffic Alerts';
                container.appendChild(header);
                
                alerts.forEach(alert => {
                    const alertDiv = document.createElement('div');
                    alertDiv.className = 'alert';
                    alertDiv.innerHTML = `<i class="fas fa-exclamation-triangle"></i> ${alert}`;
                    container.appendChild(alertDiv);
                });
            }
        }
        
        // Load data on page load
        window.onload = loadTrafficData;
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE, cities=traffic_reporter.cities)

@app.route('/api/traffic/<city>')
def get_city_traffic(city):
    if city == 'all':
        data = traffic_reporter.get_traffic_data()
    else:
        data = traffic_reporter.get_traffic_data(city)
    return jsonify(data)

@app.route('/api/alerts')
def get_alerts():
    alerts = traffic_reporter.get_traffic_alerts()
    return jsonify(alerts)

def main():
    """Console application for traffic reporting"""
    reporter = TrafficReporter()
    
    while True:
        print("\n" + "="*50)
        print("Traffic Status Reporting Application")
        print("="*50)
        print("1. Show traffic for all cities")
        print("2. Show traffic for a specific city")
        print("3. Show traffic for a specific area")
        print("4. Show traffic alerts")
        print("5. Exit")
        
        choice = input("\nPlease select an option: ")
        
        if choice == "1":
            traffic_data = reporter.get_traffic_data()
            reporter.display_traffic_report(traffic_data)
            
        elif choice == "2":
            print("\nAvailable cities:")
            for i, city in enumerate(reporter.cities, 1):
                print(f"{i}. {city}")
            
            try:
                city_idx = int(input("\nSelect city number: ")) - 1
                if 0 <= city_idx < len(reporter.cities):
                    traffic_data = reporter.get_traffic_data(reporter.cities[city_idx])
                    reporter.display_traffic_report(traffic_data)
                else:
                    print("Invalid city number.")
            except ValueError:
                print("Please enter a number.")
                
        elif choice == "3":
            print("\nAvailable cities:")
            for i, city in enumerate(reporter.cities, 1):
                print(f"{i}. {city}")
            
            try:
                city_idx = int(input("\nSelect city number: ")) - 1
                if 0 <= city_idx < len(reporter.cities):
                    city = reporter.cities[city_idx]
                    print(f"\nAvailable areas in {city}:")
                    for i, area in enumerate(reporter.areas[city], 1):
                        print(f"{i}. {area}")
                    
                    area_idx = int(input("\nSelect area number: ")) - 1
                    if 0 <= area_idx < len(reporter.areas[city]):
                        traffic_data = reporter.get_traffic_data(city, reporter.areas[city][area_idx])
                        reporter.display_traffic_report(traffic_data)
                    else:
                        print("Invalid area number.")
                else:
                    print("Invalid city number.")
            except ValueError:
                print("Please enter a number.")
                
        elif choice == "4":
            alerts = reporter.get_traffic_alerts()
            print("\nTraffic alerts:")
            for alert in alerts:
                print(f"⚠️  {alert}")
                
        elif choice == "5":
            print("Exiting application...")
            break
            
        else:
            print("Invalid option. Please try again.")
        
        # Pause before showing menu again
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    # Run web application by default
    print("Starting web server...")
    print("Open your browser and go to http://localhost:5000")
    app.run(debug=True)
    
    # To run the console application instead, comment the above lines
    # and uncomment the line below:
    # main()