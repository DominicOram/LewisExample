from lewis.adapters.modbus import ModbusBasicDataBank, ModbusInterface


class ChillerModbusInterface(ModbusInterface):

    @ModbusInterface.device.setter
    def device(self, new_device):
        """
        Overrides base implementation to give attached device a reference to self
        Required to allow communications between the interface and device
        """
        ModbusInterface.device.fset(self, new_device)
        self.device.interface = self

    ir = ModbusBasicDataBank(0, start_addr=0x0, last_addr=0x8)
