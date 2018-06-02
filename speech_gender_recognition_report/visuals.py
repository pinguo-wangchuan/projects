###########################################
# Suppress matplotlib user warnings
# Necessary for newer version of matplotlib
import warnings
warnings.filterwarnings("ignore", category = UserWarning, module = "matplotlib")
#
# Display inline matplotlib plots with IPython
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'inline')
###########################################

import matplotlib.pyplot as pl
import matplotlib.patches as mpatches
import numpy as np
import pandas as pd
from time import time
from sklearn.metrics import accuracy_score


def distribution_sexID(data, transformed = False):
    """
    Visualization code for displaying skewed distributions of features
    """
    # male index & female index
    male_index = data[data['label'] == 'male'].index.tolist()
    female_index = data[data['label'] == 'female'].index.tolist()

    # male & female data set
    male_samples = data.drop(female_index)
    female_samples = data.drop(male_index)

    # Create figure
    fig = pl.figure(figsize = (18,15));
    if transformed:
        features_list = ['skew', 'kurt']
    else:
        features_list = ['meanfreq', 'sd', 'median', 'Q25', 'Q75', 'IQR', 'skew', 'kurt', 'sp.ent', 'sfm', 'mode', 'centroid', 'meanfun', 'minfun', 'maxfun', 'meandom', 'mindom', 'maxdom', 'dfrange', 'modindx']
    # Skewed feature plotting
    for i, feature in enumerate(features_list):
        ax = fig.add_subplot(5, 4, i+1)
        ax.hist(male_samples[feature], bins = 25, color = '#00A0A0', alpha = 0.6, label = 'male')
        ax.hist(female_samples[feature], bins = 25, color = '#ff0060',alpha = 0.6, label = 'female')
        ax.set_title("'%s' Feature Distribution"%(feature), fontsize = 14)
        ax.set_xlabel("Value")
        ax.set_ylabel("Number of Samples")
        ax.set_ylim((0, 1000))
        ax.set_yticks([0, 250, 500, 750, 1000])
        ax.set_yticklabels([0, 250, 500, 750, ">1000"])
        ax.legend(framealpha = 0.8)

    # Plot aesthetics
    if transformed:
        fig.suptitle("", \
            fontsize = 16, y = 1.03)
    else:
        fig.suptitle("Samples Distributions of Features", \
            fontsize = 16, y = 1.03)

    fig.tight_layout()
    fig.show()

def evaluate(results, accuracy):
    """
    Visualization code to display results of various learners.

    inputs:
      - learners: a list of supervised learners
      - stats: a list of dictionaries of the statistic results from 'train_predict()'
      - accuracy: The score for the naive predictor
    """

    # Create figure
    fig, ax = pl.subplots(2, 2, figsize = (11,8))

    # Constants
    bar_width = 0.2
    colors = ['#A00000','#00A0A0','#00A000','#C0FF20']

    # Super loop to plot four panels of data
    for k, learner in enumerate(results.keys()):
        for j, metric in enumerate(['train_time', 'acc_train', 'pred_time', 'acc_val']):
            for i in np.arange(3):

                # Creative plot code
                ax[j/2, j%2].bar(i+k*bar_width, results[learner][i][metric], width = bar_width, color = colors[k])
                ax[j/2, j%2].set_xticks([0.3, 1.3, 2.3])
                ax[j/2, j%2].set_xticklabels(["1%", "10%", "100%"])
                ax[j/2, j%2].set_xlabel("Training Set Size")
                ax[j/2, j%2].set_xlim((-0.1, 3.0))

    # Add unique y-labels
    ax[0, 0].set_ylabel("Time (in seconds)")
    ax[0, 1].set_ylabel("Accuracy Score")
    ax[1, 0].set_ylabel("Time (in seconds)")
    ax[1, 1].set_ylabel("Accuracy Score")

    # Add titles
    ax[0, 0].set_title("Model Training")
    ax[0, 1].set_title("Accuracy Score on Training Subset")
    ax[1, 0].set_title("Model Predicting")
    ax[1, 1].set_title("Accuracy Score on Validation Set")

    # Add horizontal lines for naive predictors
    ax[0, 1].axhline(y = accuracy, xmin = -0.1, xmax = 3.0, linewidth = 1, color = 'k', linestyle = 'dashed')
    ax[1, 1].axhline(y = accuracy, xmin = -0.1, xmax = 3.0, linewidth = 1, color = 'k', linestyle = 'dashed')

    # Set y-limits for score panels
    ax[0, 1].set_ylim((0, 1))
    ax[1, 1].set_ylim((0, 1))

    # Create patches for the legend
    patches = []
    for i, learner in enumerate(results.keys()):
        patches.append(mpatches.Patch(color = colors[i], label = learner))
    pl.legend(handles = patches, bbox_to_anchor = (-0.1, 2.55), \
               loc = 'upper center', borderaxespad = 0., ncol = 2, fontsize = 'x-large')

    # Aesthetics
    pl.suptitle("Performance Metrics for four Supervised Learning Models", fontsize = 16, y = 1.10)
    pl.tight_layout()
    pl.show()

