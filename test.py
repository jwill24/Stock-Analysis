import os, sys
from functions import plot_single_stock, compile_data, visualize_data, \
process_data_for_labels, buy_sell_hold, extract_featuresets, do_ml

do_ml('AMZN')

do_ml('CMS')

do_ml('CME')
