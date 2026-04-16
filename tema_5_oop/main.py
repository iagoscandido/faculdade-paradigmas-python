class Television:
  def __init__(self, main_channel, min_channel, max_channel) -> None:
    self.main_channel = main_channel
    self.min_channel = min_channel
    self.max_channel = max_channel

  def change_channel(self, new_channel) -> str:
    if new_channel < self.min_channel:
      self.main_channel = self.max_channel

    if new_channel > self.max_channel:
        self.main_channel = self.min_channel

    self.main_channel = new_channel
    return f"Channel changed to {self.main_channel}"

tv = Television(1, 1, 100)

print(tv.change_channel(10))  # Output: Channel changed to 10
print(tv.change_channel(101)) # Output: Channel changed to 1
print(tv.change_channel(0))   # Output: Channel changed to 100