"""Consts for the myRadar."""
from __future__ import annotations
from datetime import timedelta

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntityDescription,
    SensorStateClass,
)
from homeassistant.components.weather import (
    ATTR_CONDITION_CLOUDY,
    ATTR_CONDITION_EXCEPTIONAL,
    ATTR_CONDITION_FOG,
    ATTR_CONDITION_HAIL,
    ATTR_CONDITION_LIGHTNING,
    ATTR_CONDITION_LIGHTNING_RAINY,
    ATTR_CONDITION_PARTLYCLOUDY,
    ATTR_CONDITION_POURING,
    ATTR_CONDITION_RAINY,
    ATTR_CONDITION_SNOWY,
    ATTR_CONDITION_SNOWY_RAINY,
    ATTR_CONDITION_SUNNY,
    ATTR_CONDITION_WINDY,
    ATTR_CONDITION_WINDY_VARIANT,
    ATTR_FORECAST_CONDITION,
    ATTR_FORECAST_PRECIPITATION,
    ATTR_FORECAST_PRECIPITATION_PROBABILITY,
    ATTR_FORECAST_PRESSURE,
    ATTR_FORECAST_TEMP,
    ATTR_FORECAST_TEMP_LOW,
    ATTR_FORECAST_TIME,
)
from homeassistant.const import (
    DEGREE,
    LENGTH_MILLIMETERS,
    PERCENTAGE,
    PRESSURE_HPA,
    SPEED_METERS_PER_SECOND,
    TEMP_CELSIUS,
    UV_INDEX,
    Platform,
)

DOMAIN = "myradar"
DEFAULT_NAME = "myRadar"
DEFAULT_LANGUAGE = "en"
DEFAULT_UNITS = "us"
DEFAULT_SCAN_INTERVAL = 2700
ATTRIBUTION = "Data provided by myRadar"
MANUFACTURER = "myRadar"
CONF_LANGUAGE = "language"
CONF_UNITS = "units"
CONFIG_FLOW_VERSION = 2
ENTRY_NAME = "name"
ENTRY_WEATHER_COORDINATOR = "weather_coordinator"
ATTR_API_PRECIPITATION = "precipitation"
ATTR_API_PRECIPITATION_KIND = "precipitation_kind"
ATTR_API_DATETIME = "datetime"
ATTR_API_DEW_POINT = "dew_point"
ATTR_API_WEATHER = "weather"
ATTR_API_TEMPERATURE = "temperature"
ATTR_API_FEELS_LIKE_TEMPERATURE = "feels_like_temperature"
ATTR_API_WIND_SPEED = "wind_speed"
ATTR_API_WIND_BEARING = "wind_bearing"
ATTR_API_HUMIDITY = "humidity"
ATTR_API_PRESSURE = "pressure"
ATTR_API_CONDITION = "condition"
ATTR_API_CLOUDS = "clouds"
ATTR_API_RAIN = "rain"
ATTR_API_SNOW = "snow"
ATTR_API_UV_INDEX = "uv_index"
ATTR_API_WEATHER_CODE = "weather_code"
ATTR_API_FORECAST = "forecast"
UPDATE_LISTENER = "update_listener"
PLATFORMS = [Platform.SENSOR, Platform.WEATHER]
MR_PLATFORMS = ["Sensor", "Weather"]
MR_PLATFORM = "mr_platform"
MR_PREVPLATFORM = "mr_prevplatform"
MR_ROUND = "mr_round" 

FORECAST_MODE_HOURLY = "hourly"
FORECAST_MODE_DAILY = "daily"

FORECAST_MODES = [
    FORECAST_MODE_HOURLY,
    FORECAST_MODE_DAILY,    
    ]
    
    
DEFAULT_FORECAST_MODE = FORECAST_MODE_DAILY

FORECASTS_HOURLY = "forecasts_hourly"
FORECASTS_DAILY = "forecasts_daily"

