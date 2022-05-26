API_key = 'df31701d9e14e739584302181e80b918'

function getWeather(city)
{
    fetch(`https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${API_key}`)
    .then(response => response.json())
    .then(response => {
        temperature = response.main
        weather = response.weather[0]
        if(document.getElementById('temp_scale').value == 'c')
        {
            document.getElementById('today_weather').innerHTML = 'Current Weather: ' + (temperature.temp - 273.15).toFixed(1)
            document.getElementById('today_high').innerHTML = 'High: ' + (temperature.temp_max - 273.15).toFixed(1)
            document.getElementById('today_low').innerHTML = 'Low: ' + (temperature.temp_min - 273.15).toFixed(1)
            document.getElementById('weather_description').innerHTML = weather.description
        }
        else if(document.getElementById('temp_scale').value == 'f')
        {
            document.getElementById('today_weather').innerHTML = 'Current Weather: ' + Math.round((temperature.temp - 273.15) * 9/5 + 32)
            document.getElementById('today_high').innerHTML = 'High: ' + Math.round((temperature.temp_max - 273.15) * 9/5 + 32)
            document.getElementById('today_low').innerHTML = 'Low: ' + Math.round((temperature.temp_min - 273.15) * 9/5 + 32)
        }
        

    })
    .catch(err => console.log(err))
    console.log(city)
}

newCity = document.querySelector('#city_link')

newCity.addEventListener('click', function(event){
    event.preventDefault()
    // console.log(document.getElementById('#city_link'))
    // info = getWeather(document.querySelector('#city_link').value)
})

temp_scale = document.querySelector('#temp_scale')
temp_scale.addEventListener('change', (event) =>{
    getWeather(city)
})