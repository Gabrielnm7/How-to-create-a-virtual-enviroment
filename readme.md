<h1 align="center"> Tutorial on how to set a virtual environment </h1>

## For Spanish Version, [Click here](./ES%20-%20version)

### Setting Up the Virtual Environment

To create a virtual environment, first make sure you're in the directory where you want the environment to be created. Then, run the following command in the terminal:

```bash
python -m venv example-venv
```

This command will generate a folder named `example-venv` in the current working directory and will use your current version of Python to set up the environment. You can check which version of Python you're using by running:

```bash
python --version
```

> [!TIP]
> 1. A common path for the virtual environment directory is `venv` (short for **V**irtual **ENV**ironment)
> 2. Do not modify anything within this folder.

To activate the virtual environment (while in the directory of your project), type:
```bash
.\example-venv\Scripts\activate
```

## `Note` if you encounter an error like:
> Cannot load file C:\Users\User\Desktop\testing\example-venv\Scripts\activate.ps1 because running scripts is disabled on this system...

The error you're seeing is due to the PowerShell execution policy on your system being configured to not allow script execution, which is a security measure.

To solve this problem, you can temporarily change the execution policy to allow script execution. Here's how you can do it:

Open PowerShell as an administrator.
Run the following command:

```bash
Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope CurrentUser
```

For security reasons, you may want to revert the execution policy back to its original value after activating your virtual environment. You can do so with the following command:
```bash
Set-ExecutionPolicy -ExecutionPolicy Restricted -Scope CurrentUser
```

## Once you hit `enter` in the terminal to activate the environment, you'll see something like this:

Before hitting `enter`:
> PS C:\Users\user\Desktop\testing

After hitting `enter`:

> (venv) PS C:\Users\user\Desktop\testing

Within this environment, you'll have pre-installed packages. You can view them with the command:

```bash
pip list
```
and if you need to install any additional packages, you can do so with pip install (let's see how to install pandas):
```bash
pip install pandas
```
## Let's get to the important part

Exporting the packages to a `.txt` file. To do this, type the following command in the console:

```bash
pip freeze > requirements.txt 
```
Once you have the requirements.txt, if you ever need the environment to reinstall the packages because you're using another computer, you should execute the following command within the `venv`:

```bash
pip install -r .\requirements.txt
```
Ensure that you correctly specify ***the file path***.

To exit the environment, simply run the following code in the terminal:

```bash
deactivate
```