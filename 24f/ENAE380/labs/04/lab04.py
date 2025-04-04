# Vai Srivastava - 0106

import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wave

def noisy():
    """
    Generate and plot a main sine wave and a noise sine wave, combine them, and filter the noise using FFT.
    """
    f_main = 1000  # main frequency in Hz
    f_noise = 50   # noise frequency in Hz

    sample_rate = 48000  # samples per second
    duration = 10        # duration in seconds
    t = np.linspace(0, duration, duration * sample_rate, endpoint=False)  # time vector

    w_main = np.sin(2 * np.pi * f_main * t)  # main sine wave
    w_noise = np.sin(2 * np.pi * f_noise * t)  # noise sine wave
    w_combo = w_main + w_noise  # combined wave

    # Plot main, noise, and combined waves
    fig, axs = plt.subplots(3, 1)

    axs[0].set_title("Main wave")
    axs[0].plot(t, w_main)
    axs[1].set_title("Noise wave")
    axs[1].plot(t, w_noise)
    axs[2].set_title("Combined wave")
    axs[2].plot(t, w_combo)

    for ax in axs:
        ax.set_xlim(0, 0.1)
        ax.set_xlabel("Time [s]")
        ax.set_ylabel("Amplitude")

    fig.set_size_inches(12, 16)
    plt.savefig("./6.1.2.png")
    plt.show()
    plt.close()

    # Perform FFT on the combined wave
    fftw_combo = np.fft.fft(w_combo)
    fftf_combo = np.fft.fftfreq(w_combo.size, 1 / sample_rate)

    # Plot combined wave and its frequencies
    fig, axs = plt.subplots(2, 1)

    axs[0].set_title("Combined wave")
    axs[0].plot(t, w_combo)
    axs[0].set_xlim(0, 0.1)
    axs[0].set_xlabel("Time [s]")
    axs[0].set_ylabel("Amplitude")

    axs[1].set_title("Frequencies")
    axs[1].plot(fftf_combo, np.abs(fftw_combo))
    axs[1].set_xlim(0, 1200)
    axs[1].set_xlabel("Frequency [Hz]")
    axs[1].set_ylabel("Amplitude")

    fig.set_size_inches(12, 16)
    plt.savefig("./6.1.3.png")
    plt.show()
    plt.close()

    # Filter out frequencies except the main frequency
    fftw_filter = [
        fftw_combo[i] if np.abs(fftf_combo[i]) == f_main else 0
        for i in range(fftw_combo.size)
    ]
    w_filter = np.real(np.fft.ifft(fftw_filter))

    # Plot filtered frequencies
    fig, ax = plt.subplots()

    ax.set_title("Filtered Frequencies")
    ax.plot(fftf_combo, np.abs(fftw_filter))
    ax.set_xlim(0, 1200)
    ax.set_xlabel("Frequency [Hz]")
    ax.set_ylabel("Amplitude")

    fig.set_size_inches(12, 16)
    plt.savefig("./6.1.4.png")
    plt.show()
    plt.close()

    # Plot original, combined, and filtered waves
    fig, axs = plt.subplots(3, 1)

    axs[0].set_title("Original wave")
    axs[0].plot(t, w_main)
    axs[1].set_title("Combined wave")
    axs[1].plot(t, w_combo)
    axs[2].set_title("Filtered wave")
    axs[2].plot(t, w_filter)

    for ax in axs:
        ax.set_xlim(0, 0.1)
        ax.set_xlabel("Time [s]")
        ax.set_ylabel("Amplitude")

    fig.set_size_inches(12, 16)
    plt.savefig("./6.1.5.png")
    plt.show()
    plt.close()


