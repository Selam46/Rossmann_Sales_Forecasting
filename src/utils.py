import os
import traceback
import matplotlib.pyplot as plt
import logging

def save_visualization(fig, title):
    path = f"../outputs/visualizations/{title}.png"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    fig.savefig(path)
    plt.close(fig)

def log_exception(e):
    logging.error(traceback.format_exc())
