# Web scraping - Bitcoin price 

## Technical Details
The algorithm is written in Python 3.11.6 (main, Oct  8 2023, 05:06:43) [GCC 13.2.0] on linux.
The first stable released version is V1.

## Objective
The main goal of this algorithm is to advice the user when the price of the bitcoin goes under a certain threshold (chosen by the user).

## Data
The script downloads from the website "https://www.soldionline.it/quotazioni/criptovalute/bitcoin" the price of the bitcoin.

## Data output
The output is a Toast notifier, which appears as a pop-up advice only if the price of the Bitcoin reaches values under a predefinite threshold.
