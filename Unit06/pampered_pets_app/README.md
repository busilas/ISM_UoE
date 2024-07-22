# Pampered Pets Risk Assessment Application

## Overview

Pampered Pets is a local business aiming to expand its online presence and improve internal processes. This Python application provides tools to visualize and evaluate potential risks associated with this transition. The application uses an attack tree model to assess various threats and calculate overall risk values.

## Features

- **Load Attack Tree from File**: Import attack tree data from JSON, YAML, or XML files.
- **Visualize Attack Tree**: Generate and view a visual representation of the attack tree.
- **Add Leaf Node Values**: Input and update risk values for individual nodes in the tree.
- **Aggregate Values and Calculate Total Threat Value**: Compute the total threat value by summing up the values of all nodes.
- **Export Attack Tree as Image**: Save the visual representation of the attack tree as PNG or JPG files.

## Prerequisites

Ensure you have Python 3.7 or later installed on your system. This project also requires several Python libraries, which can be installed using `pip`.

## Cloning the Repository

To clone this repository to your local machine, follow these steps:

1. Open your terminal or command prompt.
2. Run the following command to clone the repository:

    ```bash
    git clone https://github.com/yourusername/pampered-pets-risk-assessment.git
    ```

3. Navigate into the project directory:

    ```bash
    cd pampered-pets-risk-assessment
    ```

## Installation

You can install the required libraries by using `pip`. Run the following command to install all dependencies listed in `requirements.txt`:

```bash
pip install -r requirements.txt

