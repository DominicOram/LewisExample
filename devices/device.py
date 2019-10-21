from collections import OrderedDict
from lewis.devices import StateMachineDevice
from lewis.core.statemachine import State


class DefaultRunningState(State):
    cnt = 0

    def in_state(self, dt):
        self.cnt += 1

        if self.cnt < 10:
            return

        self.cnt = 0
        self._context._increase_temp()
        self.log.info('Increased temp')


class ChillerDevice(StateMachineDevice):
    def _initialize_data(self):
        self.temp = 5

    def _get_state_handlers(self):
        return {
                'off': State(),
                'on': DefaultRunningState()
                }

    def _get_initial_state(self):
        return 'on'

    def _get_transition_handlers(self):
        return OrderedDict()

    def _increase_temp(self):
        self.temp += 1
        self.interface.ir.set(0, (self.temp,))
