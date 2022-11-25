import supervisor
import board
import digitalio
import storage

button = digitalio.DigitalInOut(board.GP4)
button.pull = digitalio.Pull.UP

# Disable USB storage unless the shift key is pressed
if button.value:
    storage.disable_usb_drive()


supervisor.set_next_stack_limit(4096 + 4096)