ALL_CONDITIONS = {'summary': 'Summary',
                   'icon': 'Icon',
                   'precip_type': 'Precipitation Type',
                   'precip_intensity': 'Precipitation Intensity',
                   'precip_probability': 'Precipitation Probability',
                   'precip_accumulation': 'Precipitation Accumulation',
                   'temperature': 'Temperature',
                   'apparent_temperature': 'Apparent Temperature',
                   'dew_point': 'Dew Point',
                   'humidity': 'Humidity',
                   'wind_speed': 'Wind Speed',
                   'wind_gust': 'Wind Gust',
                   'wind_bearing': 'Wind Bearing',
                   'cloud_cover': 'Cloud Cover',
                   'pressure': 'Pressure',
                   'visibility': 'Visibility',
                   'ozone': 'Ozone',
                   'minutely_summary': 'Minutely Summary',
                   'hourly_summary': 'Hourly Summary',
                   'daily_summary': 'Daily Summary',
                   'temperature_high': 'Temperature High',
                   'temperature_low': 'Temperature Low',
                   'apparent_temperature_high': 'Apparent Temperatur High',
                   'apparent_temperature_low': 'Apparent Temperature Low',
                   'precip_intensity_max': 'Precip Intensity Max',
                   'uv_index': 'UV Index',
                   'moon_phase': 'Moon Phase',
                   'sunrise_time': 'Sunrise Time',
                   'sunset_time': 'Sunset Time',
                   'nearest_storm_distance': 'Nearest Storm Distance',         
                   'nearest_storm_bearing': 'Nearest Storm Bearing',
                   'alerts': 'Alerts'                   
                }

