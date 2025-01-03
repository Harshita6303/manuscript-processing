# Manuscripts Time Prediction

This project focuses on predicting the time and date of completion for South Indian language manuscripts using deep learning and image processing techniques. It leverages advanced models to analyze manuscript images and textual data from the 16th to 21st centuries. 

## Table of Contents

- [Overview](#overview)
- [Dataset](#dataset)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributors](#contributors)
- [Future Enhancements](#future-enhancements)

---

## Overview

This project aims to bridge historical linguistics with modern technology by accurately predicting the date of manuscript completion. The focus is on Hindi language, using datasets spanning multiple centuries, enabling insights into linguistic evolution and cultural history.

### Key Features
- Use of **Deep Learning** models for time-period classification.
- Image preprocessing with **Tesseract OCR** for text extraction.
- Trained models achieve predictions based on manuscript features like style, vocabulary, and script.

---

## Dataset

The dataset consists of:
- Manuscripts written in South Indian languages from the **16th, 17th, 18th, 19th, and 20th centuries**.
- Textual data extracted from images using **Tesseract OCR**.

You can access the datasets for each century from the following links:
- [1600's Data](https://drive.google.com/file/d/1uSzf0Nw9jAJc4nWn4G199WXhFpsODcNb/view?usp=drive_link)
- [1700's Data](https://drive.google.com/file/d/13oEFuosdcv7xAVAj_6ajC7c-rnF1iQqf/view?usp=drive_link)
- [1800's Data](https://drive.google.com/file/d/1H6AbaAORedOItiNuCCkCrYnB7ONbk0JU/view?usp=sharing)
- [1900's Data](https://drive.google.com/file/d/1WxcGq0ke6DjyjiL51tvsxZFNoGgFOIBo/view?usp=drive_link)

Additionally, you can explore a broader collection of texts through the [Internet Archive - English Collection](https://archive.org/details/texts?tab=collection&query=english).

### Dataset Structure
Files are named by century:
- `1600.txt`, `1700.txt`, `1800.txt`, `1900.txt`, `2000.txt`

Dataset path:
`C:/Users/harsh/OneDrive/Desktop/manuscripts2/`

---

## Technologies Used

- **Python**: Core programming language.
- **TensorFlow**: For building deep learning models.
- **Tesseract OCR**: For text extraction from manuscript images.
- **Image Processing**: Preprocessing images for model input.
- **Data Annotation**: Classifying and labeling manuscript periods.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/manuscript-prediction.git
   cd manuscript-prediction
