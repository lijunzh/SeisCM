import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap


def bwr(alpha=0):
    """
    Create a Blue-White-Red colormap given transparency value (alpha,
    default=0 for seismic cmap) in the middle.

    :param alpha: Transparency value in the middle between 0 and 1 (default=0).
    :type alpha: float

    :return: Blue-White-Red colormap
    :rtype: matplotlib.colors.LinearSegmentedColormap object
    """

    # Input check
    if not 0 <= alpha <= 1:
        raise ValueError("Alpha value must be between 0 and 1.")

    # Construct cmap dictionary
    cdict = {
        'red': ((0, 0, 0),
                (0.25, 0, 0),
                (0.5, 1, 1),
                (0.75, 0.8314, 0.8314),
                (1, 0.5, 0.5)),

        'green': ((0, 0, 0),
                  (0.25, 0.375, 0.375),
                  (0.5, 1, 1),
                  (0.75, 0.375, 0.375),
                  (1, 0, 0)),

        'blue': ((0, 0.5, 0.5),
                 (0.25, 0.8314, 0.8314),
                 (0.5, 1, 1),
                 (0.75, 0, 0),
                 (1, 0, 0)),

        'alpha': ((0, 1, 1),
                  (0.5, alpha, alpha),
                  (1, 1, 1)),
    }

    return LinearSegmentedColormap('BlueWhiteRed', cdict)


def seismic():
    """
    Create a seismic colormap.

    :return: seismic colormap
    :rtype: matplotlib.colors.LinearSegmentedColormap object
    """

    # Construct cmap dictionary
    cdict = {
        'red': ((0, 0.6314, 0.6314),
                (0.33, 0, 0),
                (0.4, 0.302, 0.302),
                (0.5, 0.8, 0.8),
                (0.6, 0.3804, 0.3804),
                (0.667, 0.749, 0.749),
                (1, 1, 1)),

        'green': ((0, 1, 1),
                  (0.33, 0, 0),
                  (0.4, 0.302, 0.302),
                  (0.5, 0.8, 0.8),
                  (0.6, 0.2706, 0.2706),
                  (0.667, 0, 0),
                  (1, 1, 1)),

        'blue': ((0, 1, 1),
                 (0.33, 0.749, 0.749),
                 (0.4, 0.302, 0.302),
                 (0.5, 0.8, 0.8),
                 (0.6, 0, 0),
                 (0.667, 0, 0),
                 (1, 0, 0)),
    }

    return LinearSegmentedColormap('Seismic', cdict)


def phase():
    """
    Create a phase colormap.

    :return: phase colormap
    :rtype: matplotlib.colors.LinearSegmentedColormap object
    """

    # Construct cmap dictionary
    cdict = {
        'red': ((0, 1, 1),
                (0.1, 1, 1),
                (0.2, 1, 1),
                (0.3, 1, 1),
                (0.4, 0.7765, 0.7765),
                (0.5, 0, 0),
                (0.6, 0, 0),
                (0.7, 0, 0),
                (0.8, 0, 0),
                (0.9, 0.6314, 0.6314),
                (1, 1, 1)),

        'green': ((0, 0, 0),
                  (0.1, 0, 0),
                  (0.2, 0.4471, 0.4471),
                  (0.3, 0.8941, 0.8941),
                  (0.4, 1, 1),
                  (0.5, 1, 1),
                  (0.6, 1, 1),
                  (0.7, 0.8941, 0.8941),
                  (0.8, 0.4471, 0.4471),
                  (0.9, 0, 0),
                  (1, 0, 0)),

        'blue': ((0, 1, 1),
                 (0.1, 0.6314, 0.6314),
                 (0.2, 0, 0),
                 (0.3, 0, 0),
                 (0.4, 0, 0),
                 (0.5, 0, 0),
                 (0.6, 0.7765, 0.7765),
                 (0.7, 1, 1),
                 (0.8, 1, 1),
                 (0.9, 1, 1),
                 (1, 1, 1)),
    }

    return LinearSegmentedColormap('Phase', cdict)


def frequency():
    """
    Create a phase colormap.

    :return: phase colormap
    :rtype: matplotlib.colors.LinearSegmentedColormap object
    """

    # Construct cmap dictionary
    cdict = {
        'red': ((0, 0, 0),
                (0.1, 1, 1),
                (0.2, 1, 1),
                (0.3, 0.9412, 0.9412),
                (0.4, 0.5765, 0.5765),
                (0.5, 0, 0),
                (0.6, 0, 0),
                (0.7, 0, 0),
                (0.8, 0, 0),
                (0.9, 0.6667, 0.6667),
                (1, 1, 1)),

        'green': ((0, 0, 0),
                  (0.1, 0, 0),
                  (0.2, 0.7451, 0.7451),
                  (0.3, 1, 1),
                  (0.4, 1, 1),
                  (0.5, 1, 1),
                  (0.6, 1, 1),
                  (0.7, 0.8157, 0.8157),
                  (0.8, 0.3333, 0.3333),
                  (0.9, 0, 0),
                  (1, 0, 0)),

        'blue': ((0, 0, 0),
                 (0.1, 0, 0),
                 (0.2, 0, 0),
                 (0.3, 0, 0),
                 (0.4, 0, 0),
                 (0.5, 0.4706, 0.4706),
                 (0.6, 0.8824, 0.8824),
                 (0.7, 1, 1),
                 (0.8, 1, 1),
                 (0.9, 1, 1),
                 (1, 1, 1)),
    }

    return LinearSegmentedColormap('Frequency', cdict)

if __name__ == '__main__':
    # Show colormap gradient
    gradient = np.linspace(0, 1, 256)
    gradient = np.vstack((gradient, gradient))

    fig = plt.figure()
    ax = fig.add_subplot(411)
    ax.imshow(gradient, interpolation='none', aspect='auto', cmap=bwr(0))
    ax.set_axis_off()
    ax.set_title("bwr")

    ax = fig.add_subplot(412)
    ax.imshow(gradient, interpolation='none', aspect='auto', cmap=seismic())
    ax.set_axis_off()
    ax.set_title("seismic")

    ax = fig.add_subplot(413)
    ax.imshow(gradient, interpolation='none', aspect='auto', cmap=phase())
    ax.set_axis_off()
    ax.set_title("phase")

    ax = fig.add_subplot(414)
    ax.imshow(gradient, interpolation='none', aspect='auto', cmap=frequency())
    ax.set_axis_off()
    ax.set_title("frequency")

    plt.show()
