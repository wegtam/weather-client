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

GetMonoflop = namedtuple('Monoflop', ['value', 'time', 'time_remaining'])
GetIdentity = namedtuple('Identity', ['uid', 'connected_uid', 'position', 'hardware_version', 'firmware_version', 'device_identifier'])

class BrickletIndustrialDigitalOut4(Device):
    """
    Device for controlling up to 4 optically coupled digital outputs
    """

    DEVICE_IDENTIFIER = 224

    CALLBACK_MONOFLOP_DONE = 8

    FUNCTION_SET_VALUE = 1
    FUNCTION_GET_VALUE = 2
    FUNCTION_SET_MONOFLOP = 3
    FUNCTION_GET_MONOFLOP = 4
    FUNCTION_SET_GROUP = 5
    FUNCTION_GET_GROUP = 6
    FUNCTION_GET_AVAILABLE_FOR_GROUP = 7
    FUNCTION_SET_SELECTED_VALUES = 9
    FUNCTION_GET_IDENTITY = 255


    def __init__(self, uid, ipcon):
        """
        Creates an object with the unique device ID *uid* and adds it to
        the IP Connection *ipcon*.
        """
        Device.__init__(self, uid, ipcon)

        self.api_version = (2, 0, 0)

        self.response_expected[BrickletIndustrialDigitalOut4.FUNCTION_SET_VALUE] = BrickletIndustrialDigitalOut4.RESPONSE_EXPECTED_FALSE
        self.response_expected[BrickletIndustrialDigitalOut4.FUNCTION_GET_VALUE] = BrickletIndustrialDigitalOut4.RESPONSE_EXPECTED_ALWAYS_TRUE
        self.response_expected[BrickletIndustrialDigitalOut4.FUNCTION_SET_MONOFLOP] = BrickletIndustrialDigitalOut4.RESPONSE_EXPECTED_FALSE
        self.response_expected[BrickletIndustrialDigitalOut4.FUNCTION_GET_MONOFLOP] = BrickletIndustrialDigitalOut4.RESPONSE_EXPECTED_ALWAYS_TRUE
        self.response_expected[BrickletIndustrialDigitalOut4.FUNCTION_SET_GROUP] = BrickletIndustrialDigitalOut4.RESPONSE_EXPECTED_FALSE
        self.response_expected[BrickletIndustrialDigitalOut4.FUNCTION_GET_GROUP] = BrickletIndustrialDigitalOut4.RESPONSE_EXPECTED_ALWAYS_TRUE
        self.response_expected[BrickletIndustrialDigitalOut4.FUNCTION_GET_AVAILABLE_FOR_GROUP] = BrickletIndustrialDigitalOut4.RESPONSE_EXPECTED_ALWAYS_TRUE
        self.response_expected[BrickletIndustrialDigitalOut4.CALLBACK_MONOFLOP_DONE] = BrickletIndustrialDigitalOut4.RESPONSE_EXPECTED_ALWAYS_FALSE
        self.response_expected[BrickletIndustrialDigitalOut4.FUNCTION_SET_SELECTED_VALUES] = BrickletIndustrialDigitalOut4.RESPONSE_EXPECTED_FALSE
        self.response_expected[BrickletIndustrialDigitalOut4.FUNCTION_GET_IDENTITY] = BrickletIndustrialDigitalOut4.RESPONSE_EXPECTED_ALWAYS_TRUE

        self.callback_formats[BrickletIndustrialDigitalOut4.CALLBACK_MONOFLOP_DONE] = 'H H'

    def set_value(self, value_mask):
        """
        Sets the output value with a bitmask. The bitmask
        is 16 bit long, *true* refers to high and *false* refers to 
        low.
        
        For example: The value 0b0000000000000011 will turn pins 0-1 
        high and the other pins low.
        
        If no groups are used (see :func:`SetGroup`), the pins correspond to the
        markings on the Digital Out 4 Bricklet.
        
        If groups are used, the pins correspond to the element in the group.
        Element 1 in the group will get pins 0-3, element 2 pins 4-7, element 3
        pins 8-11 and element 4 pins 12-15.
        """
        self.ipcon.send_request(self, BrickletIndustrialDigitalOut4.FUNCTION_SET_VALUE, (value_mask,), 'H', '')

    def get_value(self):
        """
        Returns the bitmask as set by :func:`SetValue`.
        """
        return self.ipcon.send_request(self, BrickletIndustrialDigitalOut4.FUNCTION_GET_VALUE, (), '', 'H')

    def set_monoflop(self, selection_mask, value_mask, time):
        """
        Configures a monoflop of the pins specified by the first parameter
        bitmask.
        
        The second parameter is a bitmask with the desired value of the specified
        pins (*true* means high and *false* means low).
        
        The third parameter indicates the time (in ms) that the pins should hold
        the value.
        
        If this function is called with the parameters 
        ((1 << 0) | (1 << 3), (1 << 0), 1500):
        Pin 0 will get high and pin 3 will get low. In 1.5s pin 0 will get low and
        pin 3 will get high again.
        
        A monoflop can be used as a fail-safe mechanism. For example: Lets assume you
        have a RS485 bus and a Digital Out 4 Bricklet connected to one of the slave
        stacks. You can now call this function every second, with a time parameter
        of two seconds and pin 0 high. Pin 0 will be high all the time. If now
        the RS485 connection is lost, then pin 0 will turn low in at most two seconds.
        """
        self.ipcon.send_request(self, BrickletIndustrialDigitalOut4.FUNCTION_SET_MONOFLOP, (selection_mask, value_mask, time), 'H H I', '')

    def get_monoflop(self, pin):
        """
        Returns (for the given pin) the current value and the time as set by
        :func:`SetMonoflop` as well as the remaining time until the value flips.
        
        If the timer is not running currently, the remaining time will be returned
        as 0.
        """
        return GetMonoflop(*self.ipcon.send_request(self, BrickletIndustrialDigitalOut4.FUNCTION_GET_MONOFLOP, (pin,), 'B', 'H I I'))

    def set_group(self, group):
        """
        Sets a group of Digital Out 4 Bricklets that should work together. You can
        find Bricklets that can be grouped together with :func:`GetAvailableForGroup`.
        
        The group consists of 4 elements. Element 1 in the group will get pins 0-3,
        element 2 pins 4-7, element 3 pins 8-11 and element 4 pins 12-15.
        
        Each element can either be one of the ports ('a' to 'd') or 'n' if it should
        not be used.
        
        For example: If you have two Digital Out 4 Bricklets connected to port A and
        port B respectively, you could call with "['a', 'b', 'n', 'n']".
        
        Now the pins on the Digital Out 4 on port A are assigned to 0-3 and the
        pins on the Digital Out 4 on port B are assigned to 4-7. It is now possible
        to call :func:`SetValue` and control two Bricklets at the same time.
        """
        self.ipcon.send_request(self, BrickletIndustrialDigitalOut4.FUNCTION_SET_GROUP, (group,), '4c', '')

    def get_group(self):
        """
        Returns the group as set by :func:`SetGroup`
        """
        return self.ipcon.send_request(self, BrickletIndustrialDigitalOut4.FUNCTION_GET_GROUP, (), '', '4c')

    def get_available_for_group(self):
        """
        Returns a bitmask of ports that are available for grouping. For example the
        value 0b0101 means: Port *A* and Port *C* are connected to Bricklets that
        can be grouped together.
        """
        return self.ipcon.send_request(self, BrickletIndustrialDigitalOut4.FUNCTION_GET_AVAILABLE_FOR_GROUP, (), '', 'B')

    def set_selected_values(self, selection_mask, value_mask):
        """
        Sets the output value with a bitmask, according to the selection mask.
        The bitmask is 16 bit long, *true* refers to high and *false* refers to 
        low.
        
        For example: The values 0b0000000000000011, b0000000000000001 will turn 
        pin 0 high, pin 1 low the other pins remain untouched.
        
        If no groups are used (see :func:`SetGroup`), the pins correspond to the
        markings on the Digital Out 4 Bricklet.
        
        If groups are used, the pins correspond to the element in the group.
        Element 1 in the group will get pins 0-3, element 2 pins 4-7, element 3
        pins 8-11 and element 4 pins 12-15.
        
        .. versionadded:: 2.0.0~(Plugin)
        """
        self.ipcon.send_request(self, BrickletIndustrialDigitalOut4.FUNCTION_SET_SELECTED_VALUES, (selection_mask, value_mask), 'H H', '')

    def get_identity(self):
        """
        Returns the UID, the UID where the Bricklet is connected to, 
        the position, the hardware and firmware version as well as the
        device identifier.
        
        The position can be 'a', 'b', 'c' or 'd'.
        
        The device identifiers can be found :ref:`here <device_identifier>`.
        
        .. versionadded:: 2.0.0~(Plugin)
        """
        return GetIdentity(*self.ipcon.send_request(self, BrickletIndustrialDigitalOut4.FUNCTION_GET_IDENTITY, (), '', '8s 8s c 3B 3B H'))

    def register_callback(self, id, callback):
        """
        Registers a callback with ID *id* to the function *callback*.
        """
        self.registered_callbacks[id] = callback

IndustrialDigitalOut4 = BrickletIndustrialDigitalOut4 # for backward compatibility
