"""
Details about the Doument:
"""

# For parsing passed arguemtns, Built-in
import argparse
# Numpy library for array manipualtion, Required for Lilcom
import numpy as np
# Main package for audio compression and decompression, Principal
import lilcom
# For mathematic calculus, Built-in
import math

globalVals = dict.fromkeys(["dataset", "samplerate"])


def PSNR(originalArray, reconstructedArray):
    """ This function calculates the peak signal to noise ratio between a
    signal and its reconstruction

       Args:
        originalArray: A numpy array which should be the original array
        before compression and reconstruction.
        reconstructedArray: A numpy array which in this case should be an
        array which is reconstructed from the compression function.
       Returns:
           A rational number which is the result of psnr between two given
    """
    # Convert both to float.
    if originalArray.dtype == np.int16:
        originalArray = originalArray.astype(np.float32) / 32768
    if reconstructedArray.dtype == np.int16:
        reconstructedArray = reconstructedArray.astype(np.float32) / 32768

    # Correct for any differences in dynamic range, which might be caused
    # by attempts of compression libraries like mp3 to avoid overflow.
    reconstructedArray *= np.sqrt((originalArray ** 2).sum() /
                                  (reconstructedArray ** 2).sum())

    max_value = float(np.max(np.abs(originalArray)))
    mean_square_error = (((originalArray - reconstructedArray) ** 2).sum() /
                         originalArray.size)
    if mean_square_error != 0:
        psnr = 20 * math.log10(max_value) - 10 * math.log10(mean_square_error)
    else:
        psnr = math.inf

    return psnr


def evaluate(filename=None, audioArray=None, algorithm="lilcom",
             additionalParam=None):
    """ This function does an evaluation on the given audio array, with
            the requested algorithm and additional parameters. As a result
            it returnes a map including the bitrate, a hash and the psnr
            result with the given audio array.

       Args:
        filename: The name of the file used for compression. It is requiered
            for some compression algorithms like MP3 which needs some file
            manipulations
        audioArray: Numpy array including original file. It is required for
            PSNR evaulation. If None value was passed, the function will
            load it from the passed filename.
        algorithm: The desired algorithm which will show which algorithm is
            chosen to be evaulated. Default value is set to lilcom
        additionalParam: Parameters which each algorithm is supposed to have.
            i.e. For lilcom it contains lpc-order and for MP3 it will have
            chosen bitrate.
       Returns:
           ///////// COMPLETE
    """
    global settings
    returnvValue = dict.fromkeys(["bitrate", "psnr", "hashKey"])

    """
    In case of empty input audio array it loads the array. The audio array is
        required for evaluation subroutine call 'PSNR'
    """
    if audioArray is None:
        if settings["sampleRate"] != 0:
            audioArray = waveRead(filename, settings["sampleRate"])

    # Evaluation Procedure for lilcom
    if algorithm == "lilcom":
        pass
    # Evaluation Procedure for MP3
    elif algorithm == "MP3":
        pass
    # Evaluation for additional compression library
    else:
        pass


def waveRead(filename, sampleRate=None):
    """ This function reads a wavefile at a desired sample rate and returns
            it in form of a numpy array

       Args:
        filename: The name of the file. File should be in wav format
            otherwise it will encounter error.
        sampleRate: an integer denoting the number of samples in a unit time.
            In case this is set to None, the function will choose the sample-
            -rate determined by arguemtns passed in while calling the script,
            otherwise the samplerate of the original wav file.

       Returns:
           a Numpy array of the given audio file.
    """
    global settings
    pass


# Parsing input arguments
parser = argparse.ArgumentParser(description="Lilcom reconstruction test \
            module")
parser.add_argument("--dataset", "-d",
                    help="The directory of test dataset")
parser.add_argument("--samplerate", "-s",
                    help="Number of samplings in a unit time for each audio")
parser.add_argument("--releaselog", "-l",
                    help="The name of the log file")
parser.add_argument("--releasedf", "-c",
                    help="The name of the csv file including results")
args = parser.parse_args()

# Global values for settings
settings = dict.fromkeys(["dataset-dir", "sample-rate", "release-log",
                         "release-df"])

if args.dataset:
    settings["dataset-dir"] = args.dataset
else:
    settings["dataset-dir"] = "None"

if args.samplerate:
    settings["sample-rate"] = int(args.samplerate)
else:
    settings["sample-rate"] = 0

if args.releasedf:
    settings["release-df"] = args.releasedf
else:
    settings["release-df"] = None

if (args.releaselog):
    settings["release-log"] = args.releaselog
else:
    settings["release-log"] = None


evaulators = [
    {
        "algorithm": "lilcom",
        "additionalParam": 4
    },
    {
        "algorithm": "MP3",
        "additionalParam": "320k"
    },
    {
        "algorithm": "MP3",
        "additionalParam": "256k"
    },
    {
        "algorithm": "MP3",
        "additionalParam": "224k"
    },
    {
        "algorithm": "MP3",
        "additionalParam": "192k"
    },
    {
        "algorithm": "MP3",
        "additionalParam": "160k"
    }
]
