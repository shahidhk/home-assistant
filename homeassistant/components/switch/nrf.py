""" Demo platform that has two fake switchces. """
from homeassistant.helpers.entity import ToggleEntity
from homeassistant.const import STATE_ON, STATE_OFF, DEVICE_DEFAULT_NAME

from homeassistant.external.nrf import nrf as nrf
from homeassistant.external.nrf.nrf import NrfDevice as NrfDevice


# pylint: disable=unused-argument
def setup_platform(hass, config, add_devices_callback, discovery_info=None):
    """ Find and return demo switches. """
    add_devices_callback([
        NrfSwitch(device) for device in nrf.get_devices()
    ])


class NrfSwitch(ToggleEntity):
    """ Provides a demo switch. """
    def __init__(self, nrf_device):
        self.nrf_device = nrf_device
        self._friendly_name = nrf_device.friendly_name
        
    @property
    def should_poll(self):
        """ No polling needed for a demo switch. """
        return False

    @property
    def name(self):
        """ Returns the name of the device if any. """
        return self.nrf_device.name

    @property
    def friendly_name(self):
        """ Returns the friendly_name of the device if any. """
        return self.nrf_device.friendly_name

    @property
    def state(self):
        """ Returns the name of the device if any. """
        return self.nrf_device.state

    @property
    def is_on(self):
        """ True if device is on. """
        return self.nrf_device.is_on()

    def turn_on(self, **kwargs):
        """ Turn the device on. """
        self.nrf_device.turn_on()

    def turn_off(self, **kwargs):
        """ Turn the device off. """
        self.nrf_device.turn_off()
