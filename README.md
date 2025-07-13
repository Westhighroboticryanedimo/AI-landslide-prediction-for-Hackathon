# Landslide Hazard Prediction AI

A machine learning model that predicts landslide hazards based on soil characteristics and environmental factors using Decision Tree classification.

## Overview

This project analyzes soil data from Washington State to predict landslide hazards. The model uses various soil properties including erosion potential, flood hazard, construction hazard, slope, precipitation, drainage rate, and other geological factors to determine landslide risk.

## Features

- **Data Preprocessing**: Comprehensive cleaning and transformation of soil characteristics data
- **Feature Engineering**: Creates meaningful features from complex soil texture and precipitation data
- **Machine Learning Model**: Uses Decision Tree Classifier for landslide hazard prediction
- **Visualization**: Displays feature importance to understand key risk factors
- **Prediction Export**: Saves predictions to CSV for further analysis

## Requirements

```
pandas
scikit-learn
matplotlib
```

## Installation

1. Clone or download the repository
2. Install required packages:
   ```bash
   pip install pandas scikit-learn matplotlib
   ```

## Data Requirements

The code expects the following CSV files in the specified directory:
- `WA_Soils.csv` - Main soil characteristics dataset
- `ai_flood_predictions.csv` - Flood hazard predictions from a separate model

### Expected Data Columns

- `OBJECTID` - Unique identifier for each soil sample
- `SOIL_EROSION_POTNL` - Soil erosion potential (LOW, MEDIUM, HIGH)
- `SOIL_FLOOD_HAZARD` - Flood hazard level (SLIGHT, MODERATE, SEVERE)
- `SOIL_CONST_HAZARD` - Construction hazard level (SLIGHT, MODERATE, SEVERE)
- `SOIL_SLP_MAX_PC` - Maximum slope percentage
- `SOIL_PRECIP` - Precipitation range (e.g., "30-40 inches")
- `SOIL_DRAIN_RATE` - Soil drainage rate
- `SOIL_LAYER_RESTR` - Layer restriction (RESTRICTION, NO RESTRICT.)
- `SOIL_TXTR_MDFR` - Soil texture modifier (various soil types)
- `SOIL_ROOT_DPT` - Root depth (in inches)
- `SOIL_ROCK_FRAG` - Rock fragment percentage

## Usage

1. **Update File Paths**: Modify the file paths in the code to match your data location:
   ```python
   data = pandas.read_csv(r'path/to/your/WA_Soils.csv')
   flood_hazard_prediction = pandas.read_csv(r'path/to/your/ai_flood_predictions.csv')
   ```

2. **Run the Script**:
   ```bash
   python Landslide_Ai.py
   ```

3. **View Results**:
   - Model accuracy will be printed to console
   - Feature importance plot will be displayed
   - Predictions saved to `ai_landslide_predictions.csv`

## How It Works

### 1. Data Loading and Preprocessing
- Loads soil characteristics data and flood predictions
- Randomly shuffles data for better training
- Strips whitespace from categorical variables

### 2. Feature Engineering
The code performs extensive feature transformation:

- **Categorical Encoding**: Maps text categories to numerical values
  - Erosion potential: LOW(0), MEDIUM(1), HIGH(2)
  - Flood/Construction hazard: SLIGHT(0), MODERATE(1), SEVERE(2)
  
- **Precipitation Processing**: Extracts low and high values from range strings
  - Example: "30-40 inches" → SOIL_PRECIP_LOW: 30, SOIL_PRECIP_HIGH: 40
  
- **Soil Texture Normalization**: Consolidates 100+ soil texture types into standard categories
  - Example: "V.COBBLY LOAM" → "LOAM"
  
- **Rock Fragment Processing**: Extracts percentage ranges for rock content

### 3. Target Variable Creation
Creates landslide hazard labels based on risk factors:
```python
SOIL_LANDSLIDE_HAZARD = (erosion > 1) OR (flood > 1) OR (construction > 1)
```

### 4. Model Training
- Uses Decision Tree Classifier from scikit-learn
- 80/20 train-test split with stratification
- Evaluates model accuracy on test set

### 5. Feature Importance Analysis
Generates a horizontal bar chart showing which soil characteristics most influence landslide predictions.

### 6. Prediction Generation
- Applies trained model to entire dataset
- Handles missing values using mean imputation
- Exports results with "Yes"/"No" labels

## Output Files

- `AWSOMECOOLDATA.csv` - Processed dataset with all transformations
- `ai_landslide_predictions.csv` - Final predictions with OBJECTID mapping

## Model Performance

The model outputs accuracy metrics and feature importance rankings to help understand:
- How well the model performs on test data
- Which soil characteristics are most predictive of landslide risk

## Key Features Analyzed

Based on the data processing, the model considers:
- **Slope characteristics** - Maximum slope percentage
- **Precipitation patterns** - High and low precipitation ranges
- **Soil drainage** - How well soil drains water
- **Layer restrictions** - Presence of impermeable layers
- **Soil texture** - Type and composition of soil
- **Rock content** - Percentage of rock fragments
- **Root depth** - How deep roots can penetrate

## Limitations

- Model assumes landslide risk is primarily determined by high erosion, flood, or construction hazards
- Relies on categorical thresholds rather than continuous risk assessment
- Performance depends on quality and completeness of input soil data
- Geographic scope limited to Washington State soil characteristics

## Future Improvements

- Incorporate additional environmental factors (seismic activity, vegetation cover)
- Use ensemble methods for improved prediction accuracy
- Add temporal analysis for seasonal landslide risk variations
- Implement cross-validation for more robust model evaluation

## License

This project is for a hackathon called "United Hacks V5"

## Contact

For questions or improvements, please refer to the project documentation or create an issue in the repository.

## Additional Info

To get the map.py code to work, download the WA_Soils.py here -> https://drive.google.com/file/d/1La68gplaKxC1PmR2RleyolHCFdZJhfvO/view?usp=sharing


