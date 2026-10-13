import my_notebook
from cog import BasePredictor, Input


class Predictor(BasePredictor):
    def setup(self):
        """Prepare the model so multiple predictions run efficiently (optional)"""

    def predict(self, name: str = Input(description="name of person to greet")) -> str:
        """Run a single prediction"""

        output = my_notebook.say_hello(name)
        return output
