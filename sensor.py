import logging
from sgp30 import SGP30
from homeassistant.helpers.entity import Entity

_LOGGER = logging.getLogger(__name__)

def initialize_sgp30():
    """Initialize the SGP30 sensor."""
    sgp30 = SGP30()
    sgp30.start_measurement()
    return sgp30

class SGP30Sensor(Entity):
    """Representation of an SGP30 Sensor."""

    def __init__(self, name, sgp30, sensor_type):
        """Initialize the sensor."""
        self._name = name
        self._sgp30 = sgp30
        self._sensor_type = sensor_type
        self._state = None

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement."""
        if self._sensor_type == "eCO2":
            return "ppm"
        elif self._sensor_type == "TVOC":
            return "ppb"
        return None

    def update(self):
        """Fetch data from the sensor."""
        try:
            if self._sensor_type == "eCO2":
                self._state = self._sgp30.get_air_quality().equivalent_co2
            elif self._sensor_type == "TVOC":
                self._state = self._sgp30.get_air_quality().total_voc
        except Exception as e:
            _LOGGER.error(f"Error updating {self._name}: {e}")

def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the SGP30 sensor platform."""
    sgp30 = initialize_sgp30()

    entities = [
        SGP30Sensor("SGP30 eCO2", sgp30, "eCO2"),
        SGP30Sensor("SGP30 TVOC", sgp30, "TVOC")
    ]
    add_entities(entities)