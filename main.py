from notifypy import Notify

notification = Notify()
notification.title = "Cool Title"
notification.message = "Even cooler message."
notification.icon = "astronaut.png"
notification.audio = "Arrow.wav"

notification.send()
