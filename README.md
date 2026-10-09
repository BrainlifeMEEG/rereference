# Set EEG Reference

[![Run on Brainlife.io](https://img.shields.io/badge/Brainlife-bl.app.745-blue.svg)](https://doi.org/10.25663/brainlife.app.745)

## Description

This Brainlife.io application re-references EEG data stored as MNE `Epochs`. It calls
`mne.Epochs.set_eeg_reference()` to recompute the reference from the recording's collection-time
reference to a chosen scheme: the average of all EEG channels, the Reference Electrode
Standardization Technique infinity reference (REST), or a user-specified list of channels.

The app generates:
- Re-referenced epochs in MNE-Python format

## Inputs

- **`epochs`** (`neuro/meeg/mne/epochs`): epoched EEG data to re-reference (required)

## Outputs

- **`out_dir/meg-epo.fif`** (`neuro/meeg/mne/epochs`): re-referenced epochs

## Configuration Parameters

| key | type | default | description |
|---|---|---|---|
| `ref_ch` | string \| list | `"average"` | Reference scheme: `"average"` for the average of all EEG channels, `"REST"` for the Reference Electrode Standardization Technique infinity reference, or a list of channel names to use as the new reference. |

## Usage

### Running on Brainlife.io

1. Upload or select your epoched EEG data file (MNE `Epochs`, `.fif`)
2. Select the rereference app
3. Choose the reference scheme (`average`, `REST`, or a list of channel names) via `ref_ch`
4. Submit the task
5. Monitor task completion and download the re-referenced epochs from `out_dir`

### Local Testing

```bash
# Update config.json with your epochs path and desired ref_ch
# Then run:
python main.py
```

## Authors

- Kamilya Salibayeva (https://github.com/KSalibay)

## Citations

- Hayashi, S., Caron, B.A., Heinsfeld, A.S. et al. brainlife.io: a decentralized and open-source cloud platform to support neuroscience research. Nat Methods 21, 809–813 (2024). https://doi.org/10.1038/s41592-024-02237-2
- Gramfort, A. et al. MEG and EEG data analysis with MNE-Python. Front. Neurosci. 7, 267 (2013). https://doi.org/10.3389/fnins.2013.00267

## Funding Acknowledgement

brainlife.io is publicly funded. We kindly ask that you acknowledge the funding below in your code and publications.

[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-1636893](https://img.shields.io/badge/NSF_BCS-1636893-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-ACI-1916518](https://img.shields.io/badge/NSF_ACI-1916518-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1916518)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NIH-NIBIB-R01EB029272](https://img.shields.io/badge/NIH_NIBIB-R01EB029272-green.svg)](https://grantome.com/grant/NIH/R01-EB029272-01)
[![NIH-NIBIB-R01EB030896](https://img.shields.io/badge/NIH_NIBIB-R01EB030896-green.svg)](https://grantome.com/grant/NIH/R01-EB030896-01)

## License

Copyright (c) 2026 MEEG Brainlife team. Licensed under AGPL-3.0, see [license.txt](license.txt).
