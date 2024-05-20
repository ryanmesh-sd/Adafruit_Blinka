import pytest
import board
import analogio

# Values for sine wave
# (data points = 20, amplitude=100, frequency=1)
sine_wave = [
    0,
    31,
    59,
    81,
    95,
    100,
    95,
    81,
    59,
    31,
    0,
    -31,
    -59,
    -81,
    -95,
    -100,
    -95,
    -81,
    -59,
    -31,
]

# Values for a sawtooth wave
# (data points = 20, amplitude=100)
sawtooth_wave = [
    -100,
    -80,
    -60,
    -40,
    -20,
    0,
    20,
    40,
    60,
    80,
    -100,
    -80,
    -60,
    -40,
    -20,
    0,
    20,
    40,
    60,
    80,
]


def test_ax_input_rand_int():
    """Test random integer from pin Ax_INPUT_RAND_INT"""
    assert board.board_id == "GENERIC_AGNOSTIC_BOARD"
    pin_random = analogio.AnalogIn(board.Ax_INPUT_RAND_INT)

    assert isinstance(pin_random.value, int)

    pin_random.deinit()


def test_ax_input_fixed_int_pi():
    """Test fixed integer from pin Ax_INPUT_FIXED_INT_PI"""
    assert board.board_id == "GENERIC_AGNOSTIC_BOARD"
    pin_pi = analogio.AnalogIn(board.Ax_INPUT_FIXED_INT_PI)

    assert pin_pi.value == 31415

    pin_pi.deinit()


def test_ax_input_sine_wave():
    """Test sine wave from pin Ax_OUTPUT_WAVE_SINE"""
    assert board.board_id == "GENERIC_AGNOSTIC_BOARD"
    pin_sine_wave = analogio.AnalogIn(board.Ax_OUTPUT_WAVE_SINE)

    # Run through the sine wave once
    for i in range(len(sine_wave)):
        assert pin_sine_wave.value == sine_wave[i]

    # Run through the sine wave again to ensure it loops back correctly
    for i in range(len(sine_wave)):
        assert pin_sine_wave.value == sine_wave[i]

    pin_sine_wave.deinit()


def test_ax_input_saw_wave():
    """Test sawtooth wave from pin Ax_OUTPUT_WAVE_SAW"""
    assert board.board_id == "GENERIC_AGNOSTIC_BOARD"
    pin_sine_wave = analogio.AnalogIn(board.Ax_OUTPUT_WAVE_SAW)

    # Run through the sine wave once
    for i in range(len(sawtooth_wave)):
        assert pin_sine_wave.value == sawtooth_wave[i]

    # Run through the sine wave again to ensure it loops back correctly
    for i in range(len(sawtooth_wave)):
        assert pin_sine_wave.value == sawtooth_wave[i]

    pin_sine_wave.deinit()
