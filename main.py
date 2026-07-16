# Copyright (c) 2020 brainlife.io
#
# This file is the main script for re-referencing MEG/EEG Epochs files.
#
# Author: Kamilya Salibayeva
# Indiana University

# set up environment
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'brainlife_utils'))

import mne

from brainlife_utils import (
    load_config,
    setup_matplotlib_backend,
    ensure_output_dirs,
    create_product_json,
    add_info_to_product,
    require_config_keys,
)

# Set up matplotlib for headless execution
setup_matplotlib_backend()

# Load configuration
config = load_config()
require_config_keys(config, ['epochs', 'ref_ch'])

fname = config['epochs']
ref_ch = config['ref_ch']

# Validate ref_ch: must be a non-empty string ('average', 'REST') or a list of channel names
if not ((isinstance(ref_ch, str) and ref_ch) or isinstance(ref_ch, list)):
    product_items = []
    add_info_to_product(
        product_items,
        f"Invalid ref_ch value: {ref_ch!r}. Must be a non-empty string ('average', 'REST') or a list of channel names.",
        'error'
    )
    create_product_json(product_items)
    sys.exit(1)

ensure_output_dirs('out_dir')

epochs = mne.read_epochs(fname)
epochs.set_eeg_reference(ref_channels=ref_ch)

# save mne/epochs
epochs.save(os.path.join('out_dir', 'epo.fif'))

# == CREATE PRODUCT.JSON ==
product_items = []
add_info_to_product(product_items, f"Re-referenced epochs using: {ref_ch}", 'success')
create_product_json(product_items)
