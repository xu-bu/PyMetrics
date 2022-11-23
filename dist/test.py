import abc
import datetime
import inspect


class MessageDisplay(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractproperty
    def display(self, message):
        pass

class FriendlyMessageDisplay(MessageDisplay):
    def greet(self):
        hour = datetime.datetime.now().timetuple().tm_hour

        if hour < 7:
            raise Exception("Cannot greet while asleep.")
        elif hour < 12:
            self.display("Good morning!")
        elif hour < 18:
            self.display("Good afternoon!")
        elif hour < 20:
            self.display("Good evening!")
        else:
            self.display("Good night.")

class FriendlyMessagePrinter(FriendlyMessageDisplay):
    def display(self, message):
        print(message)

print(inspect.isabstract(MessageDisplay))