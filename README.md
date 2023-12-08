# How to deploy locally

## Installing the model

### Install Ollama

Navigate to the Ollama website and follow the instructions to install Ollama on your machine.
https://ollama.ai/download

** Memory requirements **

- 7b models generally require at least 8GB of RAM
- 70b models generally require at least 64GB of RAM

### Installing Llama2-unscensored and running it

This command is neat because it will install the model and run it in one command. The model will run the ollama localhost:11434.

```bash
ollama run llama2-uncensored
```

## Running the interface

### Tutorial for macOS/Linux:

#### Step 1: Set up a Virtual Environment

Open a terminal and navigate to your project directory.

```bash
cd /path/to/your/project
```

Create a virtual environment named `.venv`.

```bash
python3 -m venv .venv
```

#### Step 2: Activate the Virtual Environment

On macOS/Linux:

```bash
source .venv/bin/activate
```

Your terminal prompt should change, indicating that the virtual environment is active.

#### Step 3: Install Dependencies

Ensure you are in the virtual environment, then install the required packages using `pip3`. Assuming you have a `requirements.txt` file:

```bash
pip3 install -r requirements.txt
```

#### Step 4: Run Your Model

Assuming your main Python file is named `main.py`, run it:

```bash
python3 main.py
```

#### Step 5: Deactivate the Virtual Environment

Once you're done using your application, deactivate the virtual environment:

```bash
deactivate
```

This step is optional, but it's good practice to deactivate the virtual environment when you're finished.

### Tutorial for Windows:

#### Step 1: Set up a Virtual Environment

Open a command prompt and navigate to your project directory.

```cmd
cd \path\to\your\project
```

Create a virtual environment named `.venv`.

```cmd
python -m venv .venv
```

#### Step 2: Activate the Virtual Environment

On Windows:

```cmd
.venv\Scripts\activate
```

Your command prompt should change, indicating that the virtual environment is active.

#### Step 3: Install Dependencies

Ensure you are in the virtual environment, then install the required packages using `pip`. Assuming you have a `requirements.txt` file:

```cmd
pip install -r requirements.txt
```

#### Step 4: Run Your Model

Assuming your main Python file is named `main.py`, run it:

```cmd
python main.py
```

#### Step 5: Deactivate the Virtual Environment

Once you're done using your application, deactivate the virtual environment:

```cmd
deactivate
```

This step is optional, but it's good practice to deactivate the virtual environment when you're finished.