LANGUAGES = [
    "af",
    "al",
    "ar",
    "az",
    "bg",
    "ca",
    "cz",
    "da",
    "de",
    "el",
    "en",
    "es",
    "eu",
    "fa",
    "fi",
    "fr",
    "gl",
    "he",
    "hi",
    "hr",
    "hu",
    "id",
    "it",
    "ja",
    "kr",
    "la",
    "lt",
    "mk",
    "nl",
    "no",
    "pl",
    "pt",
    "pt_br",
    "ro",
    "ru",
    "se",
    "sk",
    "sl",
    "sp",
    "sr",
    "sv",
    "th",
    "tr",
    "ua",
    "uk",
    "vi",
    "zh_cn",
    "zh_tw",
    "zu",
]
WEATHER_CODE_SUNNY_OR_CLEAR_NIGHT = 800
CONDITION_CLASSES = {
    ATTR_CONDITION_CLOUDY: [803, 804],
    ATTR_CONDITION_FOG: [701, 721, 741],
    ATTR_CONDITION_HAIL: [906],
    ATTR_CONDITION_LIGHTNING: [210, 211, 212, 221],
    ATTR_CONDITION_LIGHTNING_RAINY: [200, 201, 202, 230, 231, 232],
    ATTR_CONDITION_PARTLYCLOUDY: [801, 802],
    ATTR_CONDITION_POURING: [504, 314, 502, 503, 522],
    ATTR_CONDITION_RAINY: [300, 301, 302, 310, 311, 312, 313, 500, 501, 520, 521],
    ATTR_CONDITION_SNOWY: [600, 601, 602, 611, 612, 620, 621, 622],
    ATTR_CONDITION_SNOWY_RAINY: [511, 615, 616],
    ATTR_CONDITION_SUNNY: [WEATHER_CODE_SUNNY_OR_CLEAR_NIGHT],
    ATTR_CONDITION_WINDY: [905, 951, 952, 953, 954, 955, 956, 957],
    ATTR_CONDITION_WINDY_VARIANT: [958, 959, 960, 961],
    ATTR_CONDITION_EXCEPTIONAL: [
        711,
        731,
        751,
        761,
        762,
        771,
        900,
        901,
        962,
        903,
        904,
    ],
}
WEATHER_SENSOR_TYPES: tuple[SensorEntityDescription, ...] = (
    SensorEntityDescription(
        key=ATTR_API_WEATHER,
        name="Weather",
    ),
    SensorEntityDescription(
        key=ATTR_API_DEW_POINT,
        name="Dew Point",
        native_unit_of_measurement=TEMP_CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=ATTR_API_TEMPERATURE,
        name="Temperature",
        native_unit_of_measurement=TEMP_CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=ATTR_API_FEELS_LIKE_TEMPERATURE,
        name="Feels like temperature",
        native_unit_of_measurement=TEMP_CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=ATTR_API_WIND_SPEED,
        name="Wind speed",
        native_unit_of_measurement=SPEED_METERS_PER_SECOND,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=ATTR_API_WIND_BEARING,
        name="Wind bearing",
        native_unit_of_measurement=DEGREE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=ATTR_API_HUMIDITY,
        name="Humidity",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.HUMIDITY,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=ATTR_API_PRESSURE,
        name="Pressure",
        native_unit_of_measurement=PRESSURE_HPA,
        device_class=SensorDeviceClass.PRESSURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=ATTR_API_CLOUDS,
        name="Cloud coverage",
        native_unit_of_measurement=PERCENTAGE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=ATTR_API_RAIN,
        name="Rain",
        native_unit_of_measurement=LENGTH_MILLIMETERS,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=ATTR_API_SNOW,
        name="Snow",
        native_unit_of_measurement=LENGTH_MILLIMETERS,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=ATTR_API_PRECIPITATION_KIND,
        name="Precipitation kind",
    ),
    SensorEntityDescription(
        key=ATTR_API_UV_INDEX,
        name="UV Index",
        native_unit_of_measurement=UV_INDEX,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key=ATTR_API_CONDITION,
        name="Condition",
    ),
    SensorEntityDescription(
        key=ATTR_API_WEATHER_CODE,
        name="Weather Code",
    ),
)
FORECAST_SENSOR_TYPES: tuple[SensorEntityDescription, ...] = (
    SensorEntityDescription(
        key=ATTR_FORECAST_CONDITION,
        name="Condition",
    ),
    SensorEntityDescription(
        key=ATTR_FORECAST_PRECIPITATION,
        name="Precipitation",
        native_unit_of_measurement=LENGTH_MILLIMETERS,
    ),
    SensorEntityDescription(
        key=ATTR_FORECAST_PRECIPITATION_PROBABILITY,
        name="Precipitation probability",
        native_unit_of_measurement=PERCENTAGE,
    ),
    SensorEntityDescription(
        key=ATTR_FORECAST_PRESSURE,
        name="Pressure",
        native_unit_of_measurement=PRESSURE_HPA,
        device_class=SensorDeviceClass.PRESSURE,
    ),
    SensorEntityDescription(
        key=ATTR_FORECAST_TEMP,
        name="Temperature",
        native_unit_of_measurement=TEMP_CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
    ),
    SensorEntityDescription(
        key=ATTR_FORECAST_TEMP_LOW,
        name="Temperature Low",
        native_unit_of_measurement=TEMP_CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
    ),
    SensorEntityDescription(
        key=ATTR_FORECAST_TIME,
        name="Time",
        device_class=SensorDeviceClass.TIMESTAMP,
    ),
    SensorEntityDescription(
        key=ATTR_API_WIND_BEARING,
        name="Wind bearing",
        native_unit_of_measurement=DEGREE,
    ),
    SensorEntityDescription(
        key=ATTR_API_WIND_SPEED,
        name="Wind speed",
        native_unit_of_measurement=SPEED_METERS_PER_SECOND,
    ),
    SensorEntityDescription(
        key=ATTR_API_CLOUDS,
        name="Cloud coverage",
        native_unit_of_measurement=PERCENTAGE,
    ),
)
