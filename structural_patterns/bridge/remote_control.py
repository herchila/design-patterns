class Device:
    def turn_on(self):
        raise NotImplementedError

    def turn_off(self):
        raise NotImplementedError


class TV(Device):
    def turn_on(self):
        print("Turning on the TV.")

    def turn_off(self):
        print("Turning off the TV.")

class DVD(Device):
    def turn_on(self):
        print("Turning on the DVD Player.")

    def turn_off(self):
        print("Turning off the DVD Player.")


class RemoteControl:
    def __init__(self, device):
        self.device = device

    def toggle_power(self):
        if self.is_power_on:
            self.device.turn_off()
            self.is_power_on = False
        else:
            self.device.turn_on()
            self.is_power_on = True


# Usage
tv = TV()
tv_remote = RemoteControl(tv)
tv_remote.toggle_power()  # Turns on the TV

dvd = DVD()
dvd_remote = RemoteControl(dvd)
dvd_remote.toggle_power()  # Turns on the DVD Player
