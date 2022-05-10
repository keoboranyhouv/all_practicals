from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

MILES_TO_KM = 1.610


class MilesConverterApp(App):

    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (300, 300)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self):
        """Convert miles to kilometers."""
        value = self.get_valid_miles()
        result = value * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, change):
        """Increment to the input number."""
        value = self.get_valid_miles() + change
        self.root.ids.input_number.text = str(value)
        self.handle_calculate()

    def get_valid_miles(self):
        """Check valid input."""
        try:
            value = float(self.root.ids.input_number.text)
            return value
        except ValueError:
            return 0


MilesConverterApp().run()
