# TaskManCLI

**Note**: This project is hosted in a repository named `psychicCLI`, but the tool is referred to as `TaskManCLI` in the code.

TaskManCLI is a simple command-line interface (CLI) tool for managing tasks. It allows users to add, update, delete, and list tasks, with support for tracking task statuses (To-Do, In-Progress, Done) and timestamps for creation and updates. Tasks are stored in a `tasks.json` file for persistence.

## Table of Contents

- Features
- Installation
- Usage
- Contributing
- License
- Contact

## Features

- **Add Tasks**: Create new tasks with a description and a default "To-Do" status.
- **Update Tasks**: Modify task descriptions or update task statuses (To-Do, In-Progress, Done).
- **Delete Tasks**: Remove tasks by their ID.
- **List Tasks**: View all tasks, completed tasks, incomplete tasks, or tasks in progress, with details like ID, description, status, and timestamps.
- **Persistent Storage**: Tasks are saved in a `tasks.json` file for persistence between sessions.
- **User-Friendly Interface**: Interactive menu-driven interface with clear prompts and error handling.

## Installation

To set up TaskManCLI, follow these steps:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/bum-head/psychicCLI.git
   ```

2. **Navigate to the Project Directory**:

   ```bash
   cd psychicCLI
   ```

3. **Create a Virtual Environment** (optional but recommended):

   ```bash
   python3 -m venv env
   ```

4. **Activate the Virtual Environment**:

   - On Linux/Mac:

     ```bash
     source env/bin/activate
     ```

   - On Windows:

     ```bash
     env\Scripts\activate
     ```

5. **Install Dependencies**: TaskManCLI uses only Python standard libraries (`os`, `sys`, `json`, `datetime`), so no additional dependencies are required.

6. **Run the CLI**:

   ```bash
   python main.py
   ```

## Usage

TaskManCLI provides an interactive menu to manage tasks. Run the tool and select an option by entering the corresponding number:

```bash
python main.py
```

**Note**: TaskManCLI creates and modifies a `tasks.json` file in the project directory. Ensure you have write permissions in the directory where you run the tool to avoid `PermissionError` when adding, updating, or deleting tasks.

### Available Commands

1. **Add Task**: Prompts for a task description and creates a new task with a unique ID and "To-Do" status.

   - Example: Select `1` and enter a description like "Complete project report".

2. **Update Task**: Modify a task's description or status.

   - Update Description: `update-desc <task-id>` (e.g., `update-desc 1` to change the description of task ID 1).
   - Update Status: `update-task <task-id> <status>` (e.g., `update-task 1 progress` to set task ID 1 to "In-Progress").
   - Status options: `progress` (In-Progress), `done` (Done), `ndone` or `notdone` (To-Do).
   - To exit: Enter `back`.

3. **List All Tasks**: Displays all tasks with their ID, description, status, creation date, and last updated date.

   - Select `3`.

4. **List Completed Tasks**: Shows tasks with "Done" status.

   - Select `4`.

5. **List Incomplete Tasks**: Shows tasks with "To-Do" status.

   - Select `5`.

6. **List Ongoing Tasks**: Shows tasks with "In-Progress" status.

   - Select `6`.

7. **Delete Task**: Removes a task by ID.

   - Command: `delete <task-id>` (e.g., `delete 1` to remove task ID 1).
   - To exit: Enter `back`.

8. **Exit**: Closes the application.

   - Select `8`.

### Example Workflow

1. Run `python main.py`.
2. Select `1` to add a task, e.g., "Write README".
3. Select `2` to update, then enter `update-task 1 progress` to mark it as in progress.
4. Select `3` to list all tasks and verify the update.
5. Select `7` and enter `delete 1` to remove the task.

Tasks are saved in `tasks.json` in the project directory. Ensure write permissions in the directory to avoid file access errors.

## Contributing

Contributions are welcome! To contribute to TaskManCLI, please follow these steps:

1. Fork the repository.

2. Create a new branch for your feature or fix:

   ```bash
   git checkout -b feature-branch-name
   ```

3. Commit your changes:

   ```bash
   git commit -m "Brief description of changes"
   ```

4. Push your branch to your forked repository:

   ```bash
   git push origin feature-branch-name
   ```

5. Open a pull request against the main branch.

Please ensure your code follows Python PEP 8 style guidelines and includes appropriate error handling.

## Contact

For questions or feedback, contact the maintainer:

- GitHub: @bum-head