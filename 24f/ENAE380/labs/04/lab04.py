import wave
import struct
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np


def sine():
    # frequency is the number of times a wave repeats a second
    frequency = 1000
    num_samples = 48000

    # The sampling rate of the analog to digital convert
    sampling_rate = 48000.0
    amplitude = 16000
    file = "test.wav"

    sine_wave = [
        np.sin(2 * np.pi * frequency * x / sampling_rate) for x in range(num_samples)
    ]

    nframes = num_samples
    comptype = "NONE"
    compname = "not compressed"
    nchannels = 1
    sampwidth = 2

    wav_file = wave.open(file, "w")
    wav_file.setparams(
        (nchannels, sampwidth, int(sampling_rate), nframes, comptype, compname)
    )

    for s in sine_wave:
        wav_file.writeframes(struct.pack("h", int(s * amplitude)))


def get_freq():
    frame_rate = 48000.0
    infile = "test.wav"
    num_samples = 48000
    wav_file = wave.open(infile, "r")
    data = wav_file.readframes(num_samples)
    wav_file.close()

    data = struct.unpack("{n}h".format(n=num_samples), data)

    data = np.array(data)

    data_fft = np.fft.fft(data)

    frequencies = np.abs(data_fft)

    print("The frequency is {} Hz".format(np.argmax(frequencies)))

    plt.subplot(2, 1, 1)
    plt.plot(data[:300])
    plt.title("Original audio wave")
    plt.subplot(2, 1, 2)
    plt.plot(frequencies)
    plt.title("Frequencies found")
    plt.xlim(0, 1200)
    plt.show()


def noisy():
    main_freq = 1000
    num_samples = 48000
    noise_freq = 50

    sampling_rate = 48000.0
    amplitude = 16000

    main_wave = [
        np.sin(2 * np.pi * main_freq * x / sampling_rate) for x in range(num_samples)
    ]
    noise_wave = [
        np.sin(2 * np.pi * noise_freq * x / sampling_rate) for x in range(num_samples)
    ]
    combined_wave = [main_wave[i] + noise_wave[i] for i in range(num_samples)]

    gs = gridspec.GridSpec(2, 2)
    fig = plt.figure()

    main_plt = fig.add_subplot(gs[0, 0])
    main_plt.plot(main_wave)
    main_plt.set_title("Main wave")
    main_plt.set_xlim(0, 1200)

    noise_plt = fig.add_subplot(gs[0, 1])
    noise_plt.plot(noise_wave)
    noise_plt.set_title("Noise wave")
    noise_plt.set_xlim(0, 1200)

    combined_plt = fig.add_subplot(gs[1, :])
    combined_plt.plot(combined_wave)
    combined_plt.set_title("Combined wave")
    combined_plt.set_xlim(0, 1200)

    freqs = np.abs(np.fft.fft(combined_wave))

    gs2 = gridspec.GridSpec(2, 1)
    fig2 = plt.figure()

    combined_plt = fig2.add_subplot(gs2[0, 0])
    combined_plt.plot(combined_wave)
    combined_plt.set_title("Combined wave")
    combined_plt.set_xlim(0, 1200)

    freqs_plt = fig2.add_subplot(gs2[1, 0])
    freqs_plt.plot(freqs)
    freqs_plt.set_title("Frequencies")
    freqs_plt.set_xlim(0, 1200)

    plt.show()


def pitch():
    infile = "trumpet.wav"
    wav_file = wave.open(infile, "r")

    nchannels = wav_file.getnchannels()
    nframes = wav_file.getnframes()
    sampwidth = wav_file.getsampwidth()

    data = wav_file.readframes(nframes)

    wav_file.close()

    dtype_map = {1: np.int8, 2: np.int16, 3: "special", 4: np.int32}
    if sampwidth not in dtype_map:
        raise ValueError("sampwidth %d unknown" % sampwidth)

    if sampwidth == 3:
        xs = np.fromstring(data, dtype=np.int8).astype(np.int32)
        ys = (xs[2::3] * 256 + xs[1::3]) * 256 + xs[0::3]
    else:
        ys = np.frombuffer(data, dtype=dtype_map[sampwidth])

    # if it's in stereo, just pull out the first channel
    if nchannels == 2:
        ys = ys[::2]

    # plot full signal

    # plot segment of signal

    # FFT of segment

    # Find three highest peaks and their frequencies

    # Filter out highest frequencies

    # Plot inverse signal

    # Save original segment and filtered segment to wave files


def mix_signals():
    pass


def stretch(input, factor):
    pass


def sampling():
    freq1 = 5.0  # freq in Hz
    freq2 = 1.0  # freq in Hz
    samp = 1000.0  # sampling rate in Hz

    t = np.arange(0, 1, 1 / samp)  # time (1s of data)
    N = len(t)  # store the number of time points

    x = np.cos(2 * np.pi * freq1 * t) + 0.5 * np.cos(
        2 * np.pi * freq2 * t
    )  # the signal equation

    # Continue the function here


if __name__ == "__main__":
    noisy()