def evaluate_test(results, accuracy):
    """
    Visualization code to display results of various learners.

    inputs:
      - learners: a list of supervised learners
      - stats: a list of dictionaries of the statistic results from 'train_predict()'
      - accuracy: The score for the naive predictor
    """

    # Create figure
    fig, ax = pl.subplots(2, 2, figsize = (11,8))

    # Constants
    bar_width = 0.2
    colors = ['#A00000','#00A0A0','#00A000','#C0FF20']

    # Super loop to plot four panels of data
    for k, learner in enumerate(results.keys()):
        for j, metric in enumerate(['train_time', 'acc_train', 'pred_time', 'acc_val']):
            for i in np.arange(3):

                # Creative plot code
                ax[j/2, j%2].bar(i+k*bar_width, results[learner][i][metric], width = bar_width, color = colors[k])
                ax[j/2, j%2].set_xticks([0.3, 1.3, 2.3])
                ax[j/2, j%2].set_xticklabels(["1%", "10%", "100%"])
                ax[j/2, j%2].set_xlabel("Training Set Size")
                ax[j/2, j%2].set_xlim((-0.1, 3.0))

    # Add unique y-labels
    ax[0, 0].set_ylabel("Time (in seconds)")
    ax[0, 1].set_ylabel("Accuracy Score")
    ax[1, 0].set_ylabel("Time (in seconds)")
    ax[1, 1].set_ylabel("Accuracy Score")

    # Add titles
    ax[0, 0].set_title("Model Training")
    ax[0, 1].set_title("Accuracy Score on Training Subset")
    ax[1, 0].set_title("Model Predicting")
    ax[1, 1].set_title("Accuracy Score on test Set")

    # Add horizontal lines for naive predictors
    ax[0, 1].axhline(y = accuracy, xmin = -0.1, xmax = 3.0, linewidth = 1, color = 'k', linestyle = 'dashed')
    ax[1, 1].axhline(y = accuracy, xmin = -0.1, xmax = 3.0, linewidth = 1, color = 'k', linestyle = 'dashed')

    # Set y-limits for score panels
    ax[0, 1].set_ylim((0, 1))
    ax[1, 1].set_ylim((0, 1))

    # Create patches for the legend
    patches = []
    for i, learner in enumerate(results.keys()):
        patches.append(mpatches.Patch(color = colors[i], label = learner))
    pl.legend(handles = patches, bbox_to_anchor = (-0.1, 2.55), \
               loc = 'upper center', borderaxespad = 0., ncol = 2, fontsize = 'x-large')

    # Aesthetics
    pl.suptitle("Performance Metrics for four Supervised Learning Models", fontsize = 16, y = 1.10)
    pl.tight_layout()
    pl.show()
