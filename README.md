# Brainrot Shell

Are you tired of using the same old regular shell? Are you a true skibidi sigma? Introducing **Brainrot Shell**—the new shell that's only for those who know 💀

Originally built as a CodeCrafters "Build Your Own X" challenge, Brainrot Shell has been upgraded to be actually useful with added features.

## Prerequisites

### Operating System
- **Windows** (untested on other operating systems but should work the same way)

### Python
- Python 3 installed and added to your system PATH

You can download Python from the [official Python website](https://www.python.org/).

## Installation

Follow these steps to install Brainrot Shell on your Windows system:

### 1. Download the Brainrot Shell Repository

#### Option 1: Clone the Repository with Git
If you have Git installed, you can clone the repository:

```bash
# Replace `repository-url` with the actual URL of the Brainrot Shell repository
git clone https://github.com/whirlxd/brainrot-shell.git
```

#### Option 2: Download ZIP
1. Visit the GitHub repository page.
2. Click on the **"Code"** button and select **"Download ZIP"**.
3. Extract the contents to a folder on your computer.

### 2. Run the Installation Script

#### Navigate to the Project Directory
Open Command Prompt and navigate to the directory where you saved the Brainrot Shell files:

```bash
cd path-to-brainrot-shell-folder
```

#### Run `install.bat`
Execute the installation script by typing:

```bash
install.bat
```

> **Note:** You may need to run Command Prompt as an administrator to ensure the script can modify system environment variables.

#### Follow the On-Screen Instructions
The script will:
- Copy `brainrot.py` and the `commands` directory to `%USERPROFILE%\Scripts`.
- Add `%USERPROFILE%\Scripts` to your system PATH if it's not already included.
- Create a wrapper batch file `brainrot.bat` to run the shell.

#### Restart Command Prompt
Close all Command Prompt windows and open a new one to apply the changes to your PATH.

## Usage

After installation, you can start using Brainrot Shell.

### Starting the Shell
Open Command Prompt and type:

```bash
brainrot
```

You should see the Brainrot Shell prompt:

```
@brainrot ~$
```

### Available Commands
Brainrot Shell is a toy shell but still incredibly useful. Here are some of the commands you can use:

| Command      | Description                                    |
|--------------|------------------------------------------------|
| `ragequit`   | Exit the shell.                               |
| `yap`        | Display a line of text (similar to `echo`).   |
| `typeshi`       | Display information about command types.   |
| `pwd`        | Print the current working directory.          |
| `hawktuah`   | Change the current directory.           |
| `loot`        | Display file contents.                        |
| `help`       | Display the help message.                     |
| `map`         | List files in the current directory.          |
| `touch`      | Create a new empty file.                      |
| `spawn`      | Create a new directory.                       |
| `despawn`      | Remove an empty directory.                    |
| `unalive`      | Remove a directory w/its contents.          |
| `wipeout`      | Clear the session        |
| `fanum`      | View the top 20 processes and their tax (cpu usage)      |
| `showgyatt`      | Show the files in directory sorted by their size and with it      |
| `ksi`      | Get ksi to say anything (like cat say).                    |
| `thickofit`      | Im in the thick of it everybody knows.           |





### Examples

#### Display a Message
```bash
@brainrot~$ yap "Hello, Brainrot!"
```

#### List Files
```bash
@brainrot~$ map
```

#### Print Working Directory
```bash
@brainrot~$ pwd
```

#### Change Directory
```bash
@brainrot~$ hawktuah path/to/directory
```

#### Create a New File
```bash
@brainrot~$ touch newfile.txt
```

#### Create a New Directory
```bash
@brainrot~$ spawn newdirectory
```

#### Remove a Directory
```bash
@brainrot~$ despawn olddirectory
```

#### Display File Contents
```bash
@brainrot~$ loot file.txt
```

#### Get Help
```bash
@brainrot~$ help
```

### Exiting the Shell
To exit Brainrot Shell, type:

```bash
@brainrot~$ ragequit
```

## Troubleshooting

### `'brainrot' is not recognized as an internal or external command`
- Ensure that the installation script ran successfully.
- Verify that `%USERPROFILE%\Scripts` is added to your system PATH.
- Restart Command Prompt to apply the changes to your PATH.

### `ModuleNotFoundError: No module named 'commands'`
- Ensure that the `commands` directory is located in `%USERPROFILE%\Scripts`.
- The `install.bat` script should have copied the `commands` directory. Try running the installation script again.

### `Python is not recognized`
- Ensure that Python 3.x is installed and added to your system PATH.
- You can verify by running:

```bash
python --version
```

## Uninstallation

To remove Brainrot Shell from your system:

### Delete Installed Files
Remove the following from `%USERPROFILE%\Scripts`:
- `brainrot.py`
- `brainrot.bat`
- `commands` directory

### Remove the Scripts Directory from PATH (Optional)
If you added `%USERPROFILE%\Scripts` to your PATH and no longer need it, you can remove it:

1. Search for **"Environment Variables"** in the Start menu.
2. Select **"Edit the system environment variables"**.
3. Click on **"Environment Variables"**.
4. Under **"User variables"** or **"System variables"**, find and select PATH.
5. Click **"Edit"** and remove `%USERPROFILE%\Scripts` from the list.

#### Restart Command Prompt
Close all Command Prompt windows and open a new one to apply the changes.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements. If you have a suggestion for a new name for a command or a new command, feel free to share it through an issue.

## Acknowledgements
Inspired by the CodeCrafters "Build Your Own X" challenge. The readme was made with help of chatgpt 💀.
