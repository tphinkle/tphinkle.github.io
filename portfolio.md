---
layout: page
title: Portfolio
permalink: /portfolio/
---

I've written a few different pieces of software over the past two years for research and various other miscellaneous purposes. Here's a quick summary of some of the projects that I've completed.

### [nanoIV](https://github.com/tphinkle/nanoIV)

This is a GUI program written in C++ and Qt that enables remote control of a Keithley picoammeter. Two specific measurement protocols, IV curve and time-series measurement, are set-up and available simultaneously. The program displays the data in real-time and can be used to save the data. A separate script written in Python can be used to create a formatted Excel document from the acquired data. This was written to make my lab's IV curve measurements more efficient and to provide real-time feedback on the noise characteristics of the systems we measure.

### [pore stats](https://github.com/tphinkle/pore_stats)

This was a collection of Python programs I wrote as part of a fellowship for creating an open-source data analysis package for [resistive pulse experiments](https://tphinkle.github.io/research/#resistive_pulse_sensing). The total package consists of a GUI program for detecting, validating, and saving resistive pulse events in time-series data, and a back-end library for analyzing the data.

### [cell controller](https://github.com/tphinkle/cell_controller)

I wrote this program to control a few measurement instruments I use for my cancer cell experiments. The program is written in C++ and Qt, and uses multi-threading to control a [high-speed camera](http://www.phantomhighspeed.com/Home/gclid/CjwKEAiAkajDBRCRq8Czmdj-yFgSJADikZggiwmCFoUakGlh04kgyB43FtlUQCRi1ahD8Q_LpKD7WxoCblnw_wcB), [data acquisition card](http://www.ni.com/data-acquisition/), and a syringe pump. 

### [spectranalyzer](https://github.com/tphinkle/spectranalyzer)

This was a quick program I wote in Python and PyQt to teach my niece about sound, frequencies, etc. The app takes in sound from a connected microphone and displays the waveform or the power spectrum (PSD) to the screen.

<img src="http://tphinkle.github.io/images/portfolio/spectranalyzer/spectranalyzer.png" alt="spectranalyzer" style="width: 480px;" align="middle"/>
<img src="http://tphinkle.github.io/images/portfolio/spectranalyzer/spectranalyzer_fft.png" alt="spectranalyzer" style="width: 480px;" align="middle"/>




