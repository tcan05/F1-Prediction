# F1-Prediction

## About This Project
This project currently predicts whether a given race car will win the race or not. To create the main F1 dataset, multiple datasets were cleaned and combined. Each cleaned and combined dataset was saved to easily backtrack if a mistake was made. Also, a utils file was created to fasten the operations required for data cleaning. The project utilizes Random Forest Classifier as a machine learning algorithm and uses SMOTE to equalize the 0 and 1 values. After applying SMOTE, the program achieves highly increased Recall value for 1.

## Requirements
- Python 3.10+

## Installation
1. Clone the repository:
```bash
git clone https://github.com/tcan05/F1-Prediction.git 
```

2. Navigate to the project directory:
```bash
cd F1-Prediction/F1 Test
```

3. Run the application:
```bash
python main.py
```
