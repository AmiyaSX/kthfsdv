import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, TextBox
from datetime import datetime

class DynamicPlotter:
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.l, = self.ax.plot([0, 10], [-10,1000], 'r', label='h(t)')
        self.ax.grid(True)
        self.ax.legend()

        self.lambda_func = lambda t: 5 * np.sin(2 * np.pi * 1 * t)
        self.time_interval = 0.1
        self.t = np.arange(0, 10, self.time_interval)

        # adjusting axis with slider (zoom functionality)
        self.axcolor = 'lightgoldenrodyellow'
        ax_lambda = plt.axes([0.12, 0.01, 0.65, 0.03], facecolor=self.axcolor)
        self.lambda_slider = Slider(ax_lambda, 'Lambda', 1, 10, valinit=5)
        self.lambda_slider.on_changed(self.update)

        ax_reset = plt.axes([0.8, 0.01, 0.1, 0.04])
        self.reset_button = Button(ax_reset, 'Reset', color=self.axcolor, hovercolor='0.975')
        self.reset_button.on_clicked(self.reset)

        ax_save = plt.axes([0.9, 0.01, 0.1, 0.04])
        self.save_button = Button(ax_save, 'Save', color=self.axcolor, hovercolor='0.975')
        self.save_button.on_clicked(self.save_data)

        # input experiment name
        ax_textbox = plt.axes([0.3, 0.92, 0.2, 0.04])
        self.textbox = TextBox(ax_textbox, 'Experiment Name: ')
        self.textbox.on_submit(self.set_experiment_name)

        self.update(None)

    def update_data(self):
        self.h = 3 * np.pi * np.exp(-self.lambda_func(self.t))

    def update(self, val):
        self.lambda_func = lambda t: self.lambda_slider.val * np.sin(2 * np.pi * 1 * t)
        self.update_data()
        self.l.set_data(self.t, self.h)
        self.fig.canvas.draw_idle()

    def reset(self, event):
        self.t = np.arange(0, 10, self.time_interval)
        self.lambda_slider.set_val(5)
        self.update_data()
        self.l.set_data(self.t, self.h)
        self.fig.canvas.draw_idle()

    def set_experiment_name(self, text):
        self.experiment_name = text

    def save_data(self, event):
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"{timestamp}_{self.experiment_name}.csv"
        np.savetxt(filename, np.column_stack((self.t, self.h)), delimiter=",", header="Time,h(t)", comments="")

