from PyQt6.QtWidgets import *
from PyQt6 import QtGui
from tvcontrol import Ui_MainWindow
import sys


class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        """Initialize the main window with default settings."""
        super().__init__()
        self.setupUi(self)

        self._volume: int = 10
        self._previous_volume: int = self._volume
        self._channel: int = 0
        self._power_on: bool = True

        self.channels: dict[int, str] = {
            0: 'power_off.png',
            1: 'disney-channel-us.png',
            2: 'c-span-1-us.png',
            3: 'abc-logo-1962-us.png',
            4: 'nbc-us.png',
            5: 'mtv-us.png',
            6: 'hbo-us.png',
            7: 'espn-us.png',
            8: 'cw-us.png',
            9: 'cnn-us.png'
        }

        try:
            # Connect UI elements to their respective methods
            self.volumeUpButton.clicked.connect(self.volume_up)
            self.volumeDownButton.clicked.connect(self.volume_down)
            self.channelUpButton.clicked.connect(self.channel_up)
            self.channelDownButton.clicked.connect(self.channel_down)
            self.muteButton.clicked.connect(self.mute)
            self.horizontalSlider.valueChanged.connect(self.update_volume_from_slider)
            self.powerButton.clicked.connect(self.power_off)
            self.oneButton.clicked.connect(self.one)

            # Connect 1-9 buttons
            self.twoButton.clicked.connect(self.two)
            self.threeButton.clicked.connect(self.three)
            self.fourButton.clicked.connect(self.four)
            self.fiveButton.clicked.connect(self.five)
            self.sixButton.clicked.connect(self.six)
            self.sevenButton.clicked.connect(self.seven)
            self.eightButton.clicked.connect(self.eight)
            self.nineButton.clicked.connect(self.nine)

            # Initialize the volume slider settings
            self.horizontalSlider.setMinimum(0)
            self.horizontalSlider.setMaximum(100)
            self.horizontalSlider.setValue(self._volume)

            # Update UI to reflect the current state
            self.update_channel_display()
            self.volume_which()
        except Exception as mess:
            QMessageBox.critical(self, "Initialization Error", f"An error occurred during initialization: {str(mess)}")
            sys.exit(-1)

    def volume_which(self) -> None:
        """Update the volume label and slider with the current volume level."""
        try:
            self.volumeLabel.setText(f'Volume: {self._volume}')
            self.horizontalSlider.setValue(self._volume)
        except Exception as mess:
            QMessageBox.critical(self, "Error", f"Failed to update volume display: {str(mess)}")

    def channel_which(self) -> None:
        """Update the channel label with the current channel number."""
        self.channelLabel.setText(f'Channel: {self._channel}')

    def volume_up(self) -> None:
        """Increase the volume by one unit until the maximum is reached."""
        if self._volume < 100:
            self._volume += 1
        self.volume_which()

    def volume_down(self) -> None:
        """Decrease the volume by one unit until the minimum is reached."""
        if self._volume > 0:
            self._volume -= 1
        self.volume_which()

    def mute(self) -> None:
        """Toggle the mute state of the volume."""
        if self._volume != 0:
            self._previous_volume = self._volume
            self._volume = 0
        else:
            self._volume = self._previous_volume
        self.volume_which()

    def channel_up(self) -> None:
        """Increase the channel number by one, wrapping around to 1 if the maximum is exceeded."""
        if self._channel < 9:
            self._channel += 1
        else:
            self._channel = 1
        self.update_channel_display()

    def channel_down(self) -> None:
        """Decrease the channel number by one, wrapping around to 9 if the minimum is exceeded."""
        if self._channel > 1:
            self._channel -= 1
        else:
            self._channel = 9
        self.update_channel_display()

    def power_off(self) -> None:
        """Set the TV to power off state, showing the 'power_off' image."""
        if self._channel == 0:
            self._channel += 1
        else:
            self._channel = 0
        self.update_channel_display()

    def toggle_power(self) -> None:
        """Toggle the power state of the TV between on and off."""
        self._power_on = not self._power_on
        if self._power_on:
            self._channel = 1  # Default channel when turning on
            self.update_channel_display()
        else:
            self.power_off()

    def update_channel_display(self) -> None:
        """Update the display with the current channel's image."""
        if self._power_on:
            try:
                channel_image = self.channels.get(self._channel)
                if channel_image:
                    self.pictureLabel.setPixmap(QtGui.QPixmap(channel_image))
                else:
                    raise ValueError("Channel image not found")
            except Exception as mess:
                QMessageBox.critical(self, "Display Error", f"Failed to display channel: {str(mess)}")
        else:
            self.power_off()

    def update_volume_from_slider(self, value: int) -> None:
        """Update the volume level based on the slider's position."""
        self._volume = value
        self.volume_which()

    def one(self) -> None:
        """Set the current channel to 1 and update the display."""
        self._channel = 1
        self.update_channel_display()

    def two(self) -> None:
        """Set the current channel to 2 and update the display."""
        self._channel = 2
        self.update_channel_display()

    def three(self) -> None:
        """Set the current channel to 3 and update the display."""
        self._channel = 3
        self.update_channel_display()

    def four(self) -> None:
        """Set the current channel to 4 and update the display."""
        self._channel = 4
        self.update_channel_display()

    def five(self) -> None:
        """Set the current channel to 5 and update the display."""
        self._channel = 5
        self.update_channel_display()

    def six(self) -> None:
        """Set the current channel to 6 and update the display."""
        self._channel = 6
        self.update_channel_display()

    def seven(self) -> None:
        """Set the current channel to 7 and update the display."""
        self._channel = 7
        self.update_channel_display()

    def eight(self) -> None:
        """Set the current channel to 8 and update the display."""
        self._channel = 8
        self.update_channel_display()

    def nine(self) -> None:
        """Set the current channel to 9 and update the display."""
        self._channel = 9
        self.update_channel_display()
