from pynput.mouse import Button, Controller

mouse = Controller()

for i in range (32):
    for x in range (510, 1400, 75):
        for y in range (250, 650, 75):
            mouse.position = x, y
            mouse.click(Button.left, 1)