def pitch():
    """
    Analyze a trumpet sound file to find the three highest frequencies and filter them out.
    """
    infile = "./trumpet.wav"

    sample_rate, w_input = wave.read(infile)
    duration = w_input.shape[0] / sample_rate

    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

    # Plot full signal
    fig, ax = plt.subplots()

    ax.set_title("Full signal")
    ax.plot(t, w_input[:, 0])
    ax.set_xlabel("Time [s]")
    ax.set_ylabel("Amplitude")

    fig.set_size_inches(12, 16)
    plt.savefig("./6.2.1.png")
    plt.show()
    plt.close()

    # Plot a segment of the signal
    fig, ax = plt.subplots()

    ax.set_title("Segment of signal")
    ax.plot(t[66000:82000], w_input[66000:82000, 0])
    ax.set_xlabel("Time [s]")
    ax.set_ylabel("Amplitude")

    fig.set_size_inches(12, 16)
    plt.savefig("./6.2.2.png")
    plt.show()
    plt.close()

    # Perform FFT on the segment
    fftw_seg = np.fft.fft(w_input[66000:82000, 0])
    fftf_seg = np.fft.fftfreq(w_input[66000:82000, 0].size, 1 / sample_rate)

    # Plot frequencies of the segment
    fig, ax = plt.subplots()

    ax.set_title("Frequencies of segment")
    ax.plot(fftf_seg, np.abs(fftw_seg))
    ax.set_xlabel("Frequency [Hz]")
    ax.set_ylabel("Amplitude")
    ax.set_xlim(0)

    fig.set_size_inches(12, 16)
    plt.savefig("./6.2.3.png")
    plt.show()
    plt.close()

    # Find the three highest frequencies
    positive_freqs = fftf_seg[: fftf_seg.size // 2]
    positive_fft = fftw_seg[: fftw_seg.size // 2]

    three_highest_locs = np.argpartition(np.abs(positive_fft), -3)[-3:]

    three_highest_freqs = positive_freqs[three_highest_locs]
    three_highest_vals = positive_fft[three_highest_locs]

    print("Corresponding frequencies [Hz]:", three_highest_freqs)
    print("Amplitudes of the three highest frequencies:", np.abs(three_highest_vals))

    # Zero out the three highest frequencies
    fftw_seg[three_highest_locs] = 0
    fftw_seg[-three_highest_locs] = 0

    # Inverse FFT to get the filtered signal
    w_filtered = np.real(np.fft.ifft(fftw_seg))

    # Plot the filtered segment
    fig, ax = plt.subplots()

    ax.set_title("Filtered segment of signal")
    ax.plot(t[66000:82000], w_filtered)
    ax.set_xlabel("Time [s]")
    ax.set_ylabel("Amplitude")

    fig.set_size_inches(12, 16)
    plt.savefig("./6.2.6.png")
    plt.show()
    plt.close()

    # Normalize and save the filtered segment as a wav file
    w_filtered_norm = (w_filtered / np.max(np.abs(w_filtered)) * 32767).astype(np.int16)

    wave.write("segment_filter.wav", sample_rate, w_filtered_norm)


def mix_signals():
    """
    Mix three sine waves of different frequencies and save the result as a wav file.
    """
    arr_f = [440, 523.2, 659.2]  # frequencies in Hz
    sample_rate = 48000  # samples per second

    # Generate sine waves for each frequency
    waves = [
        np.array(np.sin(2 * np.pi * f * np.arange(sample_rate) / sample_rate))
        for f in arr_f
    ]

    w_mix = np.sum(waves, axis=0)  # sum the waves

    # Perform FFT on the mixed wave
    fftw_mix = np.fft.fft(w_mix)
    fftf_mix = np.fft.fftfreq(w_mix.size, 1 / sample_rate)

    # Plot frequencies of the mixed wave
    fig, ax = plt.subplots()

    ax.set_title("Frequencies of mixed wave")
    ax.plot(fftf_mix, np.abs(fftw_mix))
    ax.set_xlabel("Frequency [Hz]")
    ax.set_ylabel("Amplitude")
    ax.set_xlim(0)

    fig.set_size_inches(12, 16)
    plt.savefig("./6.3.png")
    plt.show()
    plt.close()

    # Normalize and save the mixed wave as a wav file
    w_mix_norm = (w_mix / np.max(np.abs(w_mix)) * 32767).astype(np.int16)

    wave.write("./mix_signals.wav", sample_rate, w_mix_norm)


def stretch(input, output, factor):
    """
    Stretch or compress a wav file by changing its sample rate.

    Parameters:
    - input: path to input wav file
    - output: path to output wav file
    - factor: stretching factor (e.g., 0.75 to compress, 1.25 to stretch)
    """
    sample_rate, w_input = wave.read(input)
    wave.write(output, int(sample_rate * factor), w_input)


def sampling():
    """
    Demonstrate aliasing by subsampling a signal with frequencies close to half the sample rate.
    """
    freq1 = 5.0  # frequency in Hz
    freq2 = 1.0  # frequency in Hz
    sample_rate = 1000  # samples per second

    t_og = np.arange(0, 1, 1 / sample_rate)  # original time vector

    # Original combined wave
    w_og = np.cos(2 * np.pi * freq1 * t_og) + 0.5 * np.cos(2 * np.pi * freq2 * t_og)

    # Perform FFT on original wave
    fftw_x = np.fft.fft(w_og)
    fftf_x = np.fft.fftfreq(w_og.size, 1 / sample_rate)

    # Plot original wave and its frequencies
    fig, axs = plt.subplots(2, 1)

    axs[0].set_title("Combined wave")
    axs[0].plot(t_og, w_og)
    axs[0].set_xlabel("Time [s]")
    axs[0].set_ylabel("Amplitude")

    axs[1].set_title("Frequencies")
    axs[1].plot(fftf_x, np.abs(fftw_x))
    axs[1].set_xlabel("Frequency [Hz]")
    axs[1].set_ylabel("Amplitude")
    axs[1].set_xlim(0)

    fig.set_size_inches(12, 16)
    plt.savefig("./6.5.1.png")
    plt.show()
    plt.close()

    # Subsample the signal
    F = 125 # new sample rate in Hz
    subsample_factor = int(sample_rate / F)

    w_sub = w_og[::subsample_factor]  # subsampled wave
    t_sub = t_og[::subsample_factor]  # subsampled time vector

    # Perform FFT on subsampled wave
    fftw_sub = np.fft.fft(w_sub)
    fftf_sub = np.fft.fftfreq(w_sub.size, 1 / F)

    # Plot subsampled wave and its frequencies
    fig, axs = plt.subplots(2, 1)
    axs[0].set_title("Subsampled Wave")
    axs[0].plot(t_sub, w_sub)
    axs[0].set_xlabel("Time [s]")
    axs[0].set_ylabel("Amplitude")

    axs[1].set_title("Frequencies of Subsampled Signal")
    axs[1].plot(fftf_sub, np.abs(fftw_sub))
    axs[1].set_xlabel("Frequency [Hz]")
    axs[1].set_ylabel("Amplitude")
    axs[1].set_xlim(0)

    fig.set_size_inches(12, 16)
    plt.savefig("./6.5.3.png")
    plt.show()
    plt.close()

if __name__ == "__main__":
    # noisy()
    # pitch()
    # mix_signals()
    # stretch("./drum.wav", "./stretch_drum.wav", 0.75)
    # sampling()
    pass
