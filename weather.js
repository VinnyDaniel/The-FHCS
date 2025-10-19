const GOOGLE_MAPS_API_KEY = "YOUR_API_KEY";

// Function to get lat/lon from user input location
async function getLatLong(location) {
  const geoUrl = `https://maps.googleapis.com/maps/api/geocode/json?address=${encodeURIComponent(location)}&key=${GOOGLE_MAPS_API_KEY}`;
  const geoResponse = await fetch(geoUrl);
  const geoData = await geoResponse.json();
  if (geoData.status === "OK") {
    const { lat, lng } = geoData.results[0].geometry.location;
    return { lat, lng };
  } else {
    throw new Error("Location not found");
  }
}

// Function to get current weather and forecast for the lat/lon
async function getWeather(lat, lng) {
  const weatherUrl = `https://weather.googleapis.com/v1/currentConditions:lookup?key=${GOOGLE_MAPS_API_KEY}&location.latitude=${lat}&location.longitude=${lng}`;
  const response = await fetch(weatherUrl);
  const data = await response.json();
  return data;  // Contains current weather details like temperature, condition, humidity, etc.
}

// Main flow: ask user for location, get weather data, display it
async function showWeatherForLocation(userInputLocation) {
  try {
    const { lat, lng } = await getLatLong(userInputLocation);
    const weatherData = await getWeather(lat, lng);
    console.log(`Current temperature in ${userInputLocation}: ${weatherData.temperature.degrees}°${weatherData.temperature.unit}`);
    console.log(`Condition: ${weatherData.weatherCondition.description.text}`);
    // You can extend this to display forecast data similarly using forecast API endpoint
  } catch (error) {
    console.error("Error:", error.message);
  }
}
