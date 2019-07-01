from PlayerTimer import PlayerTimer
import time


class TimerManager:
    def __init__(self):
        self._move_timers = {}  # 'x': [time_elapsed, start_time]

    def start_timer(self, player_char: str):
        if player_char in self._move_timers:
            self._move_timers[player_char].start_time = time.time()
        else:
            self._move_timers[player_char] = PlayerTimer(player_char, 0, time.time())

    def end_timer(self, player_char: str):
        if player_char in self._move_timers:
            player = self._move_timers[player_char]
            if player.start_time != -1:
                player.timer += time.time() - player.start_time
                player.start_time = -1
            else:
                raise TimerInactiveError("Timer {} was never started and cannot end it!".format(player_char))
        else:
            raise TimerNotFoundError("Timer {} does not exist".format(player_char))

    def get_time(self, player_char: str):
        if player_char in self._move_timers:
            return self._move_timers[player_char].timer


class TimerNotFoundError(Exception):
    pass


class TimerInactiveError(Exception):
    pass