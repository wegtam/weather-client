# -*- coding: utf-8 -*-
#############################################################
# This file was automatically generated on 2013-09-11.      #
#                                                           #
# Bindings Version 2.0.11                                    #
#                                                           #
# If you have a bugfix for this file and want to commit it, #
# please fix the bug in the generator. You can find a link  #
# to the generator git on tinkerforge.com                   #
#############################################################

try:
    from collections import namedtuple
except ImportError:
    try:
        from .ip_connection import namedtuple
    except ValueError:
        from ip_connection import namedtuple

try:
    from .ip_connection import Device, IPConnection, Error
except ValueError:
    from ip_connection import Device, IPConnection, Error

GetCurrentCallbackThreshold = namedtuple('CurrentCallbackThreshold', ['option', 'min', 'max'])
GetIdentity = namedtuple('Identity', ['uid', 'connected_uid', 'position', 'hardware_version', 'firmware_version', 'device_identifier'])

class BrickletIndustrialDual020mA(Device):
    """
    Device for sensing two currents between 0 and 20mA (IEC 60381-1)
    """

    DEVICE_IDENTIFIER = 228

    CALLBACK_CURRENT = 10
    CALLBACK_CURRENT_REACHED = 11

    FUNCTION_GET_CURRENT = 1
    FUNCTION_SET_CURRENT_CALLBACK_PERIOD = 2
    FUNCTION_GET_CURRENT_CALLBACK_PERIOD = 3
    FUNCTION_SET_CURRENT_CALLBACK_THRESHOLD = 4
    FUNCTION_GET_CURRENT_CALLBACK_THRESHOLD = 5
    FUNCTION_SET_DEBOUNCE_PERIOD = 6
    FUNCTION_GET_DEBOUNCE_PERIOD = 7
    FUNCTION_SET_SAMPLE_RATE = 8
    FUNCTION_GET_SAMPLE_RATE = 9
    FUNCTION_GET_IDENTITY = 255

    THRESHOLD_OPTION_OFF = 'x'
    THRESHOLD_OPTION_OUTSIDE = 'o'
    THRESHOLD_OPTION_INSIDE = 'i'
    THRESHOLD_OPTION_SMALLER = '<'
    THRESHOLD_OPTION_GREATER = '>'
    SAMPLE_RATE_240_SPS = 0
    SAMPLE_RATE_60_SPS = 1
    SAMPLE_RATE_15_SPS = 2
    SAMPLE_RATE_4_SPS = 3

    def __init__(self, uid, ipcon):
        """
        Creates an object with the unique device ID *uid* and adds it to
        the IP Connection *ipcon*.
        """
        Device.__init__(self, uid, ipcon)

        self.api_version = (2, 0, 0)

        self.response_expected[BrickletIndustrialDual020mA.FUNCTION_GET_CURRENT] = BrickletIndustrialDual020mA.RESPONSE_EXPECTED_ALWAYS_TRUE
        self.response_expected[BrickletIndustrialDual020mA.FUNCTION_SET_CURRENT_CALLBACK_PERIOD] = BrickletIndustrialDual020mA.RESPONSE_EXPECTED_TRUE
        self.response_expected[BrickletIndustrialDual020mA.FUNCTION_GET_CURRENT_CALLBACK_PERIOD] = BrickletIndustrialDual020mA.RESPONSE_EXPECTED_ALWAYS_TRUE
        self.response_expected[BrickletIndustrialDual020mA.FUNCTION_SET_CURRENT_CALLBACK_THRESHOLD] = BrickletIndustrialDual020mA.RESPONSE_EXPECTED_TRUE
        self.response_expected[BrickletIndustrialDual020mA.FUNCTION_GET_CURRENT_CALLBACK_THRESHOLD] = BrickletIndustrialDual020mA.RESPONSE_EXPECTED_ALWAYS_TRUE
        self.response_expected[BrickletIndustrialDual020mA.FUNCTION_SET_DEBOUNCE_PERIOD] = BrickletIndustrialDual020mA.RESPONSE_EXPECTED_TRUE
        self.response_expected[BrickletIndustrialDual020mA.FUNCTION_GET_DEBOUNCE_PERIOD] = BrickletIndustrialDual020mA.RESPONSE_EXPECTED_ALWAYS_TRUE
        self.response_expected[BrickletIndustrialDual020mA.FUNCTION_SET_SAMPLE_RATE] = BrickletIndustrialDual020mA.RESPONSE_EXPECTED_FALSE
        self.response_expected[BrickletIndustrialDual020mA.FUNCTION_GET_SAMPLE_RATE] = BrickletIndustrialDual020mA.RESPONSE_EXPECTED_ALWAYS_TRUE
        self.response_expected[BrickletIndustrialDual020mA.CALLBACK_CURRENT] = BrickletIndustrialDual020mA.RESPONSE_EXPECTED_ALWAYS_FALSE
        self.response_expected[BrickletIndustrialDual020mA.CALLBACK_CURRENT_REACHED] = BrickletIndustrialDual020mA.RESPONSE_EXPECTED_ALWAYS_FALSE
        self.response_expected[BrickletIndustrialDual020mA.FUNCTION_GET_IDENTITY] = BrickletIndustrialDual020mA.RESPONSE_EXPECTED_ALWAYS_TRUE

        self.callback_formats[BrickletIndustrialDual020mA.CALLBACK_CURRENT] = 'B i'
        self.callback_formats[BrickletIndustrialDual020mA.CALLBACK_CURRENT_REACHED] = 'B i'

    def get_current(self, sensor):
        """
        Returns the current of the specified sensor (0 or 1). The value is in nA
        and between 0nA and 22505322nA (22.5mA).
        
        It is possible to detect if an IEC 60381-1 compatible sensor is connected
        and if it works probably.
        
        If the returned current is below 4mA, there is likely no sensor connected
        or the sensor may be defect. If the returned current is over 20mA, there might
        be a short circuit or the sensor may be defect.
        
        If you want to get the current periodically, it is recommended to use the
        callback :func:`Current` and set the period with 
        :func:`SetCurrentCallbackPeriod`.
        """
        return self.ipcon.send_request(self, BrickletIndustrialDual020mA.FUNCTION_GET_CURRENT, (sensor,), 'B', 'i')

    def set_current_callback_period(self, sensor, period):
        """
        Sets the period in ms with which the :func:`Current` callback is triggered
        periodically for the given sensor. A value of 0 turns the callback off.
        
        :func:`Current` is only triggered if the current has changed since the
        last triggering.
        
        The default value is 0.
        """
        self.ipcon.send_request(self, BrickletIndustrialDual020mA.FUNCTION_SET_CURRENT_CALLBACK_PERIOD, (sensor, period), 'B I', '')

    def get_current_callback_period(self, sensor):
        """
        Returns the period as set by :func:`SetCurrentCallbackPeriod`.
        """
        return self.ipcon.send_request(self, BrickletIndustrialDual020mA.FUNCTION_GET_CURRENT_CALLBACK_PERIOD, (sensor,), 'B', 'I')

    def set_current_callback_threshold(self, sensor, option, min, max):
        """
        Sets the thresholds for the :func:`CurrentReached` callback for the given
        sensor.
        
        The following options are possible:
        
        .. csv-table::
         :header: "Option", "Description"
         :widths: 10, 100
        
         "'x'",    "Callback is turned off"
         "'o'",    "Callback is triggered when the current is *outside* the min and max values"
         "'i'",    "Callback is triggered when the current is *inside* the min and max values"
         "'<'",    "Callback is triggered when the current is smaller than the min value (max is ignored)"
         "'>'",    "Callback is triggered when the current is greater than the min value (max is ignored)"
        
        The default value is ('x', 0, 0).
        """
        self.ipcon.send_request(self, BrickletIndustrialDual020mA.FUNCTION_SET_CURRENT_CALLBACK_THRESHOLD, (sensor, option, min, max), 'B c i i', '')

    def get_current_callback_threshold(self, sensor):
        """
        Returns the threshold as set by :func:`SetCurrentCallbackThreshold`.
        """
        return GetCurrentCallbackThreshold(*self.ipcon.send_request(self, BrickletIndustrialDual020mA.FUNCTION_GET_CURRENT_CALLBACK_THRESHOLD, (sensor,), 'B', 'c i i'))

    def set_debounce_period(self, debounce):
        """
        Sets the period in ms with which the threshold callback
        
        * :func:`CurrentReached`
        
        is triggered, if the threshold
        
        * :func:`SetCurrentCallbackThreshold`
        
        keeps being reached.
        
        The default value is 100.
        """
        self.ipcon.send_request(self, BrickletIndustrialDual020mA.FUNCTION_SET_DEBOUNCE_PERIOD, (debounce,), 'I', '')

    def get_debounce_period(self):
        """
        Returns the debounce period as set by :func:`SetDebouncePeriod`.
        """
        return self.ipcon.send_request(self, BrickletIndustrialDual020mA.FUNCTION_GET_DEBOUNCE_PERIOD, (), '', 'I')

    def set_sample_rate(self, rate):
        """
        Sets the sample rate to either 240, 60, 15 or 4 samples per second.
        The resolution for the rates is 12, 14, 16 and 18 bit respectively.
        
        .. csv-table::
         :header: "Value", "Description"
         :widths: 10, 100
        
         "0",    "240 samples per second, 12 bit resolution"
         "1",    "60 samples per second, 14 bit resolution"
         "2",    "15 samples per second, 16 bit resolution"
         "3",    "4 samples per second, 18 bit resolution"
        
        The default value is 3: 4 samples per second with 18 bit resolution.
        """
        self.ipcon.send_request(self, BrickletIndustrialDual020mA.FUNCTION_SET_SAMPLE_RATE, (rate,), 'B', '')

    def get_sample_rate(self):
        """
        Returns the sample rate as set by :func:`SetSampleRate`.
        """
        return self.ipcon.send_request(self, BrickletIndustrialDual020mA.FUNCTION_GET_SAMPLE_RATE, (), '', 'B')

    def get_identity(self):
        """
        Returns the UID, the UID where the Bricklet is connected to, 
        the position, the hardware and firmware version as well as the
        device identifier.
        
        The position can be 'a', 'b', 'c' or 'd'.
        
        The device identifiers can be found :ref:`here <device_identifier>`.
        
        .. versionadded:: 2.0.0~(Plugin)
        """
        return GetIdentity(*self.ipcon.send_request(self, BrickletIndustrialDual020mA.FUNCTION_GET_IDENTITY, (), '', '8s 8s c 3B 3B H'))

    def register_callback(self, id, callback):
        """
        Registers a callback with ID *id* to the function *callback*.
        """
        self.registered_callbacks[id] = callback

IndustrialDual020mA = BrickletIndustrialDual020mA # for backward compatibility
