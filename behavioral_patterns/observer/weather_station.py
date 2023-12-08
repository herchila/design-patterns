class Observer:
    def update(self, subject): pass

class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)

class WeatherStation(Subject):
    _temperature = None

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, temp):
        self._temperature = temp
        self.notify()

class DisplayDevice(Observer):
    def update(self, subject):
        print(f"Temperature Update: {subject.temperature}°C")

# Usage
weather_station = WeatherStation()
display = DisplayDevice()
weather_station.attach(display)

weather_station.temperature = 26  # Temperature Update: 26°C
