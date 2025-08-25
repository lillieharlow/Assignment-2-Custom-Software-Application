# Version Control & Testing Evaluation
ISK1001 - Assessment 2

### Contents:
- [Version Control](#version-control)
    - [Subversion (SVN) vs GitHub (Git)](#subversion-svn-vs-github-git)
    - [Examples](#real-world-examples)
- [TO DO. Application VCS](#to-do-application-vcs)
    - [Convention](#convention)
    - [Commands](#commands)
    - [Commits & Version History](#commits-version-history)
    - [Code Review Process](#code-review-process)
    - [.gitignore](#gitignore)
    - [Branching](#branching)
    - [Merging & Pulling Challenges](#merging-pulling-challenges)
- [Testing Evaluation](#testing-evaluation)
    - [Standard Testing Process](#standard-testing-process)
    - [Test-Driven Development (TDD)](#test-driven-development-tdd)
    - [Manual Testing and User Stories](#manual-testing-and-user-stories)
- [Conclusion](#conclusion)
- [Reference List](#reference-list)

## Version Control
Version Control Systems (VCS) are essential tools in modern software development. They manage and track changes to source code, files, and directories, allowing developers to:

- Collaborate on projects without overwriting each other’s work.
- Maintain a detailed history of changes and revert to earlier versions if required.
- Experiment safely by branching and merging code.
- Protect and secure critical files through structured workflows.

VCS solutions fall into three categories: local, centralized, and distributed. There are numerous VCS available each with their own strengths and weaknesses. Below is a comparison between two widely used systems: Subversion (SVN) and GitHub (Git).

### Subversion (SVN) vs GitHub (Git)

| Feature / Aspect         | Subversion (SVN)                                         | GitHub (Git)                                                      |
|-------------------------|----------------------------------------------------------|-------------------------------------------------------------------|
| Type                    | Centralized Version Control System (CVCS)                | Distributed Version Control System (DVCS)                         |
| Repository Control      | Single, central repository                                 | Every developer has a full local copy of repo                     |
| Ease of Use             | Easier for beginners, straightforward commands            | Steeper learning curve, complex commands                           |
| Access Control          | Fine-grained control (file/directory level)               | Repo-level permissions, less granular                             |
| Handling Large Files    | Efficiently stores and compresses binaries                | Needs external tools for binaries                                  |
| Branching & Merging     | Limited, can be error-prone                               | Fast, flexible, and reliable                                      |
| Workflow                | Linear, structured, easy to audit                         | Supports multiple branching strategies, flexible workflows        |
| Offline Work            | Depends on central server for most operations             | Fully supports offline work with local commits                    |
| Single Point of Failure | Yes, central server failure blocks development             | No, distributed nature avoids single failures                    |
| Scalability             | Not ideal for large teams                               | Scales well for large global and open-source projects             |
| Community & Ecosystem   | Smaller, traditional user base                          | Huge open-source community + integrations (CI/CD, reviews, hosting, etc.) |
| Security                | Strong auditing and detailed access permissions          | Data integrity via cryptographic hashes (but less specific permissions) |
| Reliability & Maturity  | Mature, very stable workflows                            | Stable, fast-growing ecosystem, widely adopted                    |

### Examples
- Game Developers prefer SVN for handling large binary assets (textures, audio, etc.) and its file locking features.
- Government agencies choose SVN for compliance, strict access controls, and detailed audit trails.
- Popular open source projects like React and Django thrive on GitHub due to global collaboration, pull requests, and review-driven workflows.
- Remote software teams rely on GitHub’s distributed model, pull requests, and collaboration tools to work efficiently across the globe.

## TO DO. Application VCS
Project link: https://github.com/lillieharlow/TO_DO._App

Using GitHub for my TO DO. CLI app was a crucial part of my workflow. Even as a solo project, version control gave me a safety net, a way to track my progress, and a chance to build habits needed for professional settings. I learned that version control is more than just backing up your work, it's about working smarter.

Clear commit messages matter, `.gitignore` protects both privacy and professionalism, and branching provides the freedom to experiment without breaking things. Hosting my app on GitHub laid a strong foundation for future collaboration, familiarising myself with git commands, commit messages, pull and push requests, branches, and merging, all of which evolve my professional skills and workflow.

### Commands
Frequently using `git add .`, `git commit -m "I am a message"`, and `git push` in CLI became second nature, allowing me to easily push to my remote repository. I also dabbled in some advanced commands e.g. `git checkout -b testing`, `git push origin testing` and `git branch --set-upstream-to=origin/testing testing` when branching my repository.

### Commits & Version History
Committing frequently provided a safety net for my developing work, helping capture the evolution of my project with 112 commits. The beginning of this project saw two major shifts in project direction, which were reflected in my commit history. Originally wanting to create a Virtual Pet Application and then an application that was based around animal facts and quizzes. Completely seperate to the project created, in hindsight, I should have branched at these points to isolate these changes and switched the new branches to main branch.

At times, my commit messages were vague or confusing, which made it hard for me to understand my project history when a revisit was needed. Improvements can definitely be made by adopting a more conventional commit message style in future projects e.g. `feat: New branch called TDD_testing. Implement standard TDD testing.` or `test: title_upper method added to class Task in tasks.py PASSED.`, seen in the projects final commit messages. This will greatly increase clear communication, readability, and tracking of future projects.

Version history came in very handy when I accidentally deleted my `README.md` file. I was able to quickly restore it from a previous commit.

### .gitignore
My `.gitignore` (image 1) became essential for keeping my repo secure and uncluttered. I excluded:

- sensitive files like `users.json`,
- my data directory,
- Python cache folders (`__pycache__/`),
- my `venv` environment,
- and system/editor files like `.vscode/` or `.DS_Store`.

Updating `.gitignore` as my project grew ensured I wasn’t accidentally committing private or unnecessary files. Keeping my remote repository clean and professional.

<img src="2.png" alt="Screenshot of .gitignore file from TO DO. app" width="300">

*Image 1: .gitignore file from TO DO. app*

### Branching
Implementing branching was a game-changer! It meant I could try out new features without worrying about breaking the main version, e.g.:

- `inheritance-addition` branch (image 2), I worked on adding new OOP features like `PriorityTask` and `GuestUser`.
- In another branch, I tested out Python’s `unittest` (image 3) module without cluttering up the main flow.
- `TDD_testing` branch

Branches gave me confidence to make mistakes because there was no risk to my stable code.

<img src="1.png" alt="Branching inheritance-addition CLI code" width="500">

*Image 2: Branching for inheritance, OOP features*

<img src="3.png" alt="Branching testing CLI code" width="500">

*Image 3: Branching for testing with unittest*




### Merging & Pulling Challenges
After merging `inheritance-addition` on GitHub, I didn't pull before pushing new commits in the local repository. This led to push rejections and a lot of confusion for a beginner.

Again, I ran into trouble when merging my `testing` branch, which didn’t have tracking information set up (image 4). Figuring out how to set my upstream branch fixed the issue, but it definitely showed me how important syncing is between local and remote repositories. Implementing `git status` would have helped me keep track of changes more effectively.

Understanding the relationship between local and remote branches, especially when it comes to merging and pulling are areas for improvement in my VCS use. Challenging myself, lots of googling and troubleshooting creates a good foundation to handle challenges that will arise in future projects.

<img src="4.png" alt="Merging & pulling issue example" width="500">

*Image 4: Merging & pulling issue with testing branch*

## Testing Evaluation

### Standard Testing Process
The standard testing process is about checking that each part of your code does what it’s supposed to do. You write tests for your functions and classes, run them, and fix anything if needed. This helps catch bugs early and makes sure your app works as expected every time you make a change.

I used unit testing to check the main features of my app after implementation. I used Python’s `unittest` so I could run all my tests in one go, see what passed or failed and fix any bugs in my code. This way, I always knew my main features were working and could catch issues early.

`test_tasks.py` ensured users could add tasks and mark them as complete.
```python
class TestTask(unittest.TestCase):
    def test_task_creation(self):
        task = Task("Supermarket Shopping")
        self.assertEqual(task.title, "Supermarket Shopping")
        self.assertFalse(task.completed)

    def test_mark_complete(self):
        task = Task("Supermarket Shopping")
        task.mark_complete()
        self.assertTrue(task.completed)
```

`test_user.py` verified there is no current user when a new user is created, ensures user starts in a logged out state.
```python
class TestUser(unittest.TestCase):
    def test_create_user(self):
        user = User()
        self.assertIsNone(user.get_current_user())
```

One of my biggest challenges during testing was dealing with my virtual environment (see image 6). I encountered various errors and bugs—mostly caused by conflicts between my venv and Homebrew. Sometimes, packages wouldn’t install correctly, or Python would end up using the wrong version, leading to import errors or missing dependencies when I tried to run my tests.

These issues slowed down my workflow and made it difficult to focus on actually testing my code. I had to spend a lot of extra time troubleshooting, reinstalling packages, and ensuring my virtual environment was set up properly before I could do any real work. Although it was frustrating, the experience taught me how crucial it is to maintain a consistent environment for testing. Next time, I’ll make sure to double-check my setup before running tests to avoid these kinds of problems.

<img src="6.png" alt="Screenshot of environment and dependency issues during testing" width="500">

*Image 6: Venv and dependency issues during testing*

### Test-Driven Development (TDD)
Test-Driven Development (TDD) is an approach where you start by writing a test before any actual code. You begin by creating a test that fails, then implement just enough functionality to pass that test, and finally, you refactor your code if necessary. This process ensures you concentrate on the intended behavior of your code and guarantees that everything is covered by tests from the outset.

I didn’t use strict TDD for this project, as a beginner I focused on just getting code working through manual testing and dabbling in standard testing processes. Reflecting on my project, here is how I could have implemented TDD and developed my code with this approach:

A practical TDD example: adding a method to return the task title in uppercase.

**User Story:**
- As a user, I want to see my task titles in uppercase for emphasis or when I need to quickly scan my list, so that important tasks stand out. the user is asked if they would like thier task in UPPERCASE or lowercase. Personally, when words are written in uppercase it highlights importance and urgency helping the user to easily identify tasks ata glance from others, along side the priority task.

Here’s how I could use TDD to add this feature: You wrote a test for a feature (title_upper) that does not exist yet, and the test fails with an AttributeError. This is the "red" phase of TDD: the test fails because the method is missing.

The next step is to implement the title_upper method in the Task class, then rerun the tests to see them pass ("green" phase)

1. **Write the test first (it will fail):**
```python
def test_title_upper(self):
    task = Task("Supermarket Shopping")
    self.assertEqual(task.title_upper(), "SUPERMARKET SHOPPING")
```
2. **Write the minimum code to pass the test:**
```python
class Task:
    # ...existing code...
    # ===== task UPPERCASE (TDD feature) =====
    def title_upper(self) -> str:
        return self.title.upper()
```
3. **Refactor if needed:**
- This method is already as simple as it gets.

This feature is useful for users who want to highlight or visually separate certain tasks. By using TDD, I made sure the method worked exactly as intended before adding it to the app, and the user story helped me focus on a real-world need.

example 2 TDD
1. Adding is_high_priority method to test_tasks.py

def test_is_high_priority(self): # TDD test 2
        from todo_manager.tasks import PriorityTask
        high_task = PriorityTask("Pay gas bill", "High")
        med_task = PriorityTask("Homework", "Medium")
        low_task = PriorityTask("Clean fridge", "Low")
        self.assertTrue(high_task.is_high_priority())
        self.assertFalse(med_task.is_high_priority())
        self.assertFalse(low_task.is_high_priority())

failed 

2. Added to tasks.py to make the pass
 class Task
  # ===== Check if task is high priority =====
    def is_high_priority(self) -> bool:
        return False

  class PRiorityTask:
  def is_high_priority(self) -> bool: # TDD 2 - Return True if this PriorityTask is High.
        return self.priority == "High"



Yes, it is still TDD if you follow the process: write a failing test, implement the method, and see the test pass. TDD is about driving development with tests, not necessarily about immediate integration into your app.

Nnew methods in your application code. user experience user sees high priority taks in red bold uppercase to visually highlight the urgency of that task.  This ensures your tests reflect real user needs and your codebase stays clean and purposeful. For your assignment, demonstrating the TDD cycle (fail → implement → pass) is correct—even if the method isn’t yet used in the main app.

 example screenshot of app after these two tdd testing and code improvements wrere added.


### Manual Testing and User Stories

Most of my testing was done manually, acting as a user and guided by user stories. I tried all main features of TO DO. by running the app constantly. Working through each user option (sign up, log in, guest, exit) and task menu (add,view, complete, delete), just like someone would in real life. This style of testing allowed me to understand more about my projects functionality, how it looked and felt from a user perspective in the CLI. Using user stories to guide my testing, e.g.:
  - **As a user I want to delete an old task from my task list.**
    - I tested loops via user input, ensuring there had to be tasks listed in order to delete a task, user input had to select the task number to delete the associated task. Other inputs were handled gracefully. If the task deleted was the only task on the list, user is told ther is no tasks and promted to add a new one. I checked that the task was removed from the list afterwards. I also verified the input prompts were clear, visually with different colours and styalised bold and readability.
  - **As a user I want to mark a task as complete.**
    - I tested the `mark_complete` method, made sure completed tasks were displayed with a green tick emoji and checked that the app showed the updated task list to the viewer when completed. I tested user input by trying to complete already completed tasks and enter characters outside of the task list numbers to ensure errors were handled gracefully.
  - **As a guest user, I tested the app without creating an account and ensuring no data was saved.**
    - Testing the guest user mode, I could add, view, delete and complete tasks during the session but when I exited and reopened the app, all task and user data was not stored. As a user, I made sure that anyone wanting to try the app in guest mode was told several times that their data would not be saved.

Seeing the app in action gave me a clear view of how everything fits together. Manual testing helped catch bugs and user experience issues—like readability, unclear instructions, and confusing navigation—that automated tests miss. It also confirmed the app felt intuitive and user-friendly.

Testing as an actual user revealed issues only visible when app parts interact, ensuring the app is both functional and enjoyable. Immersing myself in real-use scenarios focused me on practical needs, resulting in a visually appealing, easy-to-navigate, and effective app.

### Conclusion

Looking back on this project, I learned a lot about both version control and testing. Using Git and GitHub gave me a safety net, let me track my progress, and helped me build good habits for future team projects. I saw firsthand how important it is to write clear commit messages, keep your .gitignore up to date, and use branches to experiment safely. Even when I ran into problems—like merge conflicts or environment issues—I learned how to troubleshoot and keep my codebase clean and organized.

On the testing side, focusing on core tests, user stories, and multiple types of testing helped me confidently develop and refactor my TO DO. app. Manual testing from a user’s perspective made sure the app was actually enjoyable and easy to use, not just bug-free. Writing and running unit tests gave me peace of mind that my main features worked, and exploring TDD showed me a new way to approach building features in the future.

The whole process taught me the importance of planning, organizing, and continuously improving my workflow. I now understand how version control and testing work together to make development smoother and less stressful. These skills have given me a solid foundation to build upon with future projects.



### Reference List

https://www.geeksforgeeks.org/git/version-control-systems/
https://www.geeksforgeeks.org/git/centralized-vs-distributed-version-control-which-one-should-we-choose/
https://www.alooba.com/skills/tools/version-control/subversion/
https://nulab.com/learn/software-development/git-vs-svn-version-control-system/
https://www.linode.com/docs/guides/svn-vs-git/
https://moldstud.com/articles/p-git-vs-subversion-comparison-for-version-control
https://www.geeksforgeeks.org/git/difference-between-github-and-svn/
https://www.perforce.com/blog/vcs/git-vs-svn-what-difference
https://www.geeksforgeeks.org/software-engineering/test-driven-development-tdd/
https://vandangogna.medium.com/a-practical-example-using-test-driven-development-88b4536ac574
https://medium.com/@bethqiang/the-absolute-beginners-guide-to-test-driven-development-with-a-practical-example-c39e73a11631

