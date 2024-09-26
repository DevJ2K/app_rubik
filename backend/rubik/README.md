# Rubik

![Python version](https://img.shields.io/badge/Python-3.9%2B-blue)
<!-- ![License](https://img.shields.io/badge/License-MIT-green) -->

## Description

This project is a Rubik's Cube Solver designed to find the most efficient solution using the fewest possible moves. The purpose is to implement a powerful algorithm that can analyze a given cube state and generate an optimal sequence of spins to solve it. Key features include advanced pathfinding techniques, handling various cube configurations, and minimizing the number of moves required to reach the solved state.

## Installation

### Prerequisites

Ensure you have Python 3.9 or newer installed. You can download the latest version of Python from the official [Python website](https://www.python.org/downloads/).

### Setup

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/DevJ2K/app_rubik.git
    cd app_rubik/backend/rubik
    ```

2. **(Optional) Create a Virtual Environment:**

    It's recommended to use a virtual environment to manage dependencies.

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies:**

    If there are any dependencies, you should list them in a `requirements.txt` file. Install them using:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Running the Script

You can run the script in one of the following ways:

1. **Make the script executable:**

   ```bash
    chmod +x main.py
    ```

    Then execute it directly:

    ```bash
    ./main.py "F U B' D2"
    ```

2. **Using the Python command:**

    ```bash
    python3 main.py "F U B' D2"
    ```

### Expected Output

Once the script is run successfully, you should see the following output:

```
Solution: B' U' F' R' U' L2 U R' R2 L2 U' L2 D R2 B2 U L2 D' B2 F2 U2 B2 L2 U2 R2 D2 F2 D2
Nombre de coups: 28
Temps écoulé: 0.652 secondes
```

### Use Case

<!-- Provide examples or scenarios where your project could be used. For instance: -->

<!--# Example -->
```bash
./main.py "your-sequences"
```

### Visual Overview

Below is a visual representation of the project’s functionality:

<img src="./gitimages/overview.png" width="100%">

<!--
### Contributing

If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.

1. Fork the repository.
2. Create a new feature branch (`git checkout -b feature-branch-name`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch-name`).
5. Open a pull request.


### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Contact

If you have any questions, feel free to reach out to the project maintainer at `contact@devj2k.com`.
-->
