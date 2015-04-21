devices = [
    {
        'name':'SW1',
        'friendly_name': 'Bedroom Light',
        'id': 1
    },
    {
        'name':'SW2',
        'friendly_name': 'Kitchen Light',
        'id': 2
    }
]

from homeassistant.const import STATE_ON, STATE_OFF, DEVICE_DEFAULT_NAME
import requests

class NrfDevice(object):
    """docstring for NrfDevice"""
    def __init__(self, device):
        super(NrfDevice, self).__init__()
        self._name = device['name']
        self._friendly_name = device['friendly_name']
        self._id = device['id']
        self._state = STATE_OFF

    def turn_on(self):
        # Send signal to turn on 
        # return yes or no
        print("=================================")
        print(self._name)
        print(self._id)
        print("Yay I tried to turn on this")
        print("=================================")
        reqStr = str(self._id) + "N"
        print("request: ",reqStr)
        r = requests.get("http://192.168.2.4:1000/" + reqStr)
        print("response: ", r.text)
        if r.text == str(self._id)+'1\n':
            self._state = STATE_ON
        return True

    def turn_off(self):
        # Send signal to turn on 
        # return yes or no

        print("=================================")
        print(self._name)
        print("Yay I tried to turn off this")
        print("=================================")
        reqStr = str(self._id) + "F"
        r = requests.get("http://192.168.2.4:1000/" + reqStr)
        print("response: ", r.text)
        if r.text == str(self._id)+'0\n':
            self._state = STATE_OFF
        return True

    @property
    def state(self):
        # get state
        return self._state

    @property
    def friendly_name(self):
        # get friendly_name
        return self._friendly_name
     
    @property
    def is_on(self):
        return self._state == STATE_ON

    @property
    def name(self):
        """ Returns the name of the device if any. """
        return self._name


def get_devices():
    return [NrfDevice(device) for device in devices]
