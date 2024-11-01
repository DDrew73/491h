<link rel="stylesheet" type="text/css" href="../../assets/css/styles.css">

## Noise and Filters
Noisy data is a fact of life in the space of robotics and cyberphysical systems. There are a huge number of noise sources that are relevant, with magnitude which depend on the particular physics governing signal transduction. Dealing with sensor signals and their associated noise to get them in interpretable states is the act of "signal processing." When we do this using a microcontroller/other computer, we call this "digital signal processing" or DSP. Two of the most important tools for signal processing are filters, which can remove unwanted features or components from incoming signals, and the Fourier transform, which converts temporal signals (occurring in time) to its equivalent in the frequency domain. We'll learn about the former here and the latter in the next reading. 

**Reading Material:**
- [Noise - Art of Electronics](assets/Noise_AoE.pdf) ~6 pages
- [Filters - Practical Electronics for Inventors](assets/Filters_PracticalElectronics.pdf) ~7 pages
- [Digital Low-Pass Filter on Arduino, Demo](https://www.youtube.com/watch?v=HJ-C4Incgpw&ab_channel=CurioRes) ~10 min

**Learning Outcomes:**
- Understand some of the common sources of noise in electronic components and signals
- Understand the high level functionality of a filter
- Understand the basic operation and intended functionality of some of the most common filters (e.g., low pass and high pass)
- Understand the basic design principles for a filter