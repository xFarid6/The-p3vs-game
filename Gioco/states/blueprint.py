class Blueprint:
    def __init__(self, base_class):
      self.base_class = base_class
      self.prev_state = None

    def update(self, delta_time, actions):
      pass

    def render(self, surface):
      self.base_class.draw_text(surface,
                                'Base render function',
                                (0, 0, 0),
                                self.base_class.GAME_W/2,
                                self.base_class.GAME_H/2)

    def enter_state(self):
      if len(self.base_class.state_stack) > 1:
          self.prev_state = self.base_class.state_stack[-1]
      self.base_class.state_stack.append(self)

    def exit_state(self):
      self.base_class.state_stack.pop()

    def user_settings(self):
        pass

    def make_screenshot(self, actions, delta_time):
        pass
