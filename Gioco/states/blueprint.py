from typing import TypeVar, Dict
from pygame import Surface
main_class_ref = TypeVar("reference to class in main")


class Blueprint:
    def __init__(self, base_class: main_class_ref) -> None:
      self.base_class: main_class_ref = base_class
      self.prev_state: object = None


    def update(self, delta_time: float, actions: Dict[str, bool]) -> None:
      """
      The update function is called every frame and is passed the time since the last frame and a list
      of actions that the player has taken.
      
      :param delta_time: The time in seconds since the last update
      :param actions: A list of actions that the agent can take
      """
      pass


    def render(self, surface: Surface) -> None:
      """
      The function takes a surface and draws text on it
      
      :param surface: The surface to draw the text on
      """
      self.base_class.draw_text(surface,
                                'Base render function',
                                (0, 0, 0),
                                self.base_class.GAME_W/2,
                                self.base_class.GAME_H/2)


    def enter_state(self) -> None:
      """
      If the state stack has more than one element, the previous state is the last element of the
      state stack
      """
      if len(self.base_class.state_stack) > 1:
          self.prev_state = self.base_class.state_stack[-1]
      self.base_class.state_stack.append(self)


    def exit_state(self) -> None:
      """
      It removes the current state from the state stack
      """
      self.base_class.state_stack.pop()
